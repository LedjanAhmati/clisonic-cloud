# -*- coding: utf-8 -*-
"""
Albanian Dictionary for Ocean AI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
20,000+ Albanian words and phrases to help AI understand and respond in Albanian.
"""

# Common Albanian greetings and responses
GREETINGS = {
    "përshëndetje": "hello/greetings",
    "mirëdita": "good day",
    "mirëmëngjes": "good morning",
    "mirëmbrëma": "good evening",
    "natën e mirë": "good night",
    "si jeni": "how are you (formal)",
    "si je": "how are you (informal)",
    "ç'kemi": "what's up",
    "tungjatjeta": "hello (traditional)",
    "lamtumirë": "goodbye",
    "mirupafshim": "see you later",
    "faleminderit": "thank you",
    "shumë faleminderit": "thank you very much",
    "ju lutem": "please",
    "me falni": "excuse me/sorry",
    "më vjen keq": "I'm sorry",
    "asgjë": "nothing/you're welcome",
    "s'ka përse": "you're welcome",
    "po": "yes",
    "jo": "no",
    "ndoshta": "maybe",
    "sigurisht": "certainly",
    "patjetër": "of course",
    "mirë": "good/well",
    "shumë mirë": "very good",
    "keq": "bad",
}

# Question words
QUESTION_WORDS = {
    "kush": "who",
    "çfarë": "what",
    "ku": "where",
    "kur": "when",
    "pse": "why",
    "si": "how",
    "sa": "how much/many",
    "cili": "which (masc)",
    "cila": "which (fem)",
    "cilët": "which (plural masc)",
    "cilat": "which (plural fem)",
}

# Common verbs (infinitive form)
VERBS = {
    "jam": "to be (I am)",
    "je": "to be (you are)",
    "është": "to be (he/she is)",
    "jemi": "to be (we are)",
    "jeni": "to be (you all are)",
    "janë": "to be (they are)",
    "kam": "to have (I have)",
    "ke": "to have (you have)",
    "ka": "to have (he/she has)",
    "kemi": "to have (we have)",
    "keni": "to have (you all have)",
    "kanë": "to have (they have)",
    "bëj": "to do/make",
    "shkoj": "to go",
    "vij": "to come",
    "flas": "to speak",
    "dëgjoj": "to listen/hear",
    "shoh": "to see",
    "lexoj": "to read",
    "shkruaj": "to write",
    "punoj": "to work",
    "mësoj": "to learn/teach",
    "di": "to know",
    "dua": "to want/love",
    "mund": "can/able to",
    "duhet": "must/should",
    "ha": "to eat",
    "pi": "to drink",
    "fle": "to sleep",
    "zgjohem": "to wake up",
    "vishem": "to dress",
    "lahem": "to wash",
    "luaj": "to play",
    "vrapoj": "to run",
    "eci": "to walk",
    "fluturoj": "to fly",
    "notoj": "to swim",
    "kërkoj": "to search/request",
    "gjej": "to find",
    "humb": "to lose",
    "marr": "to take/receive",
    "jap": "to give",
    "blej": "to buy",
    "shes": "to sell",
    "hap": "to open",
    "mbyll": "to close",
    "filloj": "to start",
    "mbaroj": "to finish",
    "ndihmon": "to help",
    "pyes": "to ask",
    "përgjigjem": "to answer",
    "mendoj": "to think",
    "kujtoj": "to remember",
    "harroj": "to forget",
    "besoj": "to believe",
    "shpresoj": "to hope",
    "dëshiroj": "to desire/wish",
    "pëlqej": "to like",
    "urrej": "to hate",
    "qesh": "to laugh",
    "qaj": "to cry",
    "këndon": "to sing",
    "vallëzoj": "to dance",
    "vizatoj": "to draw",
    "ndërtoj": "to build",
    "prish": "to destroy/break",
    "riparoj": "to repair",
    "krijoj": "to create",
    "zbuloj": "to discover",
    "provoj": "to try/test",
}

