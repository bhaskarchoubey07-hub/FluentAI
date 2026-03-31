from __future__ import annotations

import random
from typing import Any

from app.lessons import get_lesson


QUIZ_BANK: dict[str, dict[str, list[dict[str, Any]]]] = {
    "Spanish": {
        "Greetings and Introductions": [
            {"type": "mcq", "question": "What does 'Hola' mean?", "options": ["Goodbye", "Hello", "Please", "Friend"], "answer": "Hello"},
            {"type": "fill", "question": "Complete the phrase: 'Me ____ Ana.'", "answer": "llamo"},
            {"type": "mcq", "question": "Which phrase means 'Nice to meet you'?", "options": ["Buenos dias", "Mucho gusto", "Hasta luego", "Buenas noches"], "answer": "Mucho gusto"},
        ],
        "Present Tense Basics": [
            {"type": "mcq", "question": "Which sentence means 'I study Spanish'?", "options": ["Yo estudio espanol", "Tu hablas espanol", "Nosotros vivimos aqui", "El libro es rojo"], "answer": "Yo estudio espanol"},
            {"type": "fill", "question": "Complete: 'Tu ____ despacio.'", "answer": "hablas"},
            {"type": "mcq", "question": "Why are verb endings important in Spanish?", "options": ["They show color", "They show the subject", "They remove articles", "They make nouns plural"], "answer": "They show the subject"},
        ],
    },
    "French": {
        "Bonjour Basics": [
            {"type": "mcq", "question": "What does 'Bonsoir' mean?", "options": ["Good evening", "Good afternoon", "Thank you", "Please"], "answer": "Good evening"},
            {"type": "fill", "question": "Complete: 'Je m'____ Louis.'", "answer": "appelle"},
            {"type": "mcq", "question": "Which phrase is a polite thank you?", "options": ["Bonjour", "Merci beaucoup", "Au revoir", "Bonne nuit"], "answer": "Merci beaucoup"},
        ],
        "Simple Sentence Structure": [
            {"type": "mcq", "question": "Which sentence means 'You like music'?", "options": ["Je lis un livre", "Tu aimes la musique", "Ils parlent francais", "Nous sommes ici"], "answer": "Tu aimes la musique"},
            {"type": "fill", "question": "Complete: 'Ils parlent ____.'", "answer": "francais"},
            {"type": "mcq", "question": "What is the basic French sentence order here?", "options": ["Verb-subject-object", "Subject-verb-object", "Object-subject-verb", "Adjective-noun-verb"], "answer": "Subject-verb-object"},
        ],
    },
    "German": {
        "Everyday Greetings": [
            {"type": "mcq", "question": "What does 'Guten Morgen' mean?", "options": ["Good night", "Good afternoon", "Good morning", "See you later"], "answer": "Good morning"},
            {"type": "fill", "question": "Complete: 'Ich ____ Max.'", "answer": "heisse"},
            {"type": "mcq", "question": "Which phrase means 'Nice to meet you'?", "options": ["Freut mich", "Auf Wiedersehen", "Gute Nacht", "Bis spaeter"], "answer": "Freut mich"},
        ],
        "Verb Position Fundamentals": [
            {"type": "mcq", "question": "Which sentence correctly places the verb second?", "options": ["Ich Deutsch lerne", "Deutsch ich lerne", "Ich lerne Deutsch", "Lerne ich Deutsch"], "answer": "Ich lerne Deutsch"},
            {"type": "fill", "question": "Complete: 'Er ____ Wasser.'", "answer": "trinkt"},
            {"type": "mcq", "question": "In a main German clause, where is the conjugated verb usually placed?", "options": ["First", "Second", "Last", "It can never move"], "answer": "Second"},
        ],
    },
    "Hindi": {
        "Namaste and Introductions": [
            {"type": "mcq", "question": "What does 'Dhanyavaad' mean?", "options": ["Please", "Thank you", "Hello", "Goodbye"], "answer": "Thank you"},
            {"type": "fill", "question": "Complete: 'Mera ____ Riya hai.'", "answer": "naam"},
            {"type": "mcq", "question": "Which phrase asks 'How are you?' politely?", "options": ["Aap kaise hain", "Mera naam hai", "Dhanyavaad", "Namaste dost"], "answer": "Aap kaise hain"},
        ],
        "Simple Present Sentences": [
            {"type": "mcq", "question": "Which sentence means 'We play'?", "options": ["Main padhta hoon", "Hum khelte hain", "Woh gaana gaati hai", "Aap kaise hain"], "answer": "Hum khelte hain"},
            {"type": "fill", "question": "Complete: 'Woh gaana ____ hai.'", "answer": "gaati"},
            {"type": "mcq", "question": "Why do Hindi verb forms change in many present tense sentences?", "options": ["Only for color words", "Because of gender and number", "Because articles disappear", "Only in questions"], "answer": "Because of gender and number"},
        ],
    },
}


