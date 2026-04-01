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


def _parse_int_secret(name: str, default: int) -> int:
    raw_value = _secret(name, default)
    try:
        return int(str(raw_value).strip())
    except (TypeError, ValueError):
        return default


@dataclass(frozen=True)
class Settings:
    app_name: str
    database_url: str
    llm_provider: str
    llm_model: str
    openai_api_key: str
    groq_api_key: str
    password_rounds: int


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    database_url = _normalize_database_url(_secret("DATABASE_URL", ""))
    llm_provider = str(_secret("LLM_PROVIDER", "openai")).strip().lower()
    llm_model = str(_secret("LLM_MODEL", "")).strip()
    openai_model = str(_secret("OPENAI_MODEL", "gpt-4o-mini")).strip()

    if not llm_model:
        llm_model = "llama-3.3-70b-versatile" if llm_provider == "groq" else openai_model

    return Settings(
        app_name="FluentAI",
        database_url=database_url,
        llm_provider=llm_provider,
        llm_model=llm_model,
        openai_api_key=_secret("OPENAI_API_KEY", "").strip(),
        groq_api_key=_secret("GROQ_API_KEY", "").strip(),
        password_rounds=_parse_int_secret("PASSWORD_ROUNDS", 12),
    )