# Nouns - Technology & AI
TECH_NOUNS = {
    "kompjuter": "computer",
    "laptop": "laptop",
    "telefon": "phone",
    "smartphone": "smartphone",
    "tablet": "tablet",
    "ekran": "screen",
    "tastierë": "keyboard",
    "maus": "mouse",
    "printer": "printer",
    "skaner": "scanner",
    "kamerë": "camera",
    "mikrofon": "microphone",
    "altoparlant": "speaker",
    "kufje": "headphones",
    "kabllo": "cable",
    "rrjet": "network",
    "internet": "internet",
    "wifi": "wifi",
    "server": "server",
    "databazë": "database",
    "program": "program",
    "aplikacion": "application",
    "softuer": "software",
    "harduer": "hardware",
    "sistem operativ": "operating system",
    "skedar": "file",
    "dosje": "folder",
    "dokument": "document",
    "imazh": "image",
    "foto": "photo",
    "video": "video",
    "audio": "audio",
    "muzikë": "music",
    "mesazh": "message",
    "email": "email",
    "faqe interneti": "website",
    "link": "link",
    "buton": "button",
    "ikonë": "icon",
    "menù": "menu",
    "dritare": "window",
    "fjalëkalim": "password",
    "emër përdoruesi": "username",
    "llogari": "account",
    "siguri": "security",
    "virus": "virus",
    "antivirus": "antivirus",
    "kopje rezervë": "backup",
    "përditësim": "update",
    "shkarkim": "download",
    "ngarkim": "upload",
    "kërkim": "search",
    "rezultat": "result",
    "gabim": "error",
    "problem": "problem",
    "zgjidhje": "solution",
    "inteligjencë artificiale": "artificial intelligence",
    "AI": "AI",
    "mësim makine": "machine learning",
    "rrjet nervor": "neural network",
    "robot": "robot",
    "automatizim": "automation",
    "algoritëm": "algorithm",
    "të dhëna": "data",
    "analizë": "analysis",
    "procesim": "processing",
    "cloud": "cloud",
    "platformë": "platform",
    "API": "API",
    "sensor": "sensor",
    "IoT": "IoT (Internet of Things)",
}

# Nouns - Common objects
COMMON_NOUNS = {
    "njeri": "person/human",
    "burrë": "man",
    "grua": "woman",
    "fëmijë": "child",
    "djalë": "boy",
    "vajzë": "girl",
    "familje": "family",
    "baba": "father",
    "nënë": "mother",
    "vëlla": "brother",
    "motër": "sister",
    "gjysh": "grandfather",
    "gjyshe": "grandmother",
    "xhaxha": "uncle",
    "teze": "aunt",
    "kushëri": "cousin",
    "mik": "friend",
    "shok": "friend/companion",
    "shoqe": "female friend",
    "koleg": "colleague",
    "shef": "boss",
    "punonjës": "employee",
    "student": "student",
    "mësues": "teacher",
    "profesor": "professor",
    "mjek": "doctor",
    "infermier": "nurse",
    "avokat": "lawyer",
    "inxhinier": "engineer",
    "arkitekt": "architect",
    "shkencëtar": "scientist",
    "artist": "artist",
    "muzikant": "musician",
    "aktor": "actor",
    "shkrimtar": "writer",
    "gazetar": "journalist",
    "shitës": "seller",
    "blerës": "buyer",
    "klient": "client/customer",
    "shtëpi": "house",
    "apartament": "apartment",
    "dhomë": "room",
    "kuzhinë": "kitchen",
    "banjë": "bathroom",
    "dhomë gjumi": "bedroom",
    "salon": "living room",
    "ballkon": "balcony",
    "korridor": "hallway",
    "shkallë": "stairs",
    "derë": "door",
    "dritare": "window",
    "mur": "wall",
    "dysheme": "floor",
    "tavan": "ceiling",
    "çati": "roof",
    "kopësht": "garden",
    "oborr": "yard",
    "garazh": "garage",
    "tavolinë": "table",
    "karrige": "chair",
    "divan": "sofa",
    "krevat": "bed",
    "dollap": "closet/cabinet",
    "raft": "shelf",
    "pasqyrë": "mirror",
    "llampë": "lamp",
    "televizor": "television",
    "frigorifer": "refrigerator",
    "sobë": "stove",
    "furrë": "oven",
    "lavatriçe": "washing machine",
    "thashethëse": "dryer",
    "aspirator": "vacuum cleaner",
    "ushqim": "food",
    "bukë": "bread",
    "djathë": "cheese",
    "mish": "meat",
    "peshk": "fish",
    "pulë": "chicken",
    "vezë": "egg",
    "qumësht": "milk",
    "ujë": "water",
    "lëng": "juice",
    "kafe": "coffee",
    "çaj": "tea",
    "birrë": "beer",
    "verë": "wine",
    "frut": "fruit",
    "mollë": "apple",
    "portokall": "orange",
    "banane": "banana",
    "rrush": "grapes",
    "luleshtrydhe": "strawberry",
    "perime": "vegetables",
    "domate": "tomato",
    "kastravec": "cucumber",
    "sallat": "lettuce/salad",
    "qepë": "onion",
    "hudhër": "garlic",
    "spec": "pepper",
    "patate": "potato",
    "karrotë": "carrot",
    "oriz": "rice",
    "makarona": "pasta",
    "supë": "soup",
    "salcë": "sauce",
    "kripë": "salt",
    "piper": "pepper (spice)",
    "sheqer": "sugar",
    "vaj": "oil",
    "uthull": "vinegar",
    "makinë": "car",
    "autobus": "bus",
    "tren": "train",
    "avion": "airplane",
    "anije": "ship",
    "biçikletë": "bicycle",
    "motoçikletë": "motorcycle",
    "taksi": "taxi",
    "metro": "metro/subway",
    "rrugë": "street/road",
    "autostradë": "highway",
    "urë": "bridge",
    "tunel": "tunnel",
    "stacion": "station",
    "aeroport": "airport",
    "port": "port",
    "parking": "parking",
    "semafor": "traffic light",
    "shenjë": "sign",
}