def _distractors(correct_answer: str, lesson: dict[str, Any], pool: list[str]) -> list[str]:
    candidates = [item for item in pool if item.lower() != correct_answer.lower()]
    random.shuffle(candidates)
    picks = candidates[:3]
    while len(picks) < 3:
        picks.append(f"Option {len(picks) + 1}")
    options = picks + [correct_answer]
    random.shuffle(options)
    return options


def _build_example_questions(lesson: dict[str, Any]) -> list[dict[str, Any]]:
    example_questions: list[dict[str, Any]] = []
    examples = lesson["examples"][:2]
    meanings_pool: list[str] = []
    for item in lesson["examples"]:
        parts = item.split(" - ", maxsplit=1)
        if len(parts) == 2:
            meanings_pool.append(parts[1].strip())

    for example in examples:
        parts = example.split(" - ", maxsplit=1)
        if len(parts) != 2:
            continue
        foreign_text, meaning = parts[0].strip(), parts[1].strip()
        example_questions.append(
            {
                "type": "mcq",
                "question": f"What does '{foreign_text}' mean?",
                "options": _distractors(meaning, lesson, meanings_pool + ["Please", "Tomorrow", "Teacher", "Family"]),
                "answer": meaning,
            }
        )
    return example_questions


def _build_vocab_question(lesson: dict[str, Any]) -> dict[str, Any]:
    word = lesson["vocabulary"][0]
    return {
        "type": "fill",
        "question": f"Type this key vocabulary item exactly as shown in the lesson: '{word}'",
        "answer": word.lower(),
    }


def _build_goal_question(lesson: dict[str, Any]) -> dict[str, Any]:
    focus = lesson["focus"]
    goals = lesson["learning_goals"]
    answer = goals[0]
    distractors = _distractors(answer, lesson, goals + ["Memorize random dates", "Write code snippets", "Study unrelated history"])
    return {
        "type": "mcq",
        "question": f"Which learning goal best matches this {focus.lower()} lesson?",
        "options": distractors,
        "answer": answer,
    }


def _build_grammar_question(lesson: dict[str, Any]) -> dict[str, Any]:
    tip = lesson["grammar_tip"]
    keyword = lesson["vocabulary"][min(1, len(lesson["vocabulary"]) - 1)]
    return {
        "type": "fill",
        "question": f"Grammar recall: type this lesson word connected to the grammar tip or examples: '{keyword}'",
        "answer": keyword.lower(),
        "explanation": tip,
    }


def build_quiz(language: str, lesson_title: str) -> list[dict[str, Any]]:
    lesson = get_lesson(language, lesson_title)
    if not lesson:
        return []

    questions = QUIZ_BANK.get(language, {}).get(lesson_title)
    if questions:
        return questions + build_fallback_quiz(language, lesson_title, include_intro=False)[:2]
    return build_fallback_quiz(language, lesson_title)


def build_fallback_quiz(language: str, lesson_title: str, include_intro: bool = True) -> list[dict[str, Any]]:
    lesson = get_lesson(language, lesson_title)
    if not lesson:
        return []

    questions: list[dict[str, Any]] = []
    if include_intro:
        questions.append(
            {
                "type": "mcq",
                "question": f"What is the main focus of '{lesson['title']}'?",
                "options": _distractors(lesson["focus"], lesson, [lesson["focus"], "Pronunciation only", "Writing code", "Unrelated culture facts"]),
                "answer": lesson["focus"],
            }
        )

    questions.extend(_build_example_questions(lesson))
    questions.append(_build_vocab_question(lesson))
    questions.append(_build_goal_question(lesson))
    questions.append(_build_grammar_question(lesson))

    deduped: list[dict[str, Any]] = []
    seen_questions: set[str] = set()
    for question in questions:
        if question["question"] not in seen_questions:
            deduped.append(question)
            seen_questions.add(question["question"])
    return deduped[:5]


def grade_quiz(questions: list[dict[str, Any]], answers: list[str]) -> dict[str, float]:
    total = len(questions)
    correct = 0
    for question, answer in zip(questions, answers):
        expected = question["answer"].strip().lower()
        if answer.strip().lower() == expected:
            correct += 1

    score = float(correct)
    accuracy = (correct / total * 100) if total else 0.0
    return {"score": score, "accuracy": accuracy, "correct": correct, "total": total}
