from __future__ import annotations

import bcrypt
import streamlit as st

from app.config import get_settings


def hash_password(password: str) -> str:
    settings = get_settings()
    salt = bcrypt.gensalt(rounds=settings.password_rounds)
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))


def init_session_state() -> None:
    defaults = {
        "authenticated": False,
        "user_id": None,
        "username": "",
        "selected_language": "Spanish",
        "chat_messages": [],
        "quiz_state": {},
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def reset_quiz_state() -> None:
    st.session_state.quiz_state = {}


def language_badge(language: str) -> str:
    badges = {
        "Spanish": "ES",
        "French": "FR",
        "German": "DE",
        "Hindi": "HI",
    }
    return badges.get(language, language[:2].upper())


def percentage(value: float) -> str:
    return f"{value:.0f}%"
