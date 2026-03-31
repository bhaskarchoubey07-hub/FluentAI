from __future__ import annotations

from typing import Any

from sqlalchemy import func, select

from app.database import ProgressRecord, User, get_current_streak, get_session
from app.lessons import get_lesson, get_lessons


LEVELS = [
    ("Rookie", 0),
    ("Explorer", 60),
    ("Communicator", 140),
    ("Conversationalist", 240),
    ("Storyteller", 360),
    ("Fluent Climber", 520),
    ("Language Mentor", 720),
]


def _xp_for_record(record: ProgressRecord) -> int:
    lesson_bonus = 20
    accuracy_bonus = int(record.accuracy * 0.6)
    score_bonus = int(record.score * 8)
    return lesson_bonus + accuracy_bonus + score_bonus


def get_level_from_xp(xp: int) -> dict[str, Any]:
    current_name = LEVELS[0][0]
    current_threshold = LEVELS[0][1]
    next_name = None
    next_threshold = None

    for index, (name, threshold) in enumerate(LEVELS):
        if xp >= threshold:
            current_name = name
            current_threshold = threshold
            if index + 1 < len(LEVELS):
                next_name, next_threshold = LEVELS[index + 1]
        else:
            next_name = name
            next_threshold = threshold
            break

    if next_threshold is None:
        progress = 100.0
        xp_to_next = 0
    else:
        segment = max(next_threshold - current_threshold, 1)
        progress = min(100.0, ((xp - current_threshold) / segment) * 100)
        xp_to_next = max(next_threshold - xp, 0)

    return {
        "name": current_name,
        "xp": xp,
        "current_threshold": current_threshold,
        "next_name": next_name,
        "next_threshold": next_threshold,
        "progress": progress,
        "xp_to_next": xp_to_next,
    }


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
    xp = sum(_xp_for_record(record) for record in records)
    focus_counts: dict[str, int] = {}
    for record in records:
        lesson = get_lesson(language, record.lesson)
        if lesson:
            focus = lesson["focus"]
            focus_counts[focus] = focus_counts.get(focus, 0) + 1

    return {
        "completed": len(completed_lessons),
        "total": total_lessons,
        "avg_score": avg_score,
        "avg_accuracy": avg_accuracy,
        "completed_lessons": completed_lessons,
        "streak": get_current_streak(user_id),
        "xp": xp,
        "level": get_level_from_xp(xp),
        "focus_counts": focus_counts,
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
                "level": get_level_from_xp(int((row.completed or 0) * 40 + (row.accuracy or 0) * 2))["name"],
            }
        )
    return leaderboard


def get_personalized_suggestions(user_id: int, language: str) -> list[str]:
    progress = summarize_progress(user_id, language)
    suggestions: list[str] = []
    weakest_focus = None
    if progress["focus_counts"]:
        weakest_focus = min(progress["focus_counts"], key=progress["focus_counts"].get)

    if progress["completed"] == 0:
        suggestions.append(f"Start with the first {language} lesson to build your core vocabulary.")
    if progress["avg_accuracy"] < 70:
        suggestions.append("Review lesson examples once more and ask the AI tutor for error explanations.")
    if progress["avg_accuracy"] >= 70:
        suggestions.append("Try longer, more natural sentences in the AI Tutor to improve fluency.")
    if weakest_focus:
        suggestions.append(f"You have spent less time on {weakest_focus.lower()} practice. Add one lesson in that area next.")
    if progress["completed"] == progress["total"] and progress["total"] > 0:
        suggestions.append("You have completed the lesson track. Reinforce it with tutor chats and repeat quizzes.")
    if progress["streak"] < 3:
        suggestions.append("A short daily study session will help you build a streak.")
    return suggestions[:3]
