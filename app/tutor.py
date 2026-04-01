from __future__ import annotations

from typing import Iterable

from openai import OpenAI
from sqlalchemy import select

from app.config import get_settings
from app.database import ChatHistory, get_session


def get_client() -> OpenAI:
    settings = get_settings()
    if settings.llm_provider == "groq":
        if not settings.groq_api_key:
            raise ValueError("GROQ_API_KEY is not configured. Add it to your .env file or Streamlit secrets.")
        return OpenAI(api_key=settings.groq_api_key, base_url="https://api.groq.com/openai/v1")

    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not configured. Add it to your .env file or Streamlit secrets.")
    return OpenAI(api_key=settings.openai_api_key)


def build_system_prompt(language: str) -> str:
    return (
        f"You are a professional language tutor helping users learn {language}. "
        "Correct mistakes gently, explain why something is wrong, offer better alternatives, "
        "and keep answers concise but educational. Encourage active learning with examples."
    )


def load_chat_history(user_id: int, language: str) -> list[dict[str, str]]:
    with get_session() as session:
        messages = session.scalars(
            select(ChatHistory)
            .where(ChatHistory.user_id == user_id, ChatHistory.language == language)
            .order_by(ChatHistory.created_at.asc())
        ).all()
    return [{"role": message.role, "content": message.message} for message in messages]


def persist_message(user_id: int, language: str, role: str, message: str) -> None:
    with get_session() as session:
        session.add(ChatHistory(user_id=user_id, language=language, role=role, message=message))


def stream_tutor_reply(language: str, history: list[dict[str, str]]) -> Iterable[str]:
    client = get_client()
    settings = get_settings()
    messages = [{"role": "system", "content": build_system_prompt(language)}] + history
    stream = client.chat.completions.create(
        model=settings.llm_model,
        messages=messages,
        temperature=0.7,
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        if delta:
            yield delta


def generate_learning_tip(language: str, progress_summary: dict[str, float]) -> str:
    base_tip = (
        f"Focus on {language} for 10 minutes today. "
        f"You have completed {progress_summary['completed']} of {progress_summary['total']} lessons."
    )
    if progress_summary["avg_accuracy"] < 70:
        return base_tip + " Review vocabulary aloud and ask the tutor for correction drills."
    return base_tip + " Push yourself with free-form sentences in the tutor chat."
