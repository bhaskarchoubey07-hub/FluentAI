from __future__ import annotations

from typing import Any

from sqlalchemy import func, select

from app.database import ProgressRecord, User, get_current_streak, get_session
from app.lessons import get_lessons


def save_progress(user_id: int, language: str, lesson: str, score: float, accuracy: float) -> None:
    with get_session() as session:
        existing = session.scalar(
            select(ProgressRecord).where(
                ProgressRecord.user_id == user_id,
                ProgressRecord.language == language,
                ProgressRecord.lesson == lesson,
            )
        )
        if existing:
            existing.score = max(existing.score, score)
            existing.accuracy = max(existing.accuracy, accuracy)
        else:
            session.add(
                ProgressRecord(
                    user_id=user_id,
                    language=language,
                    lesson=lesson,
                    score=score,
                    accuracy=accuracy,
                )
            )


def get_user_progress(user_id: int, language: str | None = None) -> list[ProgressRecord]:
    with get_session() as session:
        stmt = select(ProgressRecord).where(ProgressRecord.user_id == user_id)
        if language:
            stmt = stmt.where(ProgressRecord.language == language)
        stmt = stmt.order_by(ProgressRecord.completed_at.desc())
        return list(session.scalars(stmt).all())


def summarize_progress(user_id: int, language: str) -> dict[str, Any]:
    records = get_user_progress(user_id, language)
    total_lessons = len(get_lessons(language))
    completed_lessons = {record.lesson for record in records}
    avg_score = sum(record.score for record in records) / len(records) if records else 0.0
    avg_accuracy = sum(record.accuracy for record in records) / len(records) if records else 0.0

    return {
        "completed": len(completed_lessons),
        "total": total_lessons,
        "avg_score": avg_score,
        "avg_accuracy": avg_accuracy,
        "completed_lessons": completed_lessons,
        "streak": get_current_streak(user_id),
    }


def get_leaderboard(limit: int = 10) -> list[dict[str, Any]]:
    with get_session() as session:
        rows = (
            session.query(
                ProgressRecord.user_id,
                func.avg(ProgressRecord.accuracy).label("accuracy"),
                func.count(ProgressRecord.id).label("completed"),
            )
            .group_by(ProgressRecord.user_id)
            .order_by(func.avg(ProgressRecord.accuracy).desc(), func.count(ProgressRecord.id).desc())
            .limit(limit)
            .all()
        )
        usernames = {user.id: user.username for user in session.scalars(select(User)).all()}

    leaderboard = []
    for rank, row in enumerate(rows, start=1):
        leaderboard.append(
            {
                "rank": rank,
                "username": usernames.get(row.user_id, f"user-{row.user_id}"),
                "accuracy": float(row.accuracy or 0.0),
                "completed": int(row.completed or 0),
            }
        )
    return leaderboard


def get_personalized_suggestions(user_id: int, language: str) -> list[str]:
    progress = summarize_progress(user_id, language)
    suggestions: list[str] = []

    if progress["completed"] == 0:
        suggestions.append(f"Start with the first {language} lesson to build your core vocabulary.")
    if progress["avg_accuracy"] < 70:
        suggestions.append("Review lesson examples once more and ask the AI tutor for error explanations.")
    if progress["avg_accuracy"] >= 70:
        suggestions.append("Try longer, more natural sentences in the AI Tutor to improve fluency.")
    if progress["completed"] == progress["total"] and progress["total"] > 0:
        suggestions.append("You have completed the lesson track. Reinforce it with tutor chats and repeat quizzes.")
    if progress["streak"] < 3:
        suggestions.append("A short daily study session will help you build a streak.")
    return suggestions[:3]
