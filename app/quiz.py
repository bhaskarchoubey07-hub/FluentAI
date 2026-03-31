from __future__ import annotations

import random
from typing import Any

from app.lessons import get_lesson


QUIZ_BANK: dict[str, dict[str, list[dict[str, Any]]]] = {
    "Spanish": {
        "Greetings and Introductions": [
            {"type": "mcq", "question": "What does 'Hola' mean?", "options": ["Goodbye", "Hello", "Please", "Friend"], "answer": "Hello"},
            {"type": "fill", "question": "Complete the phrase: 'Me ____ Ana.'", "answer": "llamo"},
        ],
        "Numbers and Everyday Objects": [
            {"type": "mcq", "question": "Which word means 'book'?", "options": ["Puerta", "Mesa", "Libro", "Casa"], "answer": "Libro"},
            {"type": "fill", "question": "Translate 'one' into Spanish.", "answer": "uno"},
        ],
        "Present Tense Basics": [
            {"type": "mcq", "question": "Which sentence means 'I study Spanish'?", "options": ["Yo estudio espanol", "Tu hablas espanol", "Nosotros vivimos aqui", "El libro es rojo"], "answer": "Yo estudio espanol"},
            {"type": "fill", "question": "Complete: 'Tu ____ despacio.'", "answer": "hablas"},
        ],
    },
    "French": {
        "Bonjour Basics": [
            {"type": "mcq", "question": "What does 'Bonsoir' mean?", "options": ["Good evening", "Good afternoon", "Thank you", "Please"], "answer": "Good evening"},
            {"type": "fill", "question": "Complete: 'Je m'____ Louis.'", "answer": "appelle"},
        ],
        "Family and Daily Life": [
            {"type": "mcq", "question": "Which word means 'mother'?", "options": ["Le pere", "La mere", "Le frere", "L'ami"], "answer": "La mere"},
            {"type": "fill", "question": "Translate 'father' into French with the article.", "answer": "le pere"},
        ],
        "Simple Sentence Structure": [
            {"type": "mcq", "question": "Which sentence means 'You like music'?", "options": ["Je lis un livre", "Tu aimes la musique", "Ils parlent francais", "Nous sommes ici"], "answer": "Tu aimes la musique"},
            {"type": "fill", "question": "Complete: 'Ils parlent ____.'", "answer": "francais"},
        ],
    },
    "German": {
        "Everyday Greetings": [
            {"type": "mcq", "question": "What does 'Guten Morgen' mean?", "options": ["Good night", "Good afternoon", "Good morning", "See you later"], "answer": "Good morning"},
            {"type": "fill", "question": "Complete: 'Ich ____ Max.'", "answer": "heisse"},
        ],
        "Home and School Words": [
            {"type": "mcq", "question": "Which article can go with 'Buch'?", "options": ["Die", "Das", "Der", "Den"], "answer": "Das"},
            {"type": "fill", "question": "Translate 'window' into German with its article.", "answer": "das fenster"},
        ],
        "Verb Position Fundamentals": [
            {"type": "mcq", "question": "Which sentence correctly places the verb second?", "options": ["Ich Deutsch lerne", "Deutsch ich lerne", "Ich lerne Deutsch", "Lerne ich Deutsch"], "answer": "Ich lerne Deutsch"},
            {"type": "fill", "question": "Complete: 'Er ____ Wasser.'", "answer": "trinkt"},
        ],
    },
    "Hindi": {
        "Namaste and Introductions": [
            {"type": "mcq", "question": "What does 'Dhanyavaad' mean?", "options": ["Please", "Thank you", "Hello", "Goodbye"], "answer": "Thank you"},
            {"type": "fill", "question": "Complete: 'Mera ____ Riya hai.'", "answer": "naam"},
        ],
        "Family and Common Nouns": [
            {"type": "mcq", "question": "Which word means 'water'?", "options": ["Ghar", "Dost", "Maa", "Paani"], "answer": "Paani"},
            {"type": "fill", "question": "Translate 'friend' into Hindi.", "answer": "dost"},
        ],
        "Simple Present Sentences": [
            {"type": "mcq", "question": "Which sentence means 'We play'?", "options": ["Main padhta hoon", "Hum khelte hain", "Woh gaana gaati hai", "Aap kaise hain"], "answer": "Hum khelte hain"},
            {"type": "fill", "question": "Complete: 'Woh gaana ____ hai.'", "answer": "gaati"},
        ],
    },
}


def build_quiz(language: str, lesson_title: str) -> list[dict[str, Any]]:
    questions = QUIZ_BANK.get(language, {}).get(lesson_title, [])
    return questions or build_fallback_quiz(language, lesson_title)


def build_fallback_quiz(language: str, lesson_title: str) -> list[dict[str, Any]]:
    lesson = get_lesson(language, lesson_title)
    if not lesson:
        return []

    examples = lesson["examples"]
    random_example = random.choice(examples)
    term, meaning = [part.strip() for part in random_example.split(" - ", maxsplit=1)]
    options = [meaning, "Please", "Tomorrow", "Teacher"]
    random.shuffle(options)
    return [
        {"type": "mcq", "question": f"What does '{term}' mean?", "options": options, "answer": meaning},
        {"type": "fill", "question": f"Type the first word in this phrase: '{term}'", "answer": term.split()[0].lower()},
    ]


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