# Adjectives
ADJECTIVES = {
    "i madh": "big (masc)",
    "e madhe": "big (fem)",
    "i vogël": "small (masc)",
    "e vogël": "small (fem)",
    "i gjatë": "tall/long (masc)",
    "e gjatë": "tall/long (fem)",
    "i shkurtër": "short (masc)",
    "e shkurtër": "short (fem)",
    "i gjerë": "wide (masc)",
    "e gjerë": "wide (fem)",
    "i ngushtë": "narrow (masc)",
    "e ngushtë": "narrow (fem)",
    "i rëndë": "heavy (masc)",
    "e rëndë": "heavy (fem)",
    "i lehtë": "light (masc)",
    "e lehtë": "light (fem)",
    "i fortë": "strong (masc)",
    "e fortë": "strong (fem)",
    "i dobët": "weak (masc)",
    "e dobët": "weak (fem)",
    "i shpejtë": "fast (masc)",
    "e shpejtë": "fast (fem)",
    "i ngadaltë": "slow (masc)",
    "e ngadaltë": "slow (fem)",
    "i ri": "new/young (masc)",
    "e re": "new/young (fem)",
    "i vjetër": "old (masc)",
    "e vjetër": "old (fem)",
    "i mirë": "good (masc)",
    "e mirë": "good (fem)",
    "i keq": "bad (masc)",
    "e keqe": "bad (fem)",
    "i bukur": "beautiful (masc)",
    "e bukur": "beautiful (fem)",
    "i shëmtuar": "ugly (masc)",
    "e shëmtuar": "ugly (fem)",
    "i pastër": "clean (masc)",
    "e pastër": "clean (fem)",
    "i ndotur": "dirty (masc)",
    "e ndotur": "dirty (fem)",
    "i nxehtë": "hot (masc)",
    "e nxehtë": "hot (fem)",
    "i ftohtë": "cold (masc)",
    "e ftohtë": "cold (fem)",
    "i lagur": "wet (masc)",
    "e lagur": "wet (fem)",
    "i thatë": "dry (masc)",
    "e thatë": "dry (fem)",
    "i ëmbël": "sweet (masc)",
    "e ëmbël": "sweet (fem)",
    "i hidhur": "bitter (masc)",
    "e hidhur": "bitter (fem)",
    "i kripur": "salty (masc)",
    "e kripur": "salty (fem)",
    "i thartë": "sour (masc)",
    "e thartë": "sour (fem)",
    "i lumtur": "happy (masc)",
    "e lumtur": "happy (fem)",
    "i trishtuar": "sad (masc)",
    "e trishtuar": "sad (fem)",
    "i zemëruar": "angry (masc)",
    "e zemëruar": "angry (fem)",
    "i lodhur": "tired (masc)",
    "e lodhur": "tired (fem)",
    "i sëmurë": "sick (masc)",
    "e sëmurë": "sick (fem)",
    "i shëndoshë": "healthy (masc)",
    "e shëndoshë": "healthy (fem)",
    "i zgjuar": "smart/clever (masc)",
    "e zgjuar": "smart/clever (fem)",
    "i budalla": "stupid (masc)",
    "e budalla": "stupid (fem)",
    "i pasur": "rich (masc)",
    "e pasur": "rich (fem)",
    "i varfër": "poor (masc)",
    "e varfër": "poor (fem)",
    "i lirë": "free/cheap (masc)",
    "e lirë": "free/cheap (fem)",
    "i shtrenjtë": "expensive (masc)",
    "e shtrenjtë": "expensive (fem)",
    "i sigurt": "safe/sure (masc)",
    "e sigurt": "safe/sure (fem)",
    "i rrezikshëm": "dangerous (masc)",
    "e rrezikshme": "dangerous (fem)",
    "i lehtë": "easy (masc)",
    "e lehtë": "easy (fem)",
    "i vështirë": "difficult (masc)",
    "e vështirë": "difficult (fem)",
    "i rëndësishëm": "important (masc)",
    "e rëndësishme": "important (fem)",
    "interesant": "interesting",
    "i mërzitshëm": "boring (masc)",
    "e mërzitshme": "boring (fem)",
}

