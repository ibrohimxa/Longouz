"""IELTS Academic uslubidagi savollar (rejim: "ielts").

Haqiqiy IELTS Academic Reading formatiga mos topshiriq turlari: TRUE / FALSE / NOT GIVEN, multiple choice,
sentence completion (NO MORE THAN TWO WORDS) va Academic Word List lug'ati.
Barcha matnlar LongoUZ uchun yozilgan original matnlar (IELTS rasmiy materiallaridan ko'chirilmagan).
"""
from ._dsl import C, O, expand, validate

INSTR_TFNG = ("Write TRUE if the statement agrees with the information, FALSE if it contradicts the information, "
              "or NOT GIVEN if there is no information on this.")

PASSAGES = [
    ("IR1", "Urban heat islands",
     "Cities are often several degrees warmer than the surrounding countryside, a pattern known as the urban heat island. "
     "Dark surfaces such as asphalt and roofing absorb sunlight during the day and release the stored heat slowly at night, "
     "so the difference between city and rural temperatures is usually greatest after sunset. Waste heat from vehicles, "
     "air-conditioning units and factories adds to the effect. Planners have tested several remedies. Reflective 'cool roofs' "
     "can lower roof surface temperatures considerably, and street trees cool the air both by providing shade and through "
     "the evaporation of water from their leaves. However, trees need regular watering in dry climates, which some city "
     "councils consider too expensive.",
     [("The temperature gap between cities and the countryside is usually largest at night.", "TRUE"),
      ("Cool roofs are cheaper to install than ordinary roofs.", "NOT GIVEN"),
      ("Street trees reduce temperatures only by providing shade.", "FALSE")],
     ("According to the passage, why do some city councils hesitate to plant more trees?",
      "Watering them in dry climates costs too much", ["Trees damage the asphalt", "Trees block reflective roofs", "Trees increase waste heat"]),
     ("Dark surfaces release stored heat slowly at ______.", ["night", "at night"])),

    ("IR2", "Knowledge on the Silk Road",
     "The Silk Road was not a single road but a network of routes that linked China with the Mediterranean for more than a "
     "thousand years. Merchants carried silk, spices and paper, but ideas travelled as well. Cities such as Samarkand and "
     "Bukhara became centres of learning where scholars translated scientific texts and debated new theories. Papermaking, "
     "which began in China, reached Samarkand in the eighth century, and the city soon became famous for the quality of its "
     "paper. Cheaper paper allowed libraries to grow and made it easier for students to copy books. Historians note that "
     "most traders travelled only one section of the network before selling their goods to the next merchant.",
     [("The Silk Road consisted of one main road between China and Europe.", "FALSE"),
      ("Samarkand was known for producing high-quality paper.", "TRUE"),
      ("Bukhara had more libraries than Samarkand.", "NOT GIVEN")],
     ("What does the passage say about most Silk Road traders?",
      "They travelled only part of the network", ["They travelled from China to the Mediterranean", "They carried only silk", "They worked as translators"]),
     ("Papermaking reached Samarkand in the ______ century.", ["eighth", "8th"])),

    ("IR3", "Sleep and memory",
     "Researchers have long suspected that sleep helps the brain store new information. In one experiment, volunteers learned "
     "a list of word pairs in the evening and were tested the next morning. Those who had slept normally remembered more "
     "pairs than a group kept awake for the same period. Brain recordings suggest that during deep sleep the hippocampus "
     "replays patterns of activity from the day, which may help to transfer memories to long-term storage. Short daytime "
     "naps appear to offer a smaller benefit. The scientists warn, however, that the results apply mainly to facts and "
     "word lists; the effect of sleep on learning physical skills is still being studied.",
     [("Volunteers who slept remembered more word pairs than those who stayed awake.", "TRUE"),
      ("Daytime naps are more helpful for memory than a full night's sleep.", "FALSE"),
      ("The volunteers were all university students.", "NOT GIVEN")],
     ("According to the passage, what happens in the hippocampus during deep sleep?",
      "Patterns of activity from the day are replayed", ["New brain cells are created", "Physical skills are practised", "Word lists are forgotten"]),
     ("Research on how sleep affects the learning of ______ skills is still in progress.", ["physical"])),

    ("IR4", "Turning seawater into drinking water",
     "Desalination removes salt from seawater to produce fresh water. The most common modern method, reverse osmosis, "
     "pushes seawater through membranes with extremely small pores that block salt particles. The process needs a great deal "
     "of electricity, which is why the cost of desalinated water depends heavily on energy prices. Another problem is the "
     "very salty water, called brine, that remains after treatment. If brine is released carelessly, it can harm marine life "
     "near the outlet. Some new plants mix brine with treated wastewater before returning it to the sea, while others are "
     "experimenting with solar power to reduce energy costs.",
     [("Reverse osmosis is the most widely used desalination method today.", "TRUE"),
      ("Desalination plants never affect sea creatures.", "FALSE"),
      ("Desalination is used mainly in Middle Eastern countries.", "NOT GIVEN")],
     ("Why does the price of desalinated water depend on energy prices?",
      "The process uses a lot of electricity", ["Brine must be transported far away", "Membranes are made from oil", "Seawater must be heated to boiling"]),
     ("The very salty water left after treatment is called ______.", ["brine"])),

    ("IR5", "How honeybees share information",
     "When a honeybee finds a good source of food, it returns to the hive and performs a 'waggle dance'. The angle of the "
     "dance in relation to the vertical comb indicates the direction of the food relative to the sun, while the length of "
     "the waggle section shows how far away it is. Other bees follow the dancer closely and then fly out to search. "
     "Experiments in which scientists moved feeding stations to new places showed that recruited bees arrived at the "
     "correct location surprisingly often. Bees also use scent: dancers carry the smell of the flowers they visited, which "
     "helps followers recognise the right plants when they arrive.",
     [("The length of the waggle part tells other bees the distance to the food.", "TRUE"),
      ("Bees rely only on the dance and never use smell.", "FALSE"),
      ("Bees dance more quickly on hot days.", "NOT GIVEN")],
     ("What does the angle of the waggle dance indicate?",
      "The direction of the food relative to the sun", ["The amount of food available", "The type of flower", "The age of the dancer"]),
     ("Dancers carry the ______ of the flowers they visited.", ["smell", "scent"])),

    ("IR6", "The shrinking Aral Sea",
     "The Aral Sea, which lies between Uzbekistan and Kazakhstan, was once one of the largest lakes in the world. From the "
     "1960s, large amounts of water from the Amu Darya and Syr Darya rivers were diverted to irrigate cotton fields, and the "
     "sea began to shrink rapidly. As the water retreated, fishing towns were left far from the shore and dust from the "
     "exposed seabed spread salt across farmland. In 2005 a dam was completed to separate the smaller northern part of the "
     "sea, and water levels there have since risen. Scientists are now planting salt-tolerant shrubs such as saxaul on the "
     "dry seabed to reduce dust storms.",
     [("The rivers feeding the Aral Sea were used to water cotton fields.", "TRUE"),
      ("Water levels in the northern part of the sea continued to fall after 2005.", "FALSE"),
      ("The fishing industry has completely recovered in the southern part of the sea.", "NOT GIVEN")],
     ("Why are scientists planting saxaul on the dry seabed?",
      "To reduce dust storms", ["To feed livestock", "To produce cotton", "To refill the rivers"]),
     ("A dam completed in 2005 separated the ______ part of the sea.", ["northern", "north"])),
]

