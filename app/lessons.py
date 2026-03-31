from __future__ import annotations

from typing import Any


LEVEL_ORDER = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}


TOPIC_SEQUENCE = [
    ("Introductions", "meeting people and introducing yourself"),
    ("Home and Family", "daily life at home and family relationships"),
    ("Food and Dining", "ordering food, talking about meals, and expressing tastes"),
    ("Numbers and Money", "counting, prices, budgets, and shopping"),
    ("Travel and Transport", "stations, tickets, destinations, and movement"),
    ("Directions and Places", "asking where things are and following directions"),
    ("Daily Routine", "morning to night routines and time expressions"),
    ("Work and Study", "learning, tasks, schedules, and goals"),
    ("Health and Wellbeing", "basic symptoms, rest, and common needs"),
    ("Shopping and Services", "buying things and asking for help in stores"),
    ("Past Experiences", "describing what happened yesterday or recently"),
    ("Plans and Invitations", "making future plans and inviting people"),
    ("Opinions and Preferences", "sharing ideas, comparing options, and reacting"),
]


LANGUAGE_BANK: dict[str, list[dict[str, Any]]] = {
    "Spanish": [
        {"topic": "Introductions", "vocab": ["hola", "me llamo", "mucho gusto", "como estas", "gracias"], "examples": ["Hola, me llamo Lucia - Hello, my name is Lucia", "Mucho gusto - Nice to meet you", "Como estas hoy - How are you today", "Gracias por venir - Thank you for coming"], "tip": "Spanish introductions often switch between formal and informal address."},
        {"topic": "Home and Family", "vocab": ["casa", "familia", "madre", "padre", "hermano"], "examples": ["Mi casa es pequena - My house is small", "Tengo una familia grande - I have a big family", "Mi madre cocina bien - My mother cooks well", "Mi hermano estudia mucho - My brother studies a lot"], "tip": "Possessive words like mi and tu are common when talking about family."},
        {"topic": "Food and Dining", "vocab": ["quiero", "agua", "cafe", "pan", "la cuenta"], "examples": ["Quiero un cafe - I want a coffee", "La sopa esta caliente - The soup is hot", "La cuenta, por favor - The bill, please", "Me gusta este pan - I like this bread"], "tip": "Quiero is direct; me gustaria sounds softer in restaurants."},
        {"topic": "Numbers and Money", "vocab": ["uno", "diez", "precio", "dinero", "barato"], "examples": ["Cuesta diez euros - It costs ten euros", "No tengo mucho dinero - I do not have much money", "Es muy barato - It is very cheap", "Necesito dos boletos - I need two tickets"], "tip": "Numbers often appear with nouns, so practice both together."},
        {"topic": "Travel and Transport", "vocab": ["estacion", "tren", "boleto", "viajar", "aeropuerto"], "examples": ["La estacion esta cerca - The station is nearby", "Necesito un boleto de tren - I need a train ticket", "Vamos al aeropuerto - We are going to the airport", "Quiero viajar manana - I want to travel tomorrow"], "tip": "Travel phrases often use ir, venir, and querer."},
        {"topic": "Directions and Places", "vocab": ["donde", "recto", "izquierda", "derecha", "cerca"], "examples": ["Donde esta el museo - Where is the museum", "Siga recto - Go straight", "Gire a la izquierda - Turn left", "El banco esta cerca - The bank is near"], "tip": "Question words like donde often begin simple location questions."},
        {"topic": "Daily Routine", "vocab": ["me levanto", "desayuno", "trabajo", "estudio", "duermo"], "examples": ["Me levanto temprano - I get up early", "Desayuno a las siete - I eat breakfast at seven", "Trabajo por la tarde - I work in the afternoon", "Duermo tarde - I sleep late"], "tip": "Reflexive verbs appear often when talking about routine."},
        {"topic": "Work and Study", "vocab": ["estudiar", "clase", "tarea", "oficina", "reunion"], "examples": ["Tengo clase hoy - I have class today", "La tarea es dificil - The homework is difficult", "Trabajo en una oficina - I work in an office", "Tenemos una reunion manana - We have a meeting tomorrow"], "tip": "The present tense is enough for many everyday work and study statements."},
        {"topic": "Health and Wellbeing", "vocab": ["dolor", "cansado", "agua", "descansar", "medico"], "examples": ["Tengo dolor de cabeza - I have a headache", "Estoy cansado hoy - I am tired today", "Necesito descansar - I need to rest", "Voy al medico manana - I am going to the doctor tomorrow"], "tip": "Tengo and estoy are both useful but describe different kinds of states."},
        {"topic": "Shopping and Services", "vocab": ["tienda", "camisa", "ayuda", "talla", "comprar"], "examples": ["Busco una camisa azul - I am looking for a blue shirt", "Necesito otra talla - I need another size", "Puede ayudarme - Can you help me", "Quiero comprar esto - I want to buy this"], "tip": "Service interactions often use polite questions and direct object words like esto."},
        {"topic": "Past Experiences", "vocab": ["ayer", "visite", "comi", "estudie", "fue"], "examples": ["Ayer visite a mi amiga - Yesterday I visited my friend", "Comi temprano - I ate early", "Estudie por la noche - I studied at night", "Fue un buen dia - It was a good day"], "tip": "Time markers make past tense easier to understand in conversation."},
        {"topic": "Plans and Invitations", "vocab": ["venir", "manana", "podemos", "a las seis", "no puedo"], "examples": ["Quieres venir conmigo - Do you want to come with me", "Podemos vernos manana - We can meet tomorrow", "Nos vemos a las seis - We will see each other at six", "Lo siento, no puedo - Sorry, I cannot"], "tip": "The present tense often expresses near-future plans in Spanish."},
        {"topic": "Opinions and Preferences", "vocab": ["creo que", "prefiero", "me gusta", "mejor", "no estoy de acuerdo"], "examples": ["Creo que es util - I think it is useful", "Prefiero esta opcion - I prefer this option", "Me gusta aprender asi - I like learning this way", "No estoy de acuerdo - I do not agree"], "tip": "Opinion starters help you sound more natural and organized."},
    ],
    "French": [
        {"topic": "Introductions", "vocab": ["bonjour", "je m'appelle", "merci", "comment ca va", "enchante"], "examples": ["Bonjour, je m'appelle Claire - Hello, my name is Claire", "Enchante de vous rencontrer - Nice to meet you", "Comment ca va aujourd'hui - How are you today", "Merci pour votre aide - Thank you for your help"], "tip": "French greetings shift with formality and time of day."},
        {"topic": "Home and Family", "vocab": ["maison", "famille", "mere", "pere", "frere"], "examples": ["Ma maison est calme - My house is quiet", "J'ai une grande famille - I have a big family", "Ma mere travaille ici - My mother works here", "Mon frere etudie le soir - My brother studies in the evening"], "tip": "French articles and possessives change with gender and number."},
        {"topic": "Food and Dining", "vocab": ["je veux", "eau", "cafe", "pain", "l'addition"], "examples": ["Je veux un cafe - I want a coffee", "L'addition, s'il vous plait - The bill, please", "Le pain est frais - The bread is fresh", "J'aime cette soupe - I like this soup"], "tip": "Use polite set phrases often in cafes and restaurants."},
        {"topic": "Numbers and Money", "vocab": ["un", "dix", "prix", "argent", "cher"], "examples": ["Ca coute dix euros - It costs ten euros", "Je n'ai pas beaucoup d'argent - I do not have much money", "C'est trop cher - It is too expensive", "J'ai besoin de deux billets - I need two tickets"], "tip": "French number pronunciation needs practice even when the written forms look simple."},
        {"topic": "Travel and Transport", "vocab": ["gare", "train", "billet", "voyager", "aeroport"], "examples": ["La gare est loin - The station is far", "Je cherche un billet de train - I am looking for a train ticket", "Nous allons a l'aeroport - We are going to the airport", "Je voyage demain - I travel tomorrow"], "tip": "Movement verbs like aller appear constantly in travel situations."},
        {"topic": "Directions and Places", "vocab": ["ou", "tout droit", "gauche", "droite", "pres"], "examples": ["Ou est le musee - Where is the museum", "Allez tout droit - Go straight", "Tournez a gauche - Turn left", "La banque est pres d'ici - The bank is near here"], "tip": "Short direction commands are common in spoken French."},
        {"topic": "Daily Routine", "vocab": ["je me leve", "petit-dejeuner", "travaille", "etudie", "dors"], "examples": ["Je me leve tot - I get up early", "Je prends le petit-dejeuner a sept heures - I have breakfast at seven", "Je travaille l'apres-midi - I work in the afternoon", "Je dors tard - I sleep late"], "tip": "Reflexive forms are common when describing a daily routine."},
        {"topic": "Work and Study", "vocab": ["etudier", "cours", "devoirs", "bureau", "reunion"], "examples": ["J'ai un cours aujourd'hui - I have a class today", "Les devoirs sont difficiles - The homework is difficult", "Je travaille dans un bureau - I work in an office", "Nous avons une reunion demain - We have a meeting tomorrow"], "tip": "Present-tense patterns cover many basic work and study situations."},
        {"topic": "Health and Wellbeing", "vocab": ["douleur", "fatigue", "eau", "repos", "medecin"], "examples": ["J'ai mal a la tete - I have a headache", "Je suis fatigue aujourd'hui - I am tired today", "J'ai besoin de repos - I need rest", "Je vais chez le medecin demain - I am going to the doctor tomorrow"], "tip": "French often uses fixed expressions for discomfort rather than direct word-for-word translations."},
        {"topic": "Shopping and Services", "vocab": ["magasin", "chemise", "aide", "taille", "acheter"], "examples": ["Je cherche une chemise bleue - I am looking for a blue shirt", "J'ai besoin d'une autre taille - I need another size", "Pouvez-vous m'aider - Can you help me", "Je veux acheter ceci - I want to buy this"], "tip": "Polite service language often uses pouvez-vous and je cherche."},
        {"topic": "Past Experiences", "vocab": ["hier", "j'ai visite", "j'ai mange", "j'ai etudie", "c'etait"], "examples": ["Hier, j'ai visite Paris - Yesterday I visited Paris", "J'ai mange tot - I ate early", "J'ai etudie le soir - I studied in the evening", "C'etait une bonne journee - It was a good day"], "tip": "Passe compose is the main conversational past tense for many everyday stories."},
        {"topic": "Plans and Invitations", "vocab": ["venir", "demain", "on peut", "a six heures", "je ne peux pas"], "examples": ["Tu veux venir avec nous - Do you want to come with us", "On peut se retrouver demain - We can meet tomorrow", "Je suis libre a six heures - I am free at six o'clock", "Desole, je ne peux pas - Sorry, I cannot"], "tip": "French often uses present forms to express future plans in speech."},
        {"topic": "Opinions and Preferences", "vocab": ["je pense que", "je prefere", "j'aime", "mieux", "je ne suis pas d'accord"], "examples": ["Je pense que c'est utile - I think it is useful", "Je prefere cette option - I prefer this option", "J'aime apprendre comme ca - I like learning like this", "Je ne suis pas d'accord - I do not agree"], "tip": "Opinion phrases like a mon avis help you speak more fluently and clearly."},
    ],
    "German": [
        {"topic": "Introductions", "vocab": ["hallo", "ich heisse", "danke", "wie geht es Ihnen", "freut mich"], "examples": ["Hallo, ich heisse Nina - Hello, my name is Nina", "Freut mich, Sie kennenzulernen - Nice to meet you", "Wie geht es Ihnen heute - How are you today", "Danke fuer Ihre Hilfe - Thank you for your help"], "tip": "German changes tone significantly between formal and informal situations."},
        {"topic": "Home and Family", "vocab": ["Haus", "Familie", "Mutter", "Vater", "Bruder"], "examples": ["Mein Haus ist ruhig - My house is quiet", "Ich habe eine grosse Familie - I have a big family", "Meine Mutter arbeitet hier - My mother works here", "Mein Bruder lernt am Abend - My brother studies in the evening"], "tip": "Remember articles and capitalization when learning German family vocabulary."},
        {"topic": "Food and Dining", "vocab": ["ich moechte", "Wasser", "Kaffee", "Brot", "die Rechnung"], "examples": ["Ich moechte einen Kaffee - I would like a coffee", "Die Rechnung, bitte - The bill, please", "Das Brot ist frisch - The bread is fresh", "Ich mag diese Suppe - I like this soup"], "tip": "Ich moechte is one of the most useful polite dining phrases in German."},
        {"topic": "Numbers and Money", "vocab": ["eins", "zehn", "Preis", "Geld", "billig"], "examples": ["Es kostet zehn Euro - It costs ten euros", "Ich habe nicht viel Geld - I do not have much money", "Das ist sehr billig - That is very cheap", "Ich brauche zwei Tickets - I need two tickets"], "tip": "German numbers are simple at first, but prices and compound numbers need repetition."},
        {"topic": "Travel and Transport", "vocab": ["Bahnhof", "Zug", "Ticket", "reisen", "Flughafen"], "examples": ["Der Bahnhof ist nah - The station is near", "Ich brauche ein Zugticket - I need a train ticket", "Wir fahren zum Flughafen - We are going to the airport", "Ich reise morgen - I travel tomorrow"], "tip": "Travel phrases often combine movement verbs with destination prepositions."},
        {"topic": "Directions and Places", "vocab": ["wo", "geradeaus", "links", "rechts", "in der Naehe"], "examples": ["Wo ist das Museum - Where is the museum", "Gehen Sie geradeaus - Go straight", "Biegen Sie links ab - Turn left", "Die Bank ist in der Naehe - The bank is nearby"], "tip": "Commands for directions usually keep the verb first."},
        {"topic": "Daily Routine", "vocab": ["ich stehe auf", "fruehstuecke", "arbeite", "lerne", "schlafe"], "examples": ["Ich stehe frueh auf - I get up early", "Ich fruehstuecke um sieben Uhr - I have breakfast at seven", "Ich arbeite am Nachmittag - I work in the afternoon", "Ich schlafe spaet - I sleep late"], "tip": "Separable verbs are common in routine language and change position in the sentence."},
        {"topic": "Work and Study", "vocab": ["lernen", "Kurs", "Hausaufgaben", "Buero", "Besprechung"], "examples": ["Ich habe heute einen Kurs - I have a class today", "Die Hausaufgaben sind schwer - The homework is hard", "Ich arbeite in einem Buero - I work in an office", "Wir haben morgen eine Besprechung - We have a meeting tomorrow"], "tip": "German sentence structure stays consistent even when you add time words."},
        {"topic": "Health and Wellbeing", "vocab": ["Schmerz", "muede", "Wasser", "ausruhen", "Arzt"], "examples": ["Ich habe Kopfschmerzen - I have a headache", "Ich bin heute muede - I am tired today", "Ich muss mich ausruhen - I need to rest", "Ich gehe morgen zum Arzt - I am going to the doctor tomorrow"], "tip": "Modal verbs and fixed expressions help you speak naturally about health."},
        {"topic": "Shopping and Services", "vocab": ["Geschaeft", "Hemd", "Hilfe", "Groesse", "kaufen"], "examples": ["Ich suche ein blaues Hemd - I am looking for a blue shirt", "Ich brauche eine andere Groesse - I need another size", "Koennen Sie mir helfen - Can you help me", "Ich moechte das kaufen - I want to buy that"], "tip": "Service interactions in German rely heavily on polite modal constructions."},
        {"topic": "Past Experiences", "vocab": ["gestern", "ich habe besucht", "ich habe gegessen", "ich habe gelernt", "es war"], "examples": ["Gestern habe ich meine Freundin besucht - Yesterday I visited my friend", "Ich habe frueh gegessen - I ate early", "Ich habe am Abend gelernt - I studied in the evening", "Es war ein guter Tag - It was a good day"], "tip": "The spoken past in German often uses haben plus a participle."},
        {"topic": "Plans and Invitations", "vocab": ["kommen", "morgen", "wir koennen", "um sechs", "ich kann nicht"], "examples": ["Willst du mitkommen - Do you want to come along", "Wir koennen uns morgen treffen - We can meet tomorrow", "Wir treffen uns um sechs - We meet at six", "Leider kann ich nicht - Unfortunately I cannot"], "tip": "Time expressions usually sit in the middle of the clause while the verb stays in second position."},
        {"topic": "Opinions and Preferences", "vocab": ["ich denke", "ich bevorzuge", "ich mag", "besser", "ich bin nicht einverstanden"], "examples": ["Ich denke, das ist sinnvoll - I think that is sensible", "Ich bevorzuge diese Option - I prefer this option", "Ich mag diese Lernmethode - I like this learning method", "Ich bin nicht einverstanden - I do not agree"], "tip": "German opinion phrases often connect to a second clause for explanation."},
    ],
    "Hindi": [
        {"topic": "Introductions", "vocab": ["namaste", "mera naam", "dhanyavaad", "aap kaise hain", "milkar khushi hui"], "examples": ["Namaste, mera naam Riya hai - Hello, my name is Riya", "Aapse milkar khushi hui - Nice to meet you", "Aap kaise hain aaj - How are you today", "Dhanyavaad aapki madad ke liye - Thank you for your help"], "tip": "Hindi introductions change tone depending on respect and familiarity."},
        {"topic": "Home and Family", "vocab": ["ghar", "parivar", "maa", "pitaji", "bhai"], "examples": ["Mera ghar shaant hai - My house is quiet", "Mera parivar bada hai - My family is big", "Meri maa yahan kaam karti hain - My mother works here", "Mera bhai shaam ko padhta hai - My brother studies in the evening"], "tip": "Possession and respect markers matter a lot in family sentences."},
        {"topic": "Food and Dining", "vocab": ["mujhe chahiye", "paani", "chai", "roti", "bill"], "examples": ["Mujhe ek chai chahiye - I want one tea", "Bill dijiye, kripya - Please give the bill", "Yeh roti garam hai - This bread is warm", "Mujhe yeh sabzi pasand hai - I like this vegetable dish"], "tip": "Chahiye is very useful for asking for things politely."},
        {"topic": "Numbers and Money", "vocab": ["ek", "das", "daam", "paise", "sasta"], "examples": ["Iska daam das rupaye hai - Its price is ten rupees", "Mere paas zyada paise nahin hain - I do not have much money", "Yeh bahut sasta hai - This is very cheap", "Mujhe do ticket chahiye - I need two tickets"], "tip": "Hindi quantity phrases often place the number directly before the noun."},
        {"topic": "Travel and Transport", "vocab": ["station", "train", "ticket", "safar", "havai adda"], "examples": ["Station paas mein hai - The station is nearby", "Mujhe train ka ticket chahiye - I need a train ticket", "Hum havai adde ja rahe hain - We are going to the airport", "Main kal safar karunga - I will travel tomorrow"], "tip": "Travel language often mixes borrowed nouns with common Hindi verbs."},
        {"topic": "Directions and Places", "vocab": ["kahan", "seedha", "baayen", "daayen", "paas"], "examples": ["Museum kahan hai - Where is the museum", "Seedha jaiye - Go straight", "Baayen mudiyega - Turn left", "Bank paas mein hai - The bank is nearby"], "tip": "Polite command forms like jaiye are helpful in public interactions."},
        {"topic": "Daily Routine", "vocab": ["uthna", "nashta", "kaam", "padhna", "sona"], "examples": ["Main jaldi uthta hoon - I get up early", "Main saat baje nashta karta hoon - I have breakfast at seven", "Main dopahar mein kaam karta hoon - I work in the afternoon", "Main der se sota hoon - I sleep late"], "tip": "Daily routine sentences often show gender through the verb ending."},
        {"topic": "Work and Study", "vocab": ["padhna", "class", "ghar ka kaam", "daftar", "meeting"], "examples": ["Meri aaj class hai - I have class today", "Ghar ka kaam mushkil hai - The homework is difficult", "Main daftar mein kaam karta hoon - I work in an office", "Hamari kal meeting hai - We have a meeting tomorrow"], "tip": "Hindi handles many work words with English borrowings plus Hindi grammar."},
        {"topic": "Health and Wellbeing", "vocab": ["dard", "thaka", "paani", "aaraam", "doctor"], "examples": ["Mere sir mein dard hai - I have a headache", "Main aaj thaka hua hoon - I am tired today", "Mujhe aaraam chahiye - I need rest", "Main kal doctor ke paas jaunga - I will go to the doctor tomorrow"], "tip": "Hindi often uses hai constructions to describe physical states."},
        {"topic": "Shopping and Services", "vocab": ["dukaan", "kameez", "madad", "size", "kharidna"], "examples": ["Main neeli kameez dhoondh raha hoon - I am looking for a blue shirt", "Mujhe doosra size chahiye - I need another size", "Kya aap meri madad kar sakte hain - Can you help me", "Main yeh kharidna chahta hoon - I want to buy this"], "tip": "Hindi service interactions often rely on polite question endings."},
        {"topic": "Past Experiences", "vocab": ["kal", "gaya tha", "khaya", "padha", "achha tha"], "examples": ["Kal main apni dost se mila tha - Yesterday I met my friend", "Maine jaldi khana khaya - I ate early", "Maine shaam ko padha - I studied in the evening", "Kal ka din achha tha - Yesterday was a good day"], "tip": "Past tense in Hindi changes with gender and sentence structure, so repetition helps."},
        {"topic": "Plans and Invitations", "vocab": ["aana", "kal", "hum mil sakte hain", "chhe baje", "main nahin aa sakta"], "examples": ["Kya tum mere saath aaoge - Will you come with me", "Hum kal mil sakte hain - We can meet tomorrow", "Hum chhe baje milenge - We will meet at six", "Maaf kijiye, main nahin aa sakta - Sorry, I cannot come"], "tip": "Hindi invitations often sound warmer when framed as suggestions."},
        {"topic": "Opinions and Preferences", "vocab": ["mujhe lagta hai", "main pasand karta hoon", "mujhe achha lagta hai", "behtar", "main sehmat nahin hoon"], "examples": ["Mujhe lagta hai ki yeh upyogi hai - I think this is useful", "Main is vikalp ko pasand karta hoon - I prefer this option", "Mujhe yeh tareeka achha lagta hai - I like this method", "Main sehmat nahin hoon - I do not agree"], "tip": "Opinion phrases help Hindi learners move beyond short yes or no answers."},
    ],
}


