from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Support running this file directly on platforms like Streamlit Cloud,
# where `app/main.py` may be selected as the app entrypoint.
if __package__ in (None, ""):
    repo_root = Path(__file__).resolve().parent.parent
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

from app.auth import authenticate_user, create_user, logout
from app.config import get_settings
from app.database import get_active_database_url, init_db
from app.lessons import get_lesson_catalog_summary, get_languages, get_lessons, get_recommended_next_step
from app.progress import get_leaderboard, get_personalized_suggestions, get_user_progress, save_progress, summarize_progress
from app.quiz import build_quiz, grade_quiz
from app.tutor import generate_learning_tip, load_chat_history, persist_message, stream_tutor_reply
from app.utils import init_session_state, language_badge, percentage, reset_quiz_state


def apply_theme() -> None:
    st.set_page_config(page_title="FluentAI", page_icon="🌍", layout="wide")
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(255, 209, 102, 0.28), transparent 24%),
                radial-gradient(circle at top right, rgba(17, 138, 178, 0.18), transparent 30%),
                linear-gradient(180deg, #fffdf7 0%, #f5f8fc 100%);
        }
        .hero-card, .panel-card {
            border: 1px solid rgba(15, 23, 42, 0.08);
            background: rgba(255,255,255,0.88);
            backdrop-filter: blur(8px);
            border-radius: 20px;
            padding: 1.2rem 1.3rem;
            box-shadow: 0 14px 36px rgba(15, 23, 42, 0.08);
        }
        .metric-card {
            border-radius: 18px;
            padding: 1rem;
            background: linear-gradient(135deg, rgba(17,138,178,0.08), rgba(255,209,102,0.18));
            border: 1px solid rgba(17,138,178,0.10);
        }
        .lesson-chip {
            display: inline-block;
            padding: 0.25rem 0.6rem;
            border-radius: 999px;
            background: #0f766e;
            color: white;
            font-size: 0.8rem;
            margin-right: 0.35rem;
        }
        .xp-card {
            border-radius: 18px;
            padding: 1rem 1.2rem;
            background: linear-gradient(135deg, rgba(245,158,11,0.14), rgba(14,165,233,0.12));
            border: 1px solid rgba(245,158,11,0.20);
            margin-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def auth_screen() -> None:
    st.title("🌍 FluentAI")
    st.caption("A modular AI language learning app built with Streamlit, SQLAlchemy, and OpenAI.")

    left, right = st.columns([1.1, 0.9], gap="large")
    with left:
        st.markdown(
            """
            <div class="hero-card">
                <h2>Learn like a SaaS product, not a demo</h2>
                <p>Study structured lessons, practice with quizzes, get corrected by an AI tutor, and keep all your progress saved.</p>
                <p><strong>Languages:</strong> Spanish, French, German, Hindi</p>
                <p><strong>Included:</strong> login/signup, persistent progress, chat history, streaks, leaderboard, and personalized suggestions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        tab_login, tab_signup = st.tabs(["Login", "Sign Up"])
        with tab_login:
            with st.form("login_form", clear_on_submit=False):
                username = st.text_input("Username", key="login_username")
                password = st.text_input("Password", type="password", key="login_password")
                submitted = st.form_submit_button("Login", use_container_width=True)
            if submitted:
                success, message, user = authenticate_user(username, password)
                if success and user:
                    st.session_state.authenticated = True
                    st.session_state.user_id = user.id
                    st.session_state.username = user.username
                    st.session_state.chat_messages = []
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

        with tab_signup:
            with st.form("signup_form", clear_on_submit=True):
                username = st.text_input("Choose a username", key="signup_username")
                password = st.text_input("Choose a password", type="password", key="signup_password")
                submitted = st.form_submit_button("Create account", use_container_width=True)
            if submitted:
                success, message = create_user(username, password)
                if success:
                    st.success(message)
                else:
                    st.error(message)


def sidebar() -> str:
    with st.sidebar:
        st.markdown(f"## 👋 {st.session_state.username}")
        language = st.selectbox("Learning language", options=get_languages(), key="selected_language")
        st.markdown(f"**Code:** `{language_badge(language)}`")
        page = st.radio("Navigate", ["Home", "Lessons", "AI Tutor", "Quiz", "Progress"])
        st.caption("🎤 Voice input is ready for a future speech-to-text integration.")
        if st.button("Logout", use_container_width=True):
            logout()
            st.rerun()
    return page


def home_page() -> None:
    language = st.session_state.selected_language
    summary = summarize_progress(st.session_state.user_id, language)
    suggestions = get_personalized_suggestions(st.session_state.user_id, language)
    tip = generate_learning_tip(language, summary)
    catalog = get_lesson_catalog_summary(language)
    level = summary["level"]

    st.title("🏠 Home")
    st.markdown(
        f"""
        <div class="hero-card">
            <h2>Keep your {language} momentum going</h2>
            <p>{tip}</p>
            <p>{get_recommended_next_step(language, summary["completed_lessons"])}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="xp-card">
            <h3>Level {level['name']}</h3>
            <p>{level['xp']} XP earned in {language}.</p>
            <p>{'Next level: ' + level['next_name'] if level['next_name'] else 'You reached the current top learner tier.'}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(level["progress"] / 100 if level["progress"] else 0.0, text=f"{level['progress']:.0f}% to next level")

    cols = st.columns(4)
    metrics = [
        (f"{summary['completed']}/{summary['total']}", "Lessons Completed"),
        (f"{summary['avg_score']:.1f}", "Average Score"),
        (percentage(summary["avg_accuracy"]), "Accuracy"),
        (str(summary["streak"]), "Day Streak"),
    ]
    for col, (value, label) in zip(cols, metrics):
        with col:
            st.markdown(f"<div class='metric-card'><h3>{value}</h3><p>{label}</p></div>", unsafe_allow_html=True)

    st.subheader("✨ Personalized suggestions")
    for suggestion in suggestions:
        st.info(suggestion)

    st.subheader("🧭 Learning map")
    map_cols = st.columns(3)
    map_cols[0].metric("Curriculum lessons", str(catalog["count"]))
    map_cols[1].metric("Estimated study time", f"{catalog['minutes']} min")
    map_cols[2].metric("Focus areas", str(len(catalog["focus_areas"])))
    st.caption(
        "Curriculum mix: "
        + ", ".join(f"{level_name} {count}" for level_name, count in catalog["levels"].items())
    )

    st.subheader("🏆 Leaderboard")
    leaderboard = get_leaderboard()
    if leaderboard:
        st.dataframe(leaderboard, use_container_width=True, hide_index=True)
    else:
        st.caption("No leaderboard data yet. Complete a lesson or quiz to get started.")


def lessons_page() -> None:
    language = st.session_state.selected_language
    st.title("📘 Lessons")
    st.caption(f"Structured learning path for {language} with beginner and intermediate content.")

    for lesson in get_lessons(language):
        with st.container(border=True):
            st.markdown(f"### {lesson['title']}")
            st.markdown(
                f"<span class='lesson-chip'>{lesson['level']}</span><span class='lesson-chip'>{lesson['focus']}</span>",
                unsafe_allow_html=True,
            )
            st.write(lesson["concept"])
            meta_left, meta_right = st.columns([1, 1])
            with meta_left:
                st.markdown("**Learning goals**")
                for goal in lesson["learning_goals"]:
                    st.write(f"• {goal}")
            with meta_right:
                st.markdown("**Key vocabulary**")
                st.write(", ".join(lesson["vocabulary"]))
                st.caption(f"Suggested study time: {lesson['minutes']} minutes")
            left, right = st.columns([1.4, 1])
            with left:
                st.markdown("**Examples**")
                for example in lesson["examples"]:
                    st.write(f"• {example}")
            with right:
                st.markdown("**Grammar tip**")
                st.success(lesson["grammar_tip"])
                st.markdown("**Practice prompt**")
                st.write(lesson["practice_prompt"])
            if st.button(f"Mark '{lesson['title']}' as reviewed", key=f"review_{language}_{lesson['title']}"):
                save_progress(st.session_state.user_id, language, lesson["title"], 1.0, 100.0)
                st.success("Lesson review saved.")


def tutor_page() -> None:
    language = st.session_state.selected_language
    st.title("🤖 AI Tutor")
    st.caption("Practice natural conversation, get corrections, and ask grammar questions.")

    if st.session_state.get("chat_language") != language:
        st.session_state.chat_messages = load_chat_history(st.session_state.user_id, language)
        st.session_state.chat_language = language

    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input(f"Message your {language} tutor")
    if prompt:
        user_message = {"role": "user", "content": prompt}
        st.session_state.chat_messages.append(user_message)
        persist_message(st.session_state.user_id, language, "user", prompt)

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                placeholder = st.empty()
                full_response = ""
                for chunk in stream_tutor_reply(language, st.session_state.chat_messages):
                    full_response += chunk
                    placeholder.markdown(full_response)
                st.session_state.chat_messages.append({"role": "assistant", "content": full_response})
                persist_message(st.session_state.user_id, language, "assistant", full_response)
            except Exception as exc:
                st.error(f"Unable to reach the AI tutor right now: {exc}")


def quiz_page() -> None:
    language = st.session_state.selected_language
    lessons = get_lessons(language)
    st.title("🧠 Quiz")
    st.caption("Multiple choice and fill-in-the-blank practice.")

    lesson_title = st.selectbox("Choose a lesson", [lesson["title"] for lesson in lessons], key="quiz_lesson")
    questions = build_quiz(language, lesson_title)
    if not questions:
        st.warning("No quiz is available for this lesson.")
        return

    answers: list[str] = []
    with st.form("quiz_form"):
        for index, question in enumerate(questions, start=1):
            st.markdown(f"**Q{index}. {question['question']}**")
            if question["type"] == "mcq":
                answer = st.radio("Select an answer", question["options"], key=f"quiz_{index}", label_visibility="collapsed")
            else:
                answer = st.text_input("Your answer", key=f"quiz_{index}", placeholder="Type here")
            answers.append(answer)
        submitted = st.form_submit_button("Submit Quiz", use_container_width=True)

    if submitted:
        results = grade_quiz(questions, answers)
        save_progress(st.session_state.user_id, language, lesson_title, results["score"], results["accuracy"])
        st.success(f"Score: {results['correct']}/{results['total']} | Accuracy: {results['accuracy']:.0f}%")
        if results["accuracy"] >= 85:
            st.balloons()
        with st.expander("Answer review"):
            for question, answer in zip(questions, answers):
                st.write(f"Question: {question['question']}")
                st.write(f"Your answer: {answer}")
                st.write(f"Correct answer: {question['answer']}")
                st.write("---")
        reset_quiz_state()


def progress_page() -> None:
    language = st.session_state.selected_language
    summary = summarize_progress(st.session_state.user_id, language)
    records = get_user_progress(st.session_state.user_id, language)
    level = summary["level"]

    st.title("📊 Progress")
    st.caption(f"Your learning performance in {language}.")

    st.markdown(
        f"""
        <div class="xp-card">
            <h3>{level['name']}</h3>
            <p>{level['xp']} XP earned so far.</p>
            <p>{f"{level['xp_to_next']} XP until {level['next_name']}" if level['next_name'] else "Top level reached in the current progression system."}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(level["progress"] / 100 if level["progress"] else 0.0, text=f"{level['progress']:.0f}% through current level")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Completed lessons", f"{summary['completed']}/{summary['total']}")
    col2.metric("Average score", f"{summary['avg_score']:.1f}")
    col3.metric("Accuracy", percentage(summary["avg_accuracy"]))
    col4.metric("Current streak", f"{summary['streak']} days")

    st.subheader("Suggested next actions")
    for suggestion in get_personalized_suggestions(st.session_state.user_id, language):
        st.write(f"• {suggestion}")

    if summary["focus_counts"]:
        st.subheader("Focus coverage")
        st.dataframe(
            [{"Focus": focus, "Completed lessons": count} for focus, count in summary["focus_counts"].items()],
            use_container_width=True,
            hide_index=True,
        )

    if records:
        st.subheader("Recent activity")
        st.dataframe(
            [
                {
                    "Lesson": record.lesson,
                    "Score": record.score,
                    "Accuracy": f"{record.accuracy:.0f}%",
                    "Completed": record.completed_at.strftime("%Y-%m-%d %H:%M"),
                }
                for record in records
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No saved progress yet. Complete a lesson or quiz to populate this dashboard.")


def run() -> None:
    apply_theme()
    init_db()
    init_session_state()
    settings = get_settings()

    if not settings.database_url.startswith("sqlite") and get_active_database_url().startswith("sqlite"):
        st.warning("PostgreSQL could not be reached, so FluentAI started with SQLite fallback storage.")

    if not st.session_state.authenticated:
        auth_screen()
        return

    page = sidebar()
    if page == "Home":
        home_page()
    elif page == "Lessons":
        lessons_page()
    elif page == "AI Tutor":
        tutor_page()
    elif page == "Quiz":
        quiz_page()
    else:
        progress_page()