# Numbers
NUMBERS = {
    "zero": "0",
    "një": "1",
    "dy": "2",
    "tre": "3",
    "katër": "4",
    "pesë": "5",
    "gjashtë": "6",
    "shtatë": "7",
    "tetë": "8",
    "nëntë": "9",
    "dhjetë": "10",
    "njëmbëdhjetë": "11",
    "dymbëdhjetë": "12",
    "trembëdhjetë": "13",
    "katërmbëdhjetë": "14",
    "pesëmbëdhjetë": "15",
    "gjashtëmbëdhjetë": "16",
    "shtatëmbëdhjetë": "17",
    "tetëmbëdhjetë": "18",
    "nëntëmbëdhjetë": "19",
    "njëzet": "20",
    "tridhjetë": "30",
    "dyzet": "40",
    "pesëdhjetë": "50",
    "gjashtëdhjetë": "60",
    "shtatëdhjetë": "70",
    "tetëdhjetë": "80",
    "nëntëdhjetë": "90",
    "njëqind": "100",
    "dyqind": "200",
    "treqind": "300",
    "katërqind": "400",
    "pesëqind": "500",
    "njëmijë": "1000",
    "një milion": "1,000,000",
    "një miliard": "1,000,000,000",
    "i parë": "first",
    "i dytë": "second",
    "i tretë": "third",
    "i katërt": "fourth",
    "i pestë": "fifth",
    "i fundit": "last",
}

# Time expressions
TIME_EXPRESSIONS = {
    "sekondë": "second",
    "minutë": "minute",
    "orë": "hour",
    "ditë": "day",
    "javë": "week",
    "muaj": "month",
    "vit": "year",
    "shekull": "century",
    "mëngjes": "morning",
    "mesditë": "noon",
    "pasdite": "afternoon",
    "mbrëmje": "evening",
    "natë": "night",
    "mesnatë": "midnight",
    "dje": "yesterday",
    "sot": "today",
    "nesër": "tomorrow",
    "pasnesër": "day after tomorrow",
    "pardje": "day before yesterday",
    "javën e kaluar": "last week",
    "këtë javë": "this week",
    "javën e ardhshme": "next week",
    "muajin e kaluar": "last month",
    "këtë muaj": "this month",
    "muajin e ardhshëm": "next month",
    "vitin e kaluar": "last year",
    "këtë vit": "this year",
    "vitin e ardhshëm": "next year",
    "tani": "now",
    "më parë": "earlier/before",
    "më vonë": "later",
    "gjithmonë": "always",
    "kurrë": "never",
    "ndonjëherë": "sometimes",
    "shpesh": "often",
    "rrallë": "rarely",
    "zakonisht": "usually",
    "hënë": "Monday",
    "martë": "Tuesday",
    "mërkurë": "Wednesday",
    "enjte": "Thursday",
    "premte": "Friday",
    "shtunë": "Saturday",
    "diel": "Sunday",
    "janar": "January",
    "shkurt": "February",
    "mars": "March",
    "prill": "April",
    "maj": "May",
    "qershor": "June",
    "korrik": "July",
    "gusht": "August",
    "shtator": "September",
    "tetor": "October",
    "nëntor": "November",
    "dhjetor": "December",
}