def _lesson(
    title: str,
    level: str,
    focus: str,
    concept: str,
    examples: list[str],
    grammar_tip: str,
    vocabulary: list[str],
    learning_goals: list[str],
    practice_prompt: str,
    minutes: int,
) -> dict[str, Any]:
    return {
        "title": title,
        "level": level,
        "focus": focus,
        "concept": concept,
        "examples": examples,
        "grammar_tip": grammar_tip,
        "vocabulary": vocabulary,
        "learning_goals": learning_goals,
        "practice_prompt": practice_prompt,
        "minutes": minutes,
    }


def _build_course(language: str, topic_items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    lessons: list[dict[str, Any]] = []
    for index, item in enumerate(topic_items):
        topic = item["topic"]
        context = next(description for name, description in TOPIC_SEQUENCE if name == topic)
        vocab = item["vocab"]
        examples = item["examples"]
        base_minutes = 8 + (index % 4)
        lessons.extend(
            [
                _lesson(
                    f"{topic}: Key Vocabulary",
                    "Beginner",
                    "Vocabulary",
                    f"Build core vocabulary for {context} in {language}.",
                    examples[:4],
                    item["tip"],
                    vocab,
                    [f"Recognize essential words for {topic.lower()}", "Read and repeat common short phrases", "Connect target-language words to practical situations"],
                    f"Use at least three of these words in a short {language} practice line about {topic.lower()}.",
                    base_minutes,
                ),
                _lesson(
                    f"{topic}: Core Sentence Patterns",
                    "Beginner" if index < 6 else "Intermediate",
                    "Grammar",
                    f"Practice sentence building for {context} with useful patterns and word order.",
                    examples[:3] + [f"{vocab[0]} y {vocab[1]} - A pattern using two key words"],
                    f"{item['tip']} Focus on sentence shape and repetition while practicing.",
                    vocab,
                    [f"Build short sentences about {topic.lower()}", "Notice recurring grammar patterns", "Use high-frequency structures with confidence"],
                    f"Write two simple {language} sentences related to {topic.lower()} using the lesson vocabulary.",
                    base_minutes + 1,
                ),
                _lesson(
                    f"{topic}: Guided Conversation",
                    "Intermediate",
                    "Conversation",
                    f"Use practical phrases for guided conversation about {context}.",
                    examples,
                    f"{item['tip']} In conversation, keep your response clear before making it longer.",
                    vocab,
                    [f"Ask and answer simple questions about {topic.lower()}", "Respond naturally in short dialogue", "Reuse useful chunks without translating word by word"],
                    f"Role-play a short conversation about {topic.lower()} in {language}.",
                    base_minutes + 2,
                ),
                _lesson(
                    f"{topic}: Fluency Expansion",
                    "Advanced",
                    "Conversation",
                    f"Expand from short answers to fuller explanations about {context}.",
                    examples[1:4] + [examples[0]],
                    f"{item['tip']} Add reasons, comparisons, or personal details to sound more fluent.",
                    vocab,
                    [f"Give longer opinions about {topic.lower()}", "Combine phrases into fuller responses", "Sound more natural and confident in discussion"],
                    f"Speak or write for 30-45 seconds in {language} about {topic.lower()}, adding one opinion or reason.",
                    base_minutes + 4,
                ),
            ]
        )
    return lessons


LESSON_CONTENT: dict[str, list[dict[str, Any]]] = {
    language: _build_course(language, topic_items) for language, topic_items in LANGUAGE_BANK.items()
}


def get_languages() -> list[str]:
    return list(LESSON_CONTENT.keys())


def get_lessons(language: str) -> list[dict[str, Any]]:
    return LESSON_CONTENT.get(language, [])


def get_lesson(language: str, lesson_title: str) -> dict[str, Any] | None:
    return next((lesson for lesson in get_lessons(language) if lesson["title"] == lesson_title), None)


def get_lesson_catalog_summary(language: str) -> dict[str, Any]:
    lessons = get_lessons(language)
    by_level: dict[str, int] = {}
    by_focus: dict[str, int] = {}

    for lesson in lessons:
        by_level[lesson["level"]] = by_level.get(lesson["level"], 0) + 1
        by_focus[lesson["focus"]] = by_focus.get(lesson["focus"], 0) + 1

    return {
        "count": len(lessons),
        "levels": by_level,
        "focus_areas": by_focus,
        "minutes": sum(lesson["minutes"] for lesson in lessons),
    }


def get_recommended_next_step(language: str, completed_lessons: set[str]) -> str:
    for lesson in get_lessons(language):
        if lesson["title"] not in completed_lessons:
            return f"Next best step: complete '{lesson['title']}' in {language}."
    return f"You have completed all current {language} lessons. Use the AI Tutor to deepen fluency."
