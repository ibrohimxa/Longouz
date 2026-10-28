"""Ingliz tili: grammatika mavzulari."""
from ._dsl import C, O, M

Q = {}

Q["E1"] = [
    C(1, "She ___ to school every day.", "goes", ["go", "going", "is go"], "Third person singular + -es: goes."),
    C(1, "Look! The children ___ in the garden.", "are playing", ["play", "plays", "played"], "Look! signals an action happening now."),
    C(2, "Which negative Present Simple sentence is correct?", "He doesn't like coffee.", ["He don't like coffee.", "He doesn't likes coffee.", "He not like coffee."], "doesn't + base verb."),
    C(2, "I usually ___ breakfast at seven, but today I ___ it at eight.", "have / am having", ["am having / have", "have / have", "had / am having"], "Habit vs. action at the moment."),
    C(3, "Which verb is NOT normally used in the continuous form?", "know", ["run", "write", "cook"], "State verbs (know, love, want) are rarely continuous."),
    O(3, "Complete: Water ___ (boil) at 100 degrees. (one word)", ["boils"], "General truth → Present Simple."),
    M(2, [("always", "Present Simple"), ("at the moment", "Present Continuous"), ("every Sunday", "Present Simple")], "Time expressions."),
]
Q["E2"] = [
    C(1, "Yesterday I ___ a good film.", "watched", ["watch", "watching", "have watched"], "yesterday → Past Simple."),
    C(1, "What is the past form of 'go'?", "went", ["goed", "gone", "going"], "Irregular verb: go – went – gone."),
    C(2, "I ___ TV when the phone rang.", "was watching", ["watched", "am watching", "have watched"], "Past Continuous for an interrupted action."),
    C(2, "Which Past Simple question is correct?", "Did you see him last night?", ["Did you saw him last night?", "Do you saw him last night?", "You did see him last night?"], "Did + base verb."),
    C(3, "While she ___ dinner, he ___ the newspaper.", "was cooking / was reading", ["cooked / read", "was cooking / read", "cooks / is reading"], "Two parallel past actions."),
    O(3, "Write the past simple of 'buy'. (one word)", ["bought"], "buy – bought – bought."),
]
Q["E3"] = [
    C(1, "I ___ never ___ sushi.", "have / eaten", ["has / ate", "did / eat", "am / eating"], "Experience → Present Perfect."),
    C(1, "She has lived here ___ 2015.", "since", ["for", "from", "during"], "since + point in time."),
    C(2, "They have lived here ___ ten years.", "for", ["since", "during", "from"], "for + period."),
    C(2, "Choose the correct sentence about a finished time.", "I saw him yesterday.", ["I have seen him yesterday.", "I have saw him yesterday.", "I see him yesterday."], "Finished time (yesterday) → Past Simple."),
    C(3, "Which sentence refers to a result NOW?", "I have lost my keys.", ["I lost my keys in 2019.", "I was losing my keys.", "I had lost my keys last week."], "Present Perfect shows present result."),
    O(3, "Complete: He ___ (already / finish) his homework. Write the verb phrase with 'already'. (3 words)", ["has already finished", "already has finished"], "Present Perfect with already."),
]
Q["E4"] = [
    C(1, "Look at those clouds! It ___ rain.", "is going to", ["will to", "is going", "goes to"], "Prediction from evidence → going to."),
    C(1, "I think it ___ rain tomorrow.", "will", ["is going to be", "would", "shall to"], "Opinion/prediction → will."),
    C(2, "We ___ to the cinema tonight. I've already bought the tickets.", "are going", ["will go", "go", "are go"], "Fixed plan → Present Continuous."),
    C(2, "The train ___ at 9:15 tomorrow.", "leaves", ["will leaving", "is leaving", "left"], "Timetable → Present Simple."),
    C(3, "Which sentence expresses a spontaneous decision?", "I'll open the window.", ["I'm going to open the window.", "I'm opening the window tomorrow.", "I open the window."], "Spontaneous decision → will."),
    O(3, "Complete: By next year, I ___ (finish) school. (will + verb, 3 words)", ["will have finished"], "Future Perfect."),
]
Q["E5"] = [
    C(1, "She is ___ engineer.", "an", ["a", "the", "—"], "Vowel sound → an."),
    C(1, "___ sun rises in the east.", "The", ["A", "An", "—"], "Unique thing → the."),
    C(2, "I like ___ music.", "—", ["a", "an", "the"], "General uncountable noun: zero article."),
    C(2, "He plays ___ guitar very well.", "the", ["a", "an", "—"], "Musical instruments → the."),
    C(3, "Which sentence uses articles and transport words correctly?", "She goes to school by bus.", ["She goes to the school by the bus.", "She goes to a school by bus.", "She goes to school by a bus."], "by + transport: no article."),
    O(3, "Write the missing article (a/an/the/—): ___ Pacific Ocean is the largest ocean.", ["the", "The"], "Oceans take the."),
]
Q["E6"] = [
    C(1, "The lesson starts ___ 9 o'clock.", "at", ["in", "on", "to"], "at + exact time."),
    C(1, "My birthday is ___ May.", "in", ["on", "at", "of"], "in + month."),
    C(2, "We have a test ___ Monday.", "on", ["in", "at", "by"], "on + day."),
    C(2, "She is sitting ___ the window.", "next to", ["at to", "in to", "among"], "Position: next to."),
    C(3, "He lives ___ 25 Main Street.", "at", ["in", "on", "to"], "at + street number."),
    O(3, "Complete: I was born ___ 2005. (one word)", ["in"], "in + year."),
    M(2, [("in", "the morning"), ("on", "Friday"), ("at", "night")], "Prepositions of time."),
]
Q["E7"] = [
    C(1, "This book is ___ than that one.", "better", ["more good", "gooder", "best"], "good – better – best."),
    C(1, "Mount Everest is the ___ mountain in the world.", "highest", ["higher", "most high", "more high"], "Superlative: the highest."),
    C(2, "She is ___ than her sister.", "more intelligent", ["intelligenter", "most intelligent", "more intelligently"], "Long adjectives → more."),
    C(2, "This is the ___ film I have ever seen.", "most boring", ["more boring", "boringest", "most bored"], "Superlative of long adjective."),
    C(3, "Which sentence compares two equal things correctly?", "He runs as fast as his brother.", ["He runs as faster as his brother.", "He runs so fast than his brother.", "He runs more fast as his brother."], "as ... as."),
    O(3, "Write the comparative of 'bad'. (one word)", ["worse"], "bad – worse – worst."),
]
Q["E8"] = [
    C(1, "You ___ wear a seat belt. It's the law.", "must", ["can", "may", "would"], "Obligation → must."),
    C(1, "He ___ swim when he was five.", "could", ["can", "must", "should"], "Past ability → could."),
    C(2, "You look tired. You ___ take a rest.", "should", ["must to", "would to", "can"], "Advice → should."),
    C(2, "___ I open the window? (polite request)", "May", ["Must", "Should", "Need"], "May I...? polite."),
    C(3, "'You mustn't smoke here' means:", "It is forbidden.", ["It is not necessary.", "It is possible.", "It is a good idea."], "mustn't = prohibition."),
    O(3, "Complete: You ___ come tomorrow if you don't want to. (no necessity, 2 words)", ["don't have to", "needn't", "do not have to"], "Absence of necessity."),
]
Q["E9"] = [
    C(1, "There isn't ___ milk in the fridge.", "any", ["some", "many", "a"], "Negative uncountable → any."),
    C(1, "How ___ students are there in your class?", "many", ["much", "a lot", "little"], "Countable → many."),
    C(2, "I need ___ sugar for the cake.", "some", ["any", "many", "a few"], "Positive uncountable → some."),
    C(2, "We have ___ time. Let's hurry!", "little", ["a few", "few", "many"], "little = almost no (uncountable)."),
    C(3, "Which word is uncountable?", "advice", ["suggestion", "idea", "opinion"], "Advice is uncountable."),
    O(3, "Complete: She has ___ friends in this city, so she feels lonely. (few/a few)", ["few"], "few = almost none."),
]
Q["E10"] = [
    C(1, "You live in Tashkent, ___?", "don't you", ["do you", "aren't you", "didn't you"], "Positive statement → negative tag."),
    C(1, "She can swim, ___?", "can't she", ["isn't she", "doesn't she", "can she"], "Tag repeats the modal."),
    C(2, "Which question is correct?", "Where did you go yesterday?", ["Where you went yesterday?", "Where did you went yesterday?", "Where went you yesterday?"], "Wh- + did + subject + base verb."),
    C(2, "Let's go out, ___?", "shall we", ["will we", "don't we", "do we"], "Let's → shall we."),
    C(3, "Choose the correct indirect question.", "Do you know where he lives?", ["Do you know where does he live?", "Do you know where he does live?", "Do you know where lives he?"], "Word order is like a statement."),
    O(3, "Complete the tag: They aren't ready, ___? (2 words)", ["are they"], "Negative statement → positive tag."),
]
Q["E11"] = [
    C(1, "The window ___ by the boy yesterday.", "was broken", ["broke", "is broken", "has broke"], "Past passive: was + V3."),
    C(1, "English ___ all over the world.", "is spoken", ["speaks", "is speak", "spoke"], "Present passive."),
    C(2, "The letter ___ already ___.", "has / been sent", ["is / sent", "was / send", "have / sent"], "Present Perfect passive."),
    C(2, "Change to passive: They are building a new bridge.", "A new bridge is being built.", ["A new bridge is built.", "A new bridge was being build.", "A new bridge builds."], "Present Continuous passive."),
    C(3, "Which sentence is passive?", "The cake was eaten by the children.", ["The children ate the cake.", "The children are eating cake.", "The children have eaten the cake."], "was eaten by..."),
    O(3, "Write the passive: 'Someone stole my bike.' → My bike ___. (3 words)", ["was stolen", "was stolen."], "Past passive of steal."),
]
Q["E12"] = [
    C(1, "If it rains, we ___ at home.", "will stay", ["would stay", "stayed", "stay will"], "First conditional."),
    C(1, "If you heat ice, it ___.", "melts", ["will melting", "would melt", "melted"], "Zero conditional (general truth)."),
    C(2, "If I ___ rich, I would travel the world.", "were", ["am", "will be", "would be"], "Second conditional: if + past."),
    C(2, "She ___ help you if you asked her.", "would", ["will", "can", "did"], "Second conditional result clause."),
    C(3, "Which sentence is the First Conditional?", "If he studies hard, he will pass the exam.", ["If he studied hard, he would pass.", "If he had studied, he would have passed.", "If he studies, he passes always."], "if + present, will + base."),
    O(3, "Complete: If I ___ (be) you, I would apologise. (one word)", ["were", "was"], "If I were you..."),
]
Q["E13"] = [
    C(2, "If she ___ harder, she would have passed the exam.", "had studied", ["studied", "has studied", "would study"], "Third conditional: if + past perfect."),
    C(2, "If I had known, I ___ you.", "would have told", ["would tell", "will tell", "had told"], "Third conditional result."),
    C(3, "If he ___ earlier, he wouldn't be late now. (mixed)", "had left", ["left", "leaves", "would leave"], "Mixed conditional: past condition → present result."),
    C(3, "Which sentence expresses regret about the past?", "If only I had listened to him.", ["If only I listen to him.", "If only I will listen.", "If only I listened tomorrow."], "If only + past perfect."),
    C(3, "Choose the correct form: Unless you ___, you will miss the bus.", "hurry", ["don't hurry", "will hurry", "hurried"], "Unless = if ... not, so no negative."),
    O(3, "Complete: I wouldn't have gone if I ___ (know). (2 words)", ["had known"], "Third conditional."),
]
Q["E14"] = [
    C(1, "He said, 'I am tired.' → He said that he ___ tired.", "was", ["is", "were", "has been"], "Backshift: am → was."),
    C(1, "She said, 'I will come.' → She said that she ___ come.", "would", ["will", "can", "did"], "will → would."),
    C(2, "'Do you like pizza?' he asked. → He asked me ___ pizza.", "if I liked", ["do I like", "if did I like", "that I like"], "Yes/no question → if + statement order."),
    C(2, "'Don't touch it,' she told me. → She told me ___ it.", "not to touch", ["don't touch", "to not touched", "not touching"], "Imperative → (not) to + verb."),
    C(3, "'I have finished,' he said. → He said he ___.", "had finished", ["has finished", "finished has", "would finish"], "Present perfect → past perfect."),
    O(3, "Complete: 'I saw him yesterday.' → She said she ___ him the day before. (2 words)", ["had seen"], "Past simple → past perfect."),
]
Q["E15"] = [
    C(1, "The man ___ lives next door is a doctor.", "who", ["which", "whose", "whom"], "who for people (subject)."),
    C(1, "This is the book ___ I bought yesterday.", "which", ["who", "whose", "where"], "which for things."),
    C(2, "That is the girl ___ father is a pilot.", "whose", ["who", "which", "whom"], "whose = possession."),
    C(2, "This is the town ___ I was born.", "where", ["which", "who", "whose"], "where for places."),
    C(3, "Which sentence contains a non-defining relative clause?", "My brother, who lives in Samarkand, is a teacher.", ["The man who called is my uncle.", "The book that I read was great.", "I know the girl who won."], "Commas show extra information."),
    O(3, "Complete: The film ___ we watched last night was boring. (one word, may be omitted)", ["that", "which"], "that/which."),
]
Q["E16"] = [
    C(1, "She enjoys ___ books.", "reading", ["to read", "read", "reads"], "enjoy + gerund."),
    C(1, "I want ___ a doctor.", "to be", ["being", "be", "been"], "want + infinitive."),
    C(2, "He suggested ___ to the park.", "going", ["to go", "go", "went"], "suggest + gerund."),
    C(2, "She stopped ___ because she was tired. (she ended the activity)", "walking", ["to walk", "walk", "walked"], "stop doing."),
    C(3, "I clearly remember ___ the door before I left. (a memory of a past action)", "locking", ["to lock", "lock", "locked"], "remember + -ing = recall a past action."),
    O(3, "Complete: He is good at ___ (swim). (one word)", ["swimming"], "preposition + gerund."),
]
Q["E17"] = [
    C(1, "When I arrived, the film ___.", "had already started", ["already started", "has started", "was start"], "Earlier past action: past perfect."),
    C(2, "She was tired because she ___ all day.", "had been working", ["was worked", "has worked", "worked had"], "Past perfect continuous."),
    C(2, "By the time he came, we ___ dinner.", "had finished", ["finished", "have finished", "were finish"], "Past perfect."),
    C(3, "I ___ for two hours when she finally called.", "had been waiting", ["waited", "was waited", "have waited"], "Duration before a past moment."),
    C(3, "Which reported statement is correct?", "He said he had never seen such a thing.", ["He said he never saw has such a thing.", "He said he has never seen it before yesterday.", "He said he is never seeing such."], "Reported past perfect."),
    O(3, "Complete: After she ___ (leave), I went to bed. (2 words)", ["had left"], "After + past perfect."),
]
Q["E18"] = [
    C(1, "Please ___ your shoes before you enter.", "take off", ["put off", "give up", "look for"], "take off = remove clothes."),
    C(1, "I'm ___ my keys. Have you seen them?", "looking for", ["looking after", "looking up", "looking at"], "look for = search."),
    C(2, "He ___ smoking last year.", "gave up", ["gave in", "gave out", "gave off"], "give up = stop."),
    C(2, "The plane ___ at 8 a.m.", "took off", ["took in", "took after", "took over"], "take off = leave the ground."),
    C(3, "'Put off' in 'We put off the meeting' means:", "postponed", ["cancelled forever", "started", "attended"], "put off = postpone."),
    O(3, "Complete: She takes ___ her mother. (looks/behaves like) (one word)", ["after"], "take after = resemble."),
]
Q["E19"] = [
    C(1, "The opposite of 'happy' is ___.", "unhappy", ["dishappy", "inhappy", "nonhappy"], "un- prefix."),
    C(1, "A person who teaches is a ___.", "teacher", ["teachment", "teachful", "teachly"], "-er suffix for people."),
    C(2, "Choose the correct noun: 'to decide' → ___.", "decision", ["decide-ment", "decider", "decidion"], "decide → decision."),
    C(2, "Choose the adjective: 'success' → ___.", "successful", ["successing", "successly", "successment"], "-ful forms adjectives."),
    C(3, "'impossible' uses which prefix?", "im-", ["in-", "un-", "dis-"], "im- before p."),
    O(3, "Write the adverb of 'quick'. (one word)", ["quickly"], "-ly."),
]
Q["E20"] = [
    C(1, "I was tired, ___ I went to bed early.", "so", ["but", "although", "because"], "so = result."),
    C(1, "He stayed at home ___ it was raining.", "because", ["so", "but", "although"], "because = reason."),
    C(2, "___ it was cold, they played outside.", "Although", ["Because", "So", "Therefore"], "although = contrast."),
    C(2, "She is clever; ___, she is hard-working.", "moreover", ["however", "otherwise", "although"], "moreover = addition."),
    C(3, "Which linking word shows contrast?", "However", ["Moreover", "Therefore", "Furthermore"], "However = contrast."),
    O(3, "Complete: Hurry up, ___ you will miss the train. (one word, 'if not')", ["or", "otherwise"], "or / otherwise."),
]