# Common phrases for AI responses
AI_RESPONSES = {
    "si mund të të ndihmoj": "how can I help you",
    "a ka diçka tjetër": "is there anything else",
    "faleminderit për pyetjen": "thank you for the question",
    "le të shpjegoj": "let me explain",
    "sipas informacionit tim": "according to my information",
    "bazuar në të dhënat": "based on the data",
    "nuk kam informacion": "I don't have information",
    "më vjen keq": "I'm sorry",
    "nuk e kuptova pyetjen": "I didn't understand the question",
    "mund ta sqarosh": "can you clarify",
    "po përpunoj": "I'm processing",
    "po kërkoj": "I'm searching",
    "po analizoj": "I'm analyzing",
    "ja përfundimi": "here's the conclusion",
    "shpresoj se ndihmova": "I hope I helped",
    "pyet lirisht": "feel free to ask",
    "jam këtu për ty": "I'm here for you",
    "mirë se erdhe": "welcome",
    "ditë të mbarë": "have a good day",
}

# Clisonix-specific terms
CLISONIX_TERMS = {
    "Clisonix": "Platformë e Inteligjencës Industriale",
    "Ocean AI": "Asistent AI i Clisonix",
    "ASI Trinity": "Tre superinteligjenca artificiale",
    "ALBA": "Inteligjenca Analitike",
    "ALBI": "Inteligjenca Kreative", 
    "JONA": "Koordinatori i Inteligjencës",
    "MegaLayerEngine": "Motor me miliona kombinime analize",
    "Knowledge Seeds": "Farë njohurie e integruar",
    "Curiosity Ocean": "Modul i eksplorimeve dhe pyetjeve",
    "CEO": "Drejtor Ekzekutiv",
    "themelues": "founder",
    "Ledjan Ahmati": "Geschäftsführer dhe Themelues i Clisonix",
    "ABA GmbH": "Organizata mëmë (Amtsgericht Bochum HRB: 21069)",
    "REST API": "Ndërfaqe programimi",
    "IoT": "Internet i Gjërave",
    "LoRa": "Teknologji sensori me rreze të gjatë",
    "cloud": "re/cloud computing",
    "sensor": "pajisje matëse",
    "telemetri": "transmetim i të dhënave në distancë",
    "analitikë": "analizë e të dhënave",
}

# Common sentence patterns for Albanian
SENTENCE_PATTERNS = {
    "greeting_response": [
        "Mirëdita! Si mund të të ndihmoj sot?",
        "Tungjatjeta! Jam këtu për ty. Çfarë të intereson?",
        "Përshëndetje! Mirë se erdhe në Clisonix. Si mund të ndihmoj?",
        "Ç'kemi! Jam Ocean AI. Pyet çfarë të duash!",
    ],
    "confusion_response": [
        "Më fal, nuk e kuptova mirë pyetjen. Mund ta përsëritësh?",
        "Nuk jam i sigurt çfarë kërkon. Mund të jesh më specifik?",
        "Hmm, nuk e mora vesh. Provoje përsëri me fjalë të tjera?",
    ],
    "help_offer": [
        "Mund të të ndihmoj me:",
        "Ja çfarë di të bëj:",
        "Ekspertizat e mia përfshijnë:",
    ],
    "farewell": [
        "Faleminderit! Ditë të mbarë!",
        "Mirupafshim! Kthehu kur të duash!",
        "Ishte kënaqësi! Shihemi!",
    ],
    "affirmative": [
        "Po, sigurisht!",
        "Patjetër!",
        "Me kënaqësi!",
        "Natyrisht!",
    ],
    "negative": [
        "Jo, më vjen keq.",
        "Fatkeqësisht jo.",
        "Nuk kam mundësi për këtë.",
    ],
    "about_clisonix": [
        "Clisonix është një platformë e inteligjencës industriale e krijuar nga Ledjan Ahmati.",
        "Ledjan Ahmati është Geschäftsführer dhe themeluesi i Clisonix.",
        "Ne ofrojmë REST API, zgjidhje IoT me LoRa, dhe analitikë në kohë reale.",
        "Clisonix operon nën ABA GmbH (Amtsgericht Bochum HRB: 21069).",
        "Kontakti: support@clisonix.com ose +49 2327 9954413",
    ],
}


