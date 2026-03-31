from __future__ import annotations

from typing import Any

LESSON_CONTENT: dict[str, list[dict[str, Any]]] = {
    "Spanish": [
        {
            "title": "Greetings and Introductions",
            "level": "Beginner",
            "focus": "Vocabulary",
            "concept": "Learn simple greetings, introductions, and polite expressions.",
            "examples": [
                "Hola - Hello",
                "Buenos dias - Good morning",
                "Me llamo Ana - My name is Ana",
                "Mucho gusto - Nice to meet you",
            ],
            "grammar_tip": "Spanish nouns have gender, but greetings stay the same for everyone.",
        },
        {
            "title": "Numbers and Everyday Objects",
            "level": "Beginner",
            "focus": "Vocabulary",
            "concept": "Count to ten and name daily items around you.",
            "examples": [
                "Uno, dos, tres - One, two, three",
                "La mesa - The table",
                "El libro - The book",
                "La puerta - The door",
            ],
            "grammar_tip": "Definite articles change with noun gender: el for masculine, la for feminine.",
        },
        {
            "title": "Present Tense Basics",
            "level": "Beginner",
            "focus": "Grammar",
            "concept": "Build simple present tense sentences using regular verbs.",
            "examples": [
                "Yo estudio espanol - I study Spanish",
                "Tu hablas despacio - You speak slowly",
                "Nosotros vivimos aqui - We live here",
            ],
            "grammar_tip": "Verb endings change based on the subject. Watch the ending, not only the verb root.",
        },
    ],
    "French": [
        {
            "title": "Bonjour Basics",
            "level": "Beginner",
            "focus": "Vocabulary",
            "concept": "Start conversations with common French greetings and courtesy phrases.",
            "examples": [
                "Bonjour - Hello",
                "Bonsoir - Good evening",
                "Je m'appelle Louis - My name is Louis",
                "Merci beaucoup - Thank you very much",
            ],
            "grammar_tip": "French pronunciation matters a lot, so read examples aloud while learning.",
        },
        {
            "title": "Family and Daily Life",
            "level": "Beginner",
            "focus": "Vocabulary",
            "concept": "Learn words for family members and daily routines.",
            "examples": [
                "La mere - Mother",
                "Le pere - Father",
                "Je travaille aujourd'hui - I work today",
                "Nous mangeons ensemble - We eat together",
            ],
            "grammar_tip": "Articles change with gender and number: le, la, les.",
        },
        {
            "title": "Simple Sentence Structure",
            "level": "Beginner",
            "focus": "Grammar",
            "concept": "Form short subject-verb-object sentences in French.",
            "examples": [
                "Je lis un livre - I read a book",
                "Tu aimes la musique - You like music",
                "Ils parlent francais - They speak French",
            ],
            "grammar_tip": "French uses many silent letters, but written grammar still follows strict agreement rules.",
        },
    ],
    "German": [
        {
            "title": "Everyday Greetings",
            "level": "Beginner",
            "focus": "Vocabulary",
            "concept": "Use basic greetings, introductions, and polite phrases in German.",
            "examples": [
                "Hallo - Hello",
                "Guten Morgen - Good morning",
                "Ich heisse Max - My name is Max",
                "Freut mich - Nice to meet you",
            ],
            "grammar_tip": "German capitalizes all nouns, so pay attention when reading vocabulary.",
        },
        {
            "title": "Home and School Words",
            "level": "Beginner",
            "focus": "Vocabulary",
            "concept": "Learn useful nouns for home, school, and everyday study.",
            "examples": [
                "Das Buch - The book",
                "Der Tisch - The table",
                "Die Schule - The school",
                "Das Fenster - The window",
            ],
            "grammar_tip": "German articles have three genders: der, die, das.",
        },
        {
            "title": "Verb Position Fundamentals",
            "level": "Beginner",
            "focus": "Grammar",
            "concept": "Understand basic German sentence structure with the verb in second position.",
            "examples": [
                "Ich lerne Deutsch - I learn German",
                "Wir spielen heute - We play today",
                "Er trinkt Wasser - He drinks water",
            ],
            "grammar_tip": "In main clauses, the conjugated verb usually appears in the second position.",
        },
    ],
    "Hindi": [
        {
            "title": "Namaste and Introductions",
            "level": "Beginner",
            "focus": "Vocabulary",
            "concept": "Practice basic Hindi greetings and self-introduction patterns.",
            "examples": [
                "Namaste - Hello",
                "Aap kaise hain - How are you",
                "Mera naam Riya hai - My name is Riya",
                "Dhanyavaad - Thank you",
            ],
            "grammar_tip": "Hindi often uses postpositions after nouns instead of prepositions before them.",
        },
        {
            "title": "Family and Common Nouns",
            "level": "Beginner",
            "focus": "Vocabulary",
            "concept": "Learn common household and family-related words in Hindi.",
            "examples": [
                "Ghar - House",
                "Paani - Water",
                "Maa - Mother",
                "Dost - Friend",
            ],
            "grammar_tip": "Hindi nouns can be masculine or feminine and affect adjective and verb forms.",
        },
        {
            "title": "Simple Present Sentences",
            "level": "Beginner",
            "focus": "Grammar",
            "concept": "Build short present tense sentences for daily activities.",
            "examples": [
                "Main padhta hoon - I study",
                "Woh gaana gaati hai - She sings",
                "Hum khelte hain - We play",
            ],
            "grammar_tip": "Verb endings often change based on gender and number in Hindi.",
        },
    ],
}


def get_languages() -> list[str]:
    return list(LESSON_CONTENT.keys())


def get_lessons(language: str) -> list[dict[str, Any]]:
    return LESSON_CONTENT.get(language, [])


def get_lesson(language: str, lesson_title: str) -> dict[str, Any] | None:
    return next((lesson for lesson in get_lessons(language) if lesson["title"] == lesson_title), None)


def get_recommended_next_step(language: str, completed_lessons: set[str]) -> str:
    for lesson in get_lessons(language):
        if lesson["title"] not in completed_lessons:
            return f"Next best step: complete '{lesson['title']}' in {language}."
    return f"You have completed all current {language} lessons. Use the AI Tutor to deepen fluency."
