import os
from dataclasses import dataclass
from functools import lru_cache
from typing import Any

from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except Exception:  # pragma: no cover
    st = None


def _secret(name: str, default: Any = None) -> Any:
    if st is not None:
        try:
            value = st.secrets.get(name)
            if value not in (None, ""):
                return value
        except Exception:
            pass
    return os.getenv(name, default)


def _normalize_database_url(database_url: str) -> str:
    normalized = database_url.strip()
    if not normalized:
        return "sqlite:///fluentai.db"

    if normalized.startswith("postgres://"):
        normalized = normalized.replace("postgres://", "postgresql+psycopg2://", 1)
    elif normalized.startswith("postgresql://") and "+psycopg2" not in normalized:
        normalized = normalized.replace("postgresql://", "postgresql+psycopg2://", 1)

    return normalized


@dataclass(frozen=True)
class Settings:
    app_name: str
    database_url: str
    openai_api_key: str
    openai_model: str
    password_rounds: int


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    database_url = _normalize_database_url(_secret("DATABASE_URL", ""))

    return Settings(
        app_name="FluentAI",
        database_url=database_url,
        openai_api_key=_secret("OPENAI_API_KEY", "").strip(),
        openai_model=_secret("OPENAI_MODEL", "gpt-4o-mini").strip(),
        password_rounds=int(_secret("PASSWORD_ROUNDS", 12)),
    )
