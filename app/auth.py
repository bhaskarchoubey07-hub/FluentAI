from __future__ import annotations

import streamlit as st
from sqlalchemy import select

from app.database import User, get_session
from app.utils import hash_password, verify_password


def create_user(username: str, password: str) -> tuple[bool, str]:
    normalized = username.strip().lower()
    if len(normalized) < 3:
        return False, "Username must be at least 3 characters."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    with get_session() as session:
        existing = session.scalar(select(User).where(User.username == normalized))
        if existing:
            return False, "Username already exists."

        user = User(username=normalized, password=hash_password(password))
        session.add(user)
    return True, "Account created successfully. Please log in."


def authenticate_user(username: str, password: str) -> tuple[bool, str, User | None]:
    normalized = username.strip().lower()
    with get_session() as session:
        user = session.scalar(select(User).where(User.username == normalized))
        if not user or not verify_password(password, user.password):
            return False, "Invalid username or password.", None
        return True, "Login successful.", user


def logout() -> None:
    for key in ("authenticated", "user_id", "username", "chat_messages"):
        if key == "chat_messages":
            st.session_state[key] = []
        elif key == "authenticated":
            st.session_state[key] = False
        elif key == "user_id":
            st.session_state[key] = None
        else:
            st.session_state[key] = ""