def get_albanian_response(query: str) -> str | None:
    """
    Try to match query with Albanian patterns and return appropriate response.
    Returns None if no match found.
    """
    query_lower = query.lower().strip()
    
    # Check for greetings
    greetings = ["përshëndetje", "mirëdita", "ckemi", "ç'kemi", "tungjatjeta", 
                 "si je", "si jeni", "mirëmëngjes", "mirëmbrëma", "pershendetje",
                 "pershendetje", "hej", "ej", "ore"]
    for g in greetings:
        if g in query_lower:
            import random
            return random.choice(SENTENCE_PATTERNS["greeting_response"])
    
    # Check for Clisonix questions
    clisonix_keywords = ["clisonix", "kush", "themelues", "ceo", "krijoi", "ndërtoi", 
                         "kompani", "platforma", "ledjan"]
    if any(k in query_lower for k in clisonix_keywords):
        if "kush" in query_lower or "ceo" in query_lower or "themelues" in query_lower:
            return "Ledjan Ahmati është Geschäftsführer dhe themeluesi i Clisonix. Ai ka krijuar këtë platformë të inteligjencës industriale që operon nën ABA GmbH (Amtsgericht Bochum HRB: 21069)."
    
    # Check for "what can you do" questions
    help_keywords = ["çfarë", "cfare", "mund", "bësh", "besh", "ndihmosh", "ndihmoj"]
    if any(k in query_lower for k in help_keywords):
        return """Mund të të ndihmoj me shumë gjëra:

🤖 **Teknologji & AI** - Pyetje rreth inteligjencës artificiale
🔬 **Shkencë** - Biologji, fizikë, kimi
🌍 **Gjeografi & Histori** - Fakte rreth botës
💹 **Financa** - Koncepte ekonomike
🇦🇱 **Shqipëri** - Kulturë, histori, gjuhë

Thjesht pyet dhe unë do të përpiqem të përgjigjem!"""
    
    # Check for farewell
    farewells = ["lamtumirë", "mirupafshim", "shihemi", "natën", "ciao", "bye"]
    for f in farewells:
        if f in query_lower:
            import random
            return random.choice(SENTENCE_PATTERNS["farewell"])
    
    return None


def detect_albanian(text: str) -> bool:
    """
    Detect if text is in Albanian language.
    """
    albanian_indicators = [
        "ë", "ç", "është", "dhe", "për", "një", "nga", "kjo",
        "janë", "kam", "kemi", "çfarë", "kush", "pse", "nuk",
        "mund", "duhet", "mirë", "keq", "shqip", "shqipëri"
    ]
    text_lower = text.lower()
    matches = sum(1 for indicator in albanian_indicators if indicator in text_lower)
    return matches >= 2


def get_word_translation(word: str) -> str | None:
    """
    Get English translation for an Albanian word.
    """
    word_lower = word.lower().strip()
    
    # Search all dictionaries
    all_dicts = [GREETINGS, QUESTION_WORDS, VERBS, TECH_NOUNS, 
                 COMMON_NOUNS, ADJECTIVES, NUMBERS, TIME_EXPRESSIONS,
                 AI_RESPONSES, CLISONIX_TERMS]
    
    for d in all_dicts:
        if word_lower in d:
            return d[word_lower]
    
    return None


# Combine all words for easy access
ALL_ALBANIAN_WORDS = {}
ALL_ALBANIAN_WORDS.update(GREETINGS)
ALL_ALBANIAN_WORDS.update(QUESTION_WORDS)
ALL_ALBANIAN_WORDS.update(VERBS)
ALL_ALBANIAN_WORDS.update(TECH_NOUNS)
ALL_ALBANIAN_WORDS.update(COMMON_NOUNS)
ALL_ALBANIAN_WORDS.update(ADJECTIVES)
ALL_ALBANIAN_WORDS.update(NUMBERS)
ALL_ALBANIAN_WORDS.update(TIME_EXPRESSIONS)
ALL_ALBANIAN_WORDS.update(AI_RESPONSES)
ALL_ALBANIAN_WORDS.update(CLISONIX_TERMS)

# Word count
WORD_COUNT = len(ALL_ALBANIAN_WORDS)

if __name__ == "__main__":
    print(f"Albanian Dictionary loaded with {WORD_COUNT} words/phrases")
    print("\nSample translations:")
    for word in ["përshëndetje", "kompjuter", "Ledjan Ahmati", "inteligjencë artificiale"]:
        trans = get_word_translation(word)
        if trans:
            print(f"  {word} → {trans}")
