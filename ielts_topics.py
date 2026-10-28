"""
LongoUZ — IELTS/Sertifikat Speaking va Writing bo'limlari uchun mavzular banki.

Speaking savollari HAQIQIY IELTS Speaking Part 1/2/3 formatiga mos: qisqa
shaxsiy savollar (Part 1), 1 daqiqalik tayyorlanib gapirish kartochkasi
(Part 2 — "cue card"), va chuqurroq muhokama savollari (Part 3).

Writing mavzulari IELTS Writing Task 2 uslubida — fikr bildirish/insho
yozish topshiriqlari (eng ko'p uchraydigan, real imtihonlarda qaytariladigan
mavzular asosida: ta'lim, texnologiya, atrof-muhit, jamiyat va h.k.).

Savol matnlarining o'zi INGLIZ TILIDA (chunki bu — ingliz tili imtihoni,
haqiqiy IELTS formatini simulyatsiya qiladi). Interfeys va AI fikr-mulohaza
(feedback) esa har doimgidek o'zbek tilida bo'ladi.
"""

SPEAKING_TOPICS = [
    {
        "id": "family-home",
        "title_uz": "Oila va uy",
        "part": 1,
        "questions": [
            "Can you describe your family?",
            "Do you live in a house or an apartment?",
            "What do you like most about your home?",
            "How often do you spend time with your family?",
        ],
    },
    {
        "id": "hometown",
        "title_uz": "Tug'ilgan shahar",
        "part": 1,
        "questions": [
            "Where is your hometown?",
            "What do you like about your hometown?",
            "Has your hometown changed much in recent years?",
            "Would you recommend your hometown to a tourist?",
        ],
    },
    {
        "id": "describe-person",
        "title_uz": "Sizga ta'sir qilgan inson (cue card)",
        "part": 2,
        "questions": [
            "Describe a person who has influenced you a lot. You should say: who this person is, "
            "how you know this person, what this person has done, and explain why this person has "
            "influenced you so much.",
        ],
    },
    {
        "id": "describe-place",
        "title_uz": "Borishni yoqtirgan joy (cue card)",
        "part": 2,
        "questions": [
            "Describe a place you often visit and enjoy. You should say: where it is, how often you "
            "go there, what you do there, and explain why you enjoy visiting this place.",
        ],
    },
    {
        "id": "describe-achievement",
        "title_uz": "Erishgan yutuq (cue card)",
        "part": 2,
        "questions": [
            "Describe an achievement you are proud of. You should say: what it was, how you achieved "
            "it, what difficulties you faced, and explain why you are proud of it.",
        ],
    },
    {
        "id": "technology-discussion",
        "title_uz": "Texnologiya haqida muhokama",
        "part": 3,
        "questions": [
            "How has technology changed the way people communicate?",
            "Do you think people rely on technology too much nowadays?",
            "What are the disadvantages of modern technology for young people?",
            "How do you think technology will change education in the future?",
        ],
    },
    {
        "id": "education-discussion",
        "title_uz": "Ta'lim haqida muhokama",
        "part": 3,
        "questions": [
            "What are the most important skills for students to learn at school?",
            "Do you think online education is as effective as traditional classroom learning?",
            "How can governments improve the quality of education?",
            "Should university education be free for everyone?",
        ],
    },
    {
        "id": "work-career",
        "title_uz": "Ish va kasb",
        "part": 1,
        "questions": [
            "Do you work or are you a student?",
            "What do you like about your job or studies?",
            "What kind of job would you like to have in the future?",
            "Is it important to enjoy your job, or is salary more important?",
        ],
    },
    {
        "id": "environment-discussion",
        "title_uz": "Atrof-muhit haqida muhokama",
        "part": 3,
        "questions": [
            "What are the main causes of environmental problems in cities?",
            "What can individuals do to help protect the environment?",
            "Should governments punish companies that pollute the environment?",
            "Do you think environmental problems will get better or worse in the future?",
        ],
    },
    {
        "id": "describe-skill",
        "title_uz": "O'rganmoqchi bo'lgan ko'nikma (cue card)",
        "part": 2,
        "questions": [
            "Describe a skill you would like to learn. You should say: what the skill is, why you "
            "want to learn it, how you would learn it, and explain how this skill would help you.",
        ],
    },
]

WRITING_TOPICS = [
    {
        "id": "technology-society",
        "title_uz": "Texnologiya va jamiyat",
        "task": "task2",
        "prompt_en": (
            "Some people believe that technology has made our lives more complicated, while others "
            "think it has made life easier. Discuss both views and give your own opinion."
        ),
    },
    {
        "id": "online-education",
        "title_uz": "Onlayn ta'lim",
        "task": "task2",
        "prompt_en": (
            "In many countries, more and more students are studying online instead of attending "
            "traditional classes. Do the advantages of this outweigh the disadvantages?"
        ),
    },
    {
        "id": "environment-individual",
        "title_uz": "Shaxsiy mas'uliyat va atrof-muhit",
        "task": "task2",
        "prompt_en": (
            "Some people think environmental problems should be solved by governments, while others "
            "believe individuals are responsible. Discuss both views and give your own opinion."
        ),
    },
    {
        "id": "social-media",
        "title_uz": "Ijtimoiy tarmoqlar",
        "task": "task2",
        "prompt_en": (
            "Social media has changed the way young people communicate with each other. Do you "
            "think this development has had a positive or negative effect on society?"
        ),
    },
    {
        "id": "work-life-balance",
        "title_uz": "Ish va hayot muvozanati",
        "task": "task2",
        "prompt_en": (
            "Nowadays, people are spending more time at work and less time with their families. "
            "What are the causes of this, and what solutions can you suggest?"
        ),
    },
    {
        "id": "traditional-vs-modern",
        "title_uz": "An'ana va zamonaviylik",
        "task": "task2",
        "prompt_en": (
            "Some people believe that traditional customs and values are being lost due to "
            "globalization. To what extent do you agree or disagree?"
        ),
    },
    {
        "id": "urbanization",
        "title_uz": "Shaharlashuv",
        "task": "task2",
        "prompt_en": (
            "More and more people are moving from rural areas to big cities. What are the reasons "
            "for this, and what problems does it create?"
        ),
    },
    {
        "id": "foreign-language",
        "title_uz": "Chet tilini o'rganish",
        "task": "task2",
        "prompt_en": (
            "Some people think that children should start learning a foreign language at primary "
            "school, while others believe it is better to wait until secondary school. Discuss both "
            "views and give your own opinion."
        ),
    },
]

SPEAKING_TOPICS_BY_ID = {t["id"]: t for t in SPEAKING_TOPICS}
WRITING_TOPICS_BY_ID = {t["id"]: t for t in WRITING_TOPICS}