AWL = [  # Academic Word List — sinonim tanlash
    ("substantial", "considerable", ["slight", "temporary", "hidden"]),
    ("crucial", "essential", ["optional", "harmful", "ordinary"]),
    ("diminish", "decrease", ["expand", "repeat", "explain"]),
    ("advocate", "support", ["oppose", "ignore", "measure"]),
    ("inevitable", "unavoidable", ["unlikely", "invisible", "unexpected"]),
    ("comprehensive", "complete", ["partial", "confusing", "expensive"]),
    ("hypothesis", "theory to be tested", ["final conclusion", "official rule", "historical record"]),
    ("fluctuate", "change frequently", ["stay the same", "rise steadily", "disappear suddenly"]),
    ("constrain", "limit", ["encourage", "reward", "release"]),
    ("allocate", "distribute", ["collect", "refuse", "borrow"]),
    ("deteriorate", "become worse", ["improve", "stay stable", "become larger"]),
    ("feasible", "possible", ["dangerous", "illegal", "unnecessary"]),
    ("subsequent", "following", ["previous", "current", "original"]),
    ("ambiguous", "unclear", ["obvious", "accurate", "brief"]),
    ("enhance", "improve", ["reduce", "replace", "describe"]),
    ("predominantly", "mainly", ["rarely", "partly", "recently"]),
]

