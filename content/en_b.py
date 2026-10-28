"""Ingliz tili: lug'at, o'qish va murakkab mavzular."""
from ._dsl import C, O, M

Q = {}

Q["E21"] = [
    C(1, "Your mother's sister is your ___.", "aunt", ["uncle", "cousin", "niece"], "Family vocabulary."),
    C(1, "My brother's son is my ___.", "nephew", ["niece", "cousin", "uncle"], "nephew = brother's/sister's son."),
    C(2, "I usually ___ up at 6 a.m.", "get", ["take", "make", "do"], "get up = leave bed."),
    C(2, "She ___ her teeth twice a day.", "brushes", ["washes", "cleans up", "combs"], "brush teeth."),
    C(3, "Which word does NOT belong to the group? mother, father, sister, teacher", "teacher", ["mother", "father", "sister"], "Teacher is not a family member."),
    O(3, "Your father's father is your ___. (one word)", ["grandfather", "grandpa"], "Grandfather."),
    M(2, [("mother's brother", "uncle"), ("uncle's daughter", "cousin"), ("brother's daughter", "niece")], "Family members."),
]
Q["E22"] = [
    C(1, "You need a ___ to travel by plane.", "ticket", ["recipe", "receipt", "invoice"], "ticket = travel pass."),
    C(1, "I am going to the airport to catch a ___.", "flight", ["trip", "journey", "route"], "flight = air travel."),
    C(2, "A place where you stay when travelling is a ___.", "hotel", ["museum", "bank", "pharmacy"], "Hotel = accommodation."),
    C(2, "Which is a means of public transport?", "tram", ["bike", "car", "scooter"], "Tram is public transport."),
    C(3, "'Journey' and 'trip' are both about ___.", "travelling from one place to another", ["buying tickets", "booking hotels", "learning languages"], "They are synonyms-ish."),
    O(3, "The official document that allows you to enter other countries is a ___. (one word)", ["passport"], "Passport."),
]
Q["E23"] = [
    C(1, "If you have a headache, you take a ___.", "painkiller", ["pillow", "bandage", "thermometer"], "Painkiller = analgesic."),
    C(1, "A doctor who treats teeth is a ___.", "dentist", ["surgeon", "nurse", "pharmacist"], "Dentist."),
    C(2, "I have a ___. I keep coughing and sneezing.", "cold", ["fracture", "bruise", "allergy test"], "Cold symptoms."),
    C(2, "To stay healthy you should ___ regularly.", "exercise", ["exercises", "exercised", "an exercise"], "Verb exercise."),
    C(3, "Which is NOT a part of the body?", "pillow", ["elbow", "knee", "shoulder"], "Pillow is an object."),
    O(3, "A place where you buy medicine is a ___. (one word)", ["pharmacy", "chemist's", "drugstore"], "Pharmacy."),
]
Q["E24"] = [
    C(1, "A person who writes news stories is a ___.", "journalist", ["architect", "chef", "pilot"], "Journalist."),
    C(1, "A ___ designs buildings.", "architect", ["lawyer", "accountant", "plumber"], "Architect."),
    C(2, "She wants to study at a ___ to become a doctor.", "medical university", ["kindergarten", "primary school", "playground"], "Higher education."),
    C(2, "A written test at the end of a course is called an ___.", "exam", ["excuse", "essay topic", "exit"], "Exam."),
    C(3, "'Apply for a job' means to ___.", "formally ask for a job", ["leave a job", "get a promotion", "complain about a job"], "Apply = request officially."),
    O(3, "A person who works for a company is an ___. (one word)", ["employee"], "Employee."),
]
Q["E25"] = [
    C(1, "Plastic bags pollute the ___.", "environment", ["employment", "equipment", "entertainment"], "Environment."),
    C(1, "We should ___ paper, glass and plastic.", "recycle", ["reduce", "reject", "retire"], "Recycle."),
    C(2, "Global ___ is causing glaciers to melt.", "warming", ["washing", "walking", "waiting"], "Global warming."),
    C(2, "Burning fossil fuels increases ___ in the air.", "carbon dioxide", ["oxygen only", "fresh water", "sunlight"], "CO₂."),
    C(3, "An animal in danger of disappearing is ___.", "endangered", ["extinguished", "enraged", "entertained"], "Endangered species."),
    O(3, "Energy from the sun is called ___ energy. (one word)", ["solar"], "Solar energy."),
]
Q["E26"] = [
    C(1, "You use a ___ to type text on a computer.", "keyboard", ["monitor", "printer", "speaker"], "Keyboard."),
    C(1, "Wi-Fi allows you to connect to the ___.", "internet", ["interval", "interior", "interview"], "Internet."),
    C(2, "A program that protects your computer from viruses is called ___.", "antivirus software", ["a browser", "a spreadsheet", "a screensaver"], "Antivirus."),
    C(2, "To save a file to your phone from the internet, you ___ it.", "download", ["upload", "unplug", "uninstall"], "Download."),
    C(3, "'Artificial intelligence' is often shortened to ___.", "AI", ["IT", "PC", "OS"], "AI."),
    O(3, "Copying files from your computer to the internet is called ___. (one word)", ["uploading", "upload"], "Upload."),
]
Q["E27"] = [
    C(2, "'It's raining cats and dogs' means:", "It is raining heavily.", ["Animals are falling.", "It is a light drizzle.", "It's a sunny day."], "Idiom."),
    C(2, "'Break the ice' means:", "start a conversation in an awkward situation", ["destroy something", "go skating", "cool a drink"], "Idiom."),
    C(3, "'Once in a blue moon' means:", "very rarely", ["every night", "very often", "never"], "Idiom."),
    C(3, "Which collocation with 'decision' is correct?", "make a decision", ["do a decision", "take a decision up", "build a decision"], "make a decision."),
    C(3, "Which collocation with 'homework' is correct?", "do homework", ["make homework", "create homework", "take homework"], "do homework."),
    O(3, "Complete the idiom: A piece of ___ (= very easy). (one word)", ["cake"], "A piece of cake."),
]
Q["E28"] = [
    C(1, "Read: 'Tom gets up at 7. He has breakfast and goes to school by bus. He studies until 2 p.m.' — How does Tom get to school?", "By bus", ["On foot", "By bike", "By car"], "Stated in the text."),
    C(1, "Read: 'Anna has a cat called Misha. Misha likes milk and sleeps all day.' — What does Misha like?", "Milk", ["Fish", "Meat", "Bones"], "Stated in the text."),
    C(2, "Read: 'The library opens at 9 a.m. and closes at 6 p.m. On Sundays it is closed.' — When is the library closed?", "On Sundays", ["On Saturdays", "At 6 p.m. daily", "At 9 a.m."], "Detail question."),
    C(2, "Read: 'Water is essential for life. People can live for weeks without food, but only a few days without water.' — What is the main idea?", "Water is vital for life.", ["Food is unimportant.", "People never drink.", "Weeks are long."], "Main idea."),
    C(3, "Read: 'Although the exam was difficult, Karim stayed calm and answered all the questions.' — Karim was ___.", "calm", ["angry", "afraid", "careless"], "Stated attitude."),
    O(3, "Read: 'Samarkand is famous for the Registan square.' — What is Samarkand famous for? (2 words)", ["Registan square", "the Registan"], "Detail."),
]
Q["E29"] = [
    C(2, "Read: 'The new phone is pricey, but its battery is outstanding.' — 'pricey' means:", "expensive", ["cheap", "small", "old"], "Context clue."),
    C(2, "Read: 'He was so exhausted that he fell asleep at his desk.' — 'exhausted' means:", "very tired", ["very angry", "very hungry", "very happy"], "Context clue."),
    C(3, "Read: 'She never complained; instead she smiled and kept working.' — What can we infer about her?", "She is patient and hard-working.", ["She is lazy.", "She is rude.", "She is bored."], "Inference."),
    C(3, "Read: 'The streets were empty and all the shops were shut.' — What can we infer?", "It was probably very late or a holiday.", ["It was lunchtime rush hour.", "A festival was in progress.", "The shops were opening."], "Inference."),
    C(3, "Read: 'Unlike her brother, who loves noise, Lola prefers silence.' — Lola prefers ___.", "quiet places", ["loud music", "crowded parties", "traffic"], "Contrast."),
    O(3, "Read: 'The dog barked furiously at the stranger.' — Write a synonym for 'furiously'. (one word, e.g. angrily)", ["angrily", "wildly", "fiercely", "loudly"], "Context."),
]
Q["E30"] = [
    C(1, "Synonym of 'big':", "large", ["tiny", "narrow", "thin"], "Synonym."),
    C(1, "Antonym of 'ancient':", "modern", ["old", "historic", "classical"], "Antonym."),
    C(2, "Synonym of 'begin':", "start", ["finish", "stop", "end"], "Synonym."),
    C(2, "Antonym of 'generous':", "mean", ["kind", "friendly", "polite"], "Antonym."),
    C(3, "Synonym of 'enormous':", "huge", ["tiny", "average", "little"], "Synonym."),
    O(3, "Write an antonym of 'rapid'. (one word)", ["slow"], "Antonym."),
    M(2, [("hard", "difficult"), ("quick", "fast"), ("glad", "happy")], "Synonyms."),
]
Q["E31"] = [
    C(2, "Choose the correct word: The weather ___ my mood.", "affects", ["effects", "affected by", "effect"], "affect = verb; effect = noun."),
    C(2, "Choose the correct word: I need some ___ on my essay.", "advice", ["advise", "advices", "advised"], "advice (noun) / advise (verb)."),
    C(3, "Choose the correct word: He didn't ___ to the party.", "come", ["came", "comes", "coming"], "did not + base."),
    C(3, "Choose the correct word: It's ___ umbrella. (possession)", "her", ["hers'", "she's", "hers"], "her + noun."),
    C(3, "Choose: ___ going to the park? (= Are you going)", "Are you", ["Your", "You're", "Youre"], "Are you...?"),
    O(3, "Complete: There are ___ books on the table. (their / there / they're) — write the correct word for 'in that place'.", ["there"], "There."),
]
Q["E32"] = [
    C(3, "Choose the correct inversion: ___ had he arrived than it started to rain.", "No sooner", ["As soon", "Hardly", "Not only"], "No sooner ... than."),
    C(3, "Never ___ such a beautiful place.", "have I seen", ["I have seen", "I saw have", "have seen I"], "Negative adverbial → inversion."),
    C(3, "Rarely ___ late for class.", "does he arrive", ["he arrives", "he does arrive", "arrives he"], "Inversion with rarely."),
    C(3, "Not only ___ the exam, but she also got the highest score.", "did she pass", ["she passed", "she did pass", "passed she"], "Not only + inversion."),
    C(3, "Under no circumstances ___ the door.", "should you open", ["you should open", "you open should", "open you should"], "Inversion."),
    O(3, "Complete: Hardly ___ I sat down when the phone rang. (one word)", ["had"], "Hardly had I... when."),
]
Q["E33"] = [
    C(2, "I wish I ___ a car. (I don't have one)", "had", ["have", "would have", "will have"], "Present wish → past simple."),
    C(2, "I wish it ___ raining. (annoying situation)", "would stop", ["stopped", "stops", "will stop"], "wish + would for annoyance."),
    C(3, "If only I ___ harder last year. (regret)", "had studied", ["studied", "study", "would study"], "Past regret → past perfect."),
    C(3, "I wish I ___ swim. (I can't)", "could", ["can", "will", "would"], "wish + could."),
    C(3, "She wishes she ___ there yesterday. (she wasn't there)", "had been", ["was", "were", "has been"], "Past wish."),
    O(3, "Complete: I wish I ___ (be) taller. (one word)", ["were", "was"], "wish + were/was."),
]
Q["E34"] = [
    C(1, "The team ___ playing well this season.", "is", ["are", "were", "be"], "Collective noun (UK may be plural), standard test: is."),
    C(1, "Neither the teacher nor the students ___ ready.", "are", ["is", "was", "be"], "Verb agrees with the nearer subject."),
    C(2, "Each of the boys ___ a book.", "has", ["have", "having", "are having"], "Each → singular."),
    C(2, "News ___ travelling fast these days.", "is", ["are", "were", "have"], "News is uncountable singular."),
    C(3, "There ___ many people in the hall.", "were", ["was", "is", "has"], "Plural subject."),
    O(3, "Complete: Mathematics ___ my favourite subject. (is/are)", ["is"], "Singular."),
]
Q["E35"] = [
    C(1, "This is my book and that is ___.", "yours", ["your", "you", "your's"], "Possessive pronoun."),
    C(1, "___ is a nice day, isn't it?", "It", ["He", "She", "They"], "Impersonal it."),
    C(2, "I like ___. (the girl)", "her", ["she", "hers", "herself"], "Object pronoun."),
    C(2, "He cut ___ while cooking.", "himself", ["him", "his", "he"], "Reflexive pronoun."),
    C(3, "The pen is not mine. It is ___.", "hers", ["her", "she", "she's"], "Possessive pronoun."),
    O(3, "Complete: They gave ___ the keys. (we, object form)", ["us"], "Object pronoun."),
]
Q["E36"] = [
    C(1, "How do we say 3/4?", "three quarters", ["three fours", "third four", "thirty four"], "Fractions."),
    C(1, "What is the correct way to say 1998?", "nineteen ninety-eight", ["one thousand nine ninety-eight", "ten ninety-eight", "nineteen eighty-nine"], "Years."),
    C(2, "The 21st is read as ___.", "the twenty-first", ["the twenty-one", "twenty-oneth", "twenty and first"], "Ordinals."),
    C(2, "Half past six is ___.", "6:30", ["6:15", "6:45", "5:30"], "Time."),
    C(3, "A quarter to nine is ___.", "8:45", ["9:15", "8:15", "9:45"], "Time."),
    O(3, "Write the number 100 in words. (one/two words)", ["one hundred", "a hundred", "hundred"], "100."),
]
Q["E37"] = [
    C(2, "Last summer we ___ to the mountains. We ___ there for a week. (Choose the best pair)", "went / stayed", ["go / stay", "have gone / have stayed", "were going / stay"], "Narrative past."),
    C(2, "I ___ in this city since 2010. (tense choice)", "have lived", ["lived", "live", "am living"], "since → present perfect."),
    C(3, "While I ___ in the park, I ___ an old friend.", "was walking / met", ["walked / was meeting", "walk / meet", "was walking / was meeting"], "Past continuous + past simple."),
    C(3, "By 2030, scientists ___ a cure for the disease.", "will have found", ["will find", "found", "have found"], "Future perfect."),
    C(3, "'I ___ here for ages when the bus finally came.'", "had been waiting", ["was waited", "have waited", "waited"], "Past perfect continuous."),
    O(3, "Complete: She ___ (live) here for ten years now. (2 words)", ["has lived"], "Present perfect."),
]
Q["E38"] = [
    C(1, "Which spelling of the word meaning 'needed' is correct?", "necessary", ["neccessary", "necesary", "neccesary"], "One c, two s."),
    C(1, "Which shopping-list sentence is punctuated correctly?", "I bought apples, bananas and milk.", ["I bought apples bananas, and milk.", "I bought, apples, bananas and milk.", "I bought apples; bananas and milk"], "List commas."),
    C(2, "Which spelling of the word meaning 'get' is correct?", "receive", ["recieve", "receeve", "receve"], "i before e except after c."),
    C(2, "Choose the sentence with correct apostrophes.", "It's a sunny day, and I'm happy.", ["Its a sunny day, and Im happy.", "Its' a sunny day, and I'm happy.", "It's a sunny day and, I'm happy."], "Apostrophes."),
    C(3, "Which sentence with direct speech is punctuated correctly?", "'Come here,' she said.", ["'Come here' she said.", "Come here, she said.", "'Come here.' she said"], "Direct speech punctuation."),
    O(3, "Fix the spelling: 'definately' → write the correct word.", ["definitely"], "definitely."),
]
Q["E39"] = [
    C(2, "He studied hard ___ pass the exam.", "in order to", ["because", "so that to", "in case of"], "Purpose."),
    C(2, "It was ___ cold that we stayed inside.", "so", ["such", "too", "very"], "so + adj + that."),
    C(3, "It was ___ a boring film that we left early.", "such", ["so", "too", "very"], "such + a/an + adj + noun."),
    C(3, "She spoke ___ quietly that nobody could hear her.", "so", ["such", "enough", "too"], "so + adv + that."),
    C(3, "He is ___ young to drive a car.", "too", ["enough", "so", "such"], "too + adj + to."),
    O(3, "Complete: She isn't old ___ to vote. (one word)", ["enough"], "adj + enough."),
]
Q["E40"] = [
    C(3, "___ the report, he went home. (After he finished)", "Having finished", ["Finish", "To finished", "Being finish"], "Perfect participle."),
    C(3, "The man ___ by the window is my uncle.", "standing", ["stand", "stood", "stands"], "Present participle clause."),
    C(3, "The book ___ by Orwell is famous.", "written", ["writing", "wrote", "write"], "Past participle clause."),
    C(3, "___ tired, she went to bed early.", "Feeling", ["Felt", "To feel", "Feels"], "Participle of reason."),
    C(3, "Which sentence uses a participle clause correctly?", "Walking down the street, I met an old friend.", ["Walk down the street, I met an old friend.", "Walked down the street, I meet an old friend.", "To walking down the street, I met a friend."], "-ing clause."),
    O(3, "Complete: ___ (not know) the answer, he stayed silent. (2 words, -ing)", ["not knowing"], "Negative participle."),
]