COLLOC = [  # IELTS Writing uchun kollokatsiyalar
    ("Governments should ______ measures to reduce air pollution.", "take", ["make", "do", "give"]),
    ("The number of tourists rose ______ between 2010 and 2020.", "steadily", ["steady", "steadiness", "steadied"]),
    ("There was a sharp ______ in unemployment after the factory closed.", "increase", ["increasing", "increased", "increasingly"]),
    ("Many experts ______ the view that education should be free.", "hold", ["keep", "make", "have got"]),
    ("The graph shows that sales ______ a peak in July.", "reached", ["arrived", "came", "went"]),
    ("This problem has a significant ______ on young people.", "impact", ["affect", "effective", "impactful"]),
    ("It is widely ______ that exercise improves mental health.", "believed", ["belief", "believing", "believable"]),
    ("______, the advantages of online learning outweigh the disadvantages.", "On balance", ["In balance", "At balance", "By balance"]),
]


def _passage_q(title, text, q):
    return f"IELTS Reading — «{title}»\n\n{text}\n\n{q}"


def pack() -> dict:
    topics, questions = [], []
    t_tfng = ("IR-TFNG", 11, "IELTS Reading: True / False / Not Given", "free")
    t_mcq = ("IR-MCQ", 11, "IELTS Reading: Multiple choice", "free")
    t_sc = ("IR-SC", 11, "IELTS Reading: Sentence completion", "pro")
    t_awl = ("IV-AWL", 11, "IELTS Vocabulary: Academic Word List", "free")
    t_col = ("IW-COL", 11, "IELTS Writing: collocations va grafik tili", "pro")
    tfng, mcq, sc = [], [], []
    for code, title, text, tf, (mq, ma, mw), (sq, sa) in PASSAGES:
        for stmt, ans in tf:
            acc = {"TRUE": ["TRUE", "T", "true"], "FALSE": ["FALSE", "F", "false"], "NOT GIVEN": ["NOT GIVEN", "NG", "not given"]}[ans]
            tfng.append(O(2, _passage_q(title, text, f"{INSTR_TFNG}\n\nStatement: {stmt}\n(Answer: TRUE / FALSE / NOT GIVEN)"), acc,
                          f"Javob: {ans}. Matnda tekshiring: «{title}»."))
        mcq.append(C(2, _passage_q(title, text, f"Choose the correct answer: {mq}"), ma, mw, f"Matnda aytilgan: {ma}."))
        sc.append(O(3, _passage_q(title, text, f"Complete the sentence. Write NO MORE THAN TWO WORDS from the passage.\n\n{sq}"), sa,
                    f"To'g'ri javob: {sa[0]}."))
    awl = [C(1 if i < 8 else 2, f"Choose the word or phrase closest in meaning to «{w}».", a, ws, f"{w} = {a}.") for i, (w, a, ws) in enumerate(AWL)]
    col = [C(2, f"Choose the best option to complete the sentence (academic English):\n{s}", a, ws, f"To'g'ri: {a}.") for s, a, ws in COLLOC]
    for (code, grade, name, tier), items in ((t_tfng, tfng), (t_mcq, mcq), (t_sc, sc), (t_awl, awl), (t_col, col)):
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": ""})
        questions.extend(expand(name, grade, items, ""))
    problems = validate(questions)
    if problems:
        import logging
        logging.getLogger(__name__).warning("IELTS bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "english", "modes": ["ielts"], "topics": topics, "questions": questions}
