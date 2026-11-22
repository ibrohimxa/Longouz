"""v246: INGLIZ TILI — eng kam savolli grammatika mavzulariga yangi savollar va 8 ta YANGI mavzu.

DTM 2026 va milliy sertifikat (CEFR B1–C1) uslubida: bitta to'g'ri javob, 3 ta ishonarli xato variant, o'zbekcha izoh.
Har bir savol qo'lda tuzilgan va grammatik qoida bo'yicha tekshirilgan.
"""
from __future__ import annotations

from ._dsl import C, O

Q: dict[str, list] = {}

Q["E1"] = [
    C(1, "Water ___ at 100 degrees Celsius.", "boils", ["is boiling", "boil", "boiled"], "Umumiy haqiqat — Present Simple."),
    C(1, "Look! The baby ___.", "is sleeping", ["sleeps", "sleep", "slept"], "Look! — hozir sodir bo'layotgan ish: Present Continuous."),
    C(2, "I ___ what you mean now.", "understand", ["am understanding", "understanding", "am understand"], "Stative fe'llar (understand, know, believe) odatda Continuous'da ishlatilmaydi."),
    C(2, "She usually ___ to work, but this week she ___ the bus.", "walks / is taking", ["is walking / takes", "walk / takes", "walks / take"], "Odat — Present Simple; vaqtinchalik holat (this week) — Present Continuous."),
    C(2, "How often ___ your grandparents?", "do you visit", ["are you visiting", "you visit", "visit you"], "How often — odat, Present Simple savol: do + ega + fe'l."),
    C(3, "This soup ___ delicious. What ___ in it?", "tastes / are you putting", ["is tasting / do you put", "tastes / do you putting", "is tasting / are you put"], "taste (ta'mi bor) — stative; hozir qo'shilayotgan narsa — Continuous."),
    O(2, "Complete: He ___ (not / like) coffee. (2 words)", ["doesn't like", "does not like"], "3-shaxs birlik inkor: doesn't + V1."),
]

Q["E4"] = [
    C(1, "Look at those dark clouds! It ___ rain.", "is going to", ["will", "rains", "is raining to"], "Hozirgi dalilga asoslangan bashorat — be going to."),
    C(1, "A: The phone is ringing. B: I ___ answer it.", "will", ["am going to", "answer", "am answering"], "Gapirish paytida qabul qilingan qaror — will."),
    C(2, "We ___ our grandparents next Sunday. We bought the tickets yesterday.", "are visiting", ["will visit", "visit", "visited"], "Aniq kelishilgan reja — Present Continuous."),
    C(2, "The train ___ at 7:45 tomorrow morning.", "leaves", ["is leaving to", "will leaving", "leave"], "Jadval bo'yicha voqealar — Present Simple."),
    C(2, "I think Uzbekistan ___ the match.", "will win", ["is winning", "wins", "is going win"], "I think — fikrga asoslangan bashorat: will."),
    C(3, "By the time you arrive, I ___ dinner.", "will have cooked", ["will cook", "cook", "am cooking"], "By the time — kelajakdagi nuqtagacha tugaydi: Future Perfect."),
    C(3, "This time tomorrow we ___ over the Atlantic.", "will be flying", ["will fly", "fly", "are flying to"], "Kelajakdagi aniq paytda davom etayotgan ish — Future Continuous."),
]

Q["E5"] = [
    C(1, "She is ___ honest woman.", "an", ["a", "the", "—"], "honest — h talaffuz qilinmaydi, unli tovush: an."),
    C(1, "He wants to be ___ engineer.", "an", ["a", "the", "—"], "Kasb + unli tovush: an engineer."),
    C(1, "___ sun rises in the east.", "The", ["A", "An", "—"], "Yagona narsa — the."),
    C(2, "I play ___ piano, and my brother plays ___ football.", "the / —", ["— / the", "a / the", "the / a"], "Musiqa asbobi — the; sport turi — artiklsiz."),
    C(2, "She goes to ___ school by bus.", "—", ["the", "a", "an"], "O'qish maqsadida: go to school — artiklsiz."),
    C(2, "That was ___ useful lesson.", "a", ["an", "the", "—"], "useful [ju:] — undosh tovush bilan boshlanadi: a."),
    C(3, "___ Nile is the longest river in ___ Africa.", "The / —", ["— / the", "The / the", "A / —"], "Daryolar — the; qit'alar — artiklsiz."),
    C(3, "He is ___ best student in our class.", "the", ["a", "an", "—"], "Orttirma daraja — the."),
    O(2, "Complete with an article: I saw ___ elephant at the zoo. (one word)", ["an"], "elephant — unli tovush."),
]

Q["E8"] = [
    C(1, "You ___ wear a seat belt. It's the law.", "must", ["might", "could", "would"], "Qonun/majburiyat — must."),
    C(1, "___ I open the window? It's hot.", "May", ["Must", "Should to", "Have"], "Ruxsat so'rash — May I...?"),
    C(2, "You ___ bring food — there will be plenty at the party.", "don't have to", ["mustn't", "can't", "shouldn't to"], "Zarurat yo'q — don't have to; mustn't — taqiq."),
    C(2, "You ___ smoke here. It's a hospital.", "mustn't", ["don't have to", "needn't", "may not to"], "Taqiq — mustn't."),
    C(2, "She ___ speak three languages when she was ten.", "could", ["can", "must", "should"], "O'tmishdagi qobiliyat — could."),
    C(3, "He isn't answering. He ___ be asleep.", "might", ["must to", "can", "should"], "Ehtimol — might/may/could."),
    C(3, "The lights are off. They ___ be at home.", "can't", ["mustn't", "needn't", "shouldn't"], "Mantiqiy inkor xulosa — can't."),
    C(3, "You ___ have told me earlier! Now it's too late.", "should", ["must", "can", "would"], "should have + V3 — o'tmishdagi afsus/tanqid."),
    O(3, "Complete: You look tired. You ___ go to bed early. (one word — advice)", ["should"], "Maslahat — should."),
]

Q["E9"] = [
    C(1, "How ___ money do you have?", "much", ["many", "a lot", "few"], "money — sanalmaydigan: how much."),
    C(1, "There are ___ apples in the fridge.", "some", ["any", "much", "a little"], "Darak gap, ko'plik — some."),
    C(2, "I have ___ friends here, so I'm not lonely.", "a few", ["few", "a little", "little"], "a few — bir nechta (ijobiy); few — juda kam (salbiy)."),
    C(2, "Could I have ___ information about the course?", "some", ["an", "a few", "many"], "information — sanalmaydigan; taklif/so'rovda some."),
    C(2, "There isn't ___ milk left.", "any", ["some", "many", "few"], "Inkor gap — any."),
    C(3, "She gave me two ___ of advice.", "pieces", ["advices", "items advices", "piece"], "advice sanalmaydi — a piece/two pieces of advice."),
    C(3, "___ of the students passed the exam — the teacher was very happy.", "Most", ["Much", "Little", "A little"], "Most of + sanaladigan ko'plik."),
    O(2, "Complete: We have very ___ time — hurry up! (one word, negative meaning)", ["little"], "little + sanalmaydigan — juda kam."),
]

Q["E10"] = [
    C(1, "She lives in Tashkent, ___?", "doesn't she", ["isn't she", "does she", "don't she"], "Darak gap — inkor tag; Present Simple: doesn't she."),
    C(1, "You aren't tired, ___?", "are you", ["aren't you", "do you", "don't you"], "Inkor gap — tasdiq tag."),
    C(2, "Let's go to the cinema, ___?", "shall we", ["will we", "don't we", "let we"], "Let's... — shall we?"),
    C(2, "I'm late, ___?", "aren't I", ["am not I", "isn't I", "don't I"], "I am... — aren't I?"),
    C(2, "Who ___ this window?", "broke", ["did break", "did broke", "breaked"], "Ega haqida savol (Who) — yordamchi fe'lsiz: Who broke?"),
    C(3, "Nobody called, ___?", "did they", ["didn't they", "did he", "didn't he"], "Nobody — inkor ma'no; tag tasdiq: did they."),
    C(3, "Open the door, ___?", "will you", ["do you", "don't you", "shall you"], "Buyruq gap — will you / would you."),
    O(2, "Make a question: She bought a new car. → What ___ she buy? (one word)", ["did"], "Past Simple savol: did + V1."),
]

Q["E11"] = [
    C(1, "This book ___ by Abdulla Qodiriy.", "was written", ["wrote", "is writing", "has write"], "O'tgan zamon passiv: was + V3."),
    C(1, "Rice ___ in many Asian countries.", "is grown", ["grows", "is growing by", "grew"], "Umumiy fakt — Present Simple passive."),
    C(2, "The new school ___ next year.", "will be opened", ["will open by", "is opening by", "opened"], "Future passive: will be + V3."),
    C(2, "My car ___ at the moment, so I'm taking the bus.", "is being repaired", ["is repaired", "repairs", "has repairing"], "Hozir davom etayotgan passiv — is being + V3."),
    C(2, "The thieves ___ yet.", "haven't been caught", ["didn't catch", "haven't caught", "weren't catch"], "Present Perfect passive inkor."),
    C(3, "The bridge ___ when the earthquake happened.", "was being built", ["was built", "has been built", "built"], "Past Continuous passive: was being + V3."),
    C(3, "It ___ that the city was founded 2,500 years ago.", "is believed", ["believes", "is believing", "believed by"], "It is said/believed that... — shaxssiz passiv."),
    C(3, "The documents must ___ before Friday.", "be signed", ["sign", "signed", "being signed"], "Modal + be + V3."),
    O(3, "Passive: They will finish the project soon. → The project will ___ soon. (2 words)", ["be finished"], "will + be + V3."),
]

Q["E12"] = [
    C(1, "If you heat ice, it ___.", "melts", ["will melt", "melted", "would melt"], "Zero conditional — umumiy haqiqat: Present + Present."),
    C(1, "If it rains tomorrow, we ___ at home.", "will stay", ["would stay", "stayed", "stay to"], "First conditional: If + Present, will + V1."),
    C(2, "If I ___ rich, I would travel around the world.", "were", ["am", "will be", "had been"], "Second conditional: If + Past Simple (were)."),
    C(2, "What would you do if you ___ a lion in the street?", "saw", ["see", "will see", "had see"], "Second conditional — xayoliy vaziyat."),
    C(2, "Unless you ___ harder, you will fail.", "study", ["will study", "don't study", "studied"], "Unless = if not; Present Simple."),
    C(3, "If I ___ you, I wouldn't sign that contract.", "were", ["am", "was being", "would be"], "Maslahat: If I were you..."),
    C(3, "I'll lend you the book as long as you ___ it back on Monday.", "bring", ["will bring", "brought", "would bring"], "as long as — shart; Present Simple."),
    O(2, "Complete: If she ___ (call), tell her I'm out. (one word)", ["calls"], "First conditional, 3-shaxs: calls."),
]

Q["E13"] = [
    C(2, "If we had left earlier, we ___ the train.", "wouldn't have missed", ["wouldn't miss", "didn't miss", "won't have missed"], "Third conditional: would have + V3."),
    C(2, "If she ___ harder, she would have passed the exam.", "had studied", ["studied", "has studied", "would study"], "Third conditional: If + Past Perfect."),
    C(3, "If I had taken the job, I ___ in London now.", "would be living", ["would have lived", "will live", "had lived"], "Mixed: o'tmishdagi shart → hozirgi natija."),
    C(3, "If he weren't so lazy, he ___ the exam last week.", "would have passed", ["would pass", "passed", "had passed"], "Mixed: hozirgi xususiyat → o'tmishdagi natija."),
    C(3, "___ I known about the problem, I would have helped.", "Had", ["If", "Have", "Did"], "Inversiya: Had I known = If I had known."),
    C(3, "We would have won ___ our goalkeeper's mistake.", "but for", ["unless", "if", "in case"], "but for = agar ... bo'lmaganida (ot bilan)."),
    O(3, "Complete: If you had asked me, I ___ have helped you. (one word)", ["would", "could"], "would/could have + V3."),
]

Q["E14"] = [
    C(1, "He said, \"I am tired.\" → He said that he ___ tired.", "was", ["is", "were", "has been"], "Reported speech: am → was."),
    C(2, "She said, \"I will call you.\" → She said that she ___ call me.", "would", ["will", "shall", "is going"], "will → would."),
    C(2, "\"Where do you live?\" he asked. → He asked me where ___.", "I lived", ["did I live", "do I live", "I live"], "Ko'chirma savolda so'z tartibi darak: ega + fe'l."),
    C(2, "\"Don't touch it!\" she said. → She told me ___ it.", "not to touch", ["don't touch", "to not touching", "not touch"], "Buyruq inkori: told sb not to + V1."),
    C(3, "\"I saw him yesterday,\" she said. → She said she ___ him the day before.", "had seen", ["saw", "has seen", "sees"], "Past Simple → Past Perfect; yesterday → the day before."),
    C(3, "He asked me ___ I could swim.", "if", ["that", "what", "do"], "Ha/yo'q savol — if/whether."),
    C(3, "\"Let's go out,\" she said. → She ___ going out.", "suggested", ["told", "said us", "asked to"], "Let's → suggest + -ing."),
    O(3, "\"I can drive,\" he said. → He said he ___ drive. (one word)", ["could"], "can → could."),
]

Q["E15"] = [
    C(1, "The man ___ lives next door is a doctor.", "who", ["which", "whose", "where"], "Shaxs — who/that."),
    C(1, "This is the house ___ I was born.", "where", ["which", "who", "whose"], "Joy — where (= in which)."),
    C(2, "That's the girl ___ father is a pilot.", "whose", ["who", "who's", "which"], "Egalik — whose."),
    C(2, "The book ___ you gave me is very interesting.", "that", ["who", "whose", "what"], "Narsa — which/that."),
    C(2, "I don't remember the day ___ we first met.", "when", ["which", "where", "whom"], "Vaqt — when."),
    C(3, "My brother, ___ lives in Samarkand, is an architect.", "who", ["that", "which", "whom"], "Ajratilgan (non-defining) gapda that ishlatilmaydi."),
    C(3, "He passed the exam, ___ surprised everyone.", "which", ["that", "what", "who"], "Butun gapga ishora — which."),
    C(3, "The woman to ___ I spoke was very kind.", "whom", ["who", "which", "that"], "Predlogdan keyin shaxs — whom."),
    O(2, "Complete: Is this the bag ___ you lost? (one word: which/that)", ["which", "that"], "Narsa — which yoki that."),
]

Q["E16"] = [
    C(1, "I'm looking forward to ___ you.", "seeing", ["see", "to see", "saw"], "look forward to + -ing (to — predlog)."),
    C(1, "He decided ___ a new car.", "to buy", ["buying", "buy", "bought"], "decide + to-infinitive."),
    C(2, "Would you mind ___ the window?", "opening", ["to open", "open", "opened"], "mind + -ing."),
    C(2, "She avoided ___ him.", "meeting", ["to meet", "meet", "met"], "avoid + -ing."),
    C(2, "I stopped ___ some water because I was thirsty.", "to buy", ["buying", "buy", "bought"], "stop + to = bir ishni qilish uchun to'xtash."),
    C(3, "I'll never forget ___ the Registan for the first time.", "seeing", ["to see", "see", "having see"], "forget + -ing — o'tmishdagi xotira."),
    C(3, "Don't forget ___ the lights when you leave.", "to turn off", ["turning off", "turn off", "turned off"], "forget + to — bajarilishi kerak bo'lgan ish."),
    C(3, "He is used to ___ up early.", "getting", ["get", "got", "to get"], "be used to + -ing — ko'nikkan."),
    O(2, "Complete: It's no use ___ (cry) over spilt milk. (one word)", ["crying"], "It's no use + -ing."),
]

Q["E18"] = [
    C(1, "Please ___ your shoes before you come in.", "take off", ["take on", "take up", "take after"], "take off — yechmoq."),
    C(1, "Can you ___ my cat while I'm away?", "look after", ["look for", "look up", "look into"], "look after — qaramoq."),
    C(2, "I'm ___ my keys. Have you seen them?", "looking for", ["looking after", "looking up", "looking out"], "look for — qidirmoq."),
    C(2, "She ___ her mother — they have the same eyes.", "takes after", ["takes off", "takes up", "takes in"], "take after — o'xshamoq (ota-onaga)."),
    C(2, "The meeting was ___ because the manager was ill.", "called off", ["called up", "called in", "called back"], "call off — bekor qilmoq."),
    C(3, "We've ___ milk. Can you buy some?", "run out of", ["run into", "run over", "run away from"], "run out of — tugab qolmoq."),
    C(3, "I can't ___ this noise any longer!", "put up with", ["put off", "put on", "put away"], "put up with — chidamoq."),
    C(3, "The plane ___ at 6 a.m.", "took off", ["took up", "took after", "took over"], "take off — (samolyot) ko'tarilmoq."),
    O(3, "Complete: Don't give ___! You can do it. (one word)", ["up"], "give up — taslim bo'lmoq."),
]

Q["E19"] = [
    C(1, "The opposite of 'happy' is ___.", "unhappy", ["dishappy", "inhappy", "nonhappy"], "un- prefiksi."),
    C(1, "A person who teaches is a ___.", "teacher", ["teachist", "teachian", "teachor"], "-er — kasb egasi."),
    C(2, "The opposite of 'possible' is ___.", "impossible", ["unpossible", "inpossible", "dispossible"], "p dan oldin im-."),
    C(2, "Choose the noun: She showed great ___.", "kindness", ["kind", "kindly", "kinder"], "-ness — ot yasaydi."),
    C(2, "The opposite of 'agree' is ___.", "disagree", ["unagree", "misagree", "inagree"], "dis- prefiksi."),
    C(3, "Choose the adjective: It was a very ___ decision.", "responsible", ["responsibility", "responsibly", "response"], "-ible — sifat."),
    C(3, "He ___ the instructions and did everything wrong.", "misunderstood", ["disunderstood", "ununderstood", "overunderstood"], "mis- — noto'g'ri."),
    C(3, "The government plans to ___ the education system.", "modernize", ["modernity", "modernly", "modernization"], "-ize — fe'l yasaydi."),
    O(2, "Make a noun from 'decide': ___ (one word)", ["decision"], "decide → decision."),
]

Q["E20"] = [
    C(1, "I was tired, ___ I went to bed early.", "so", ["but", "because", "although"], "Natija — so."),
    C(1, "She stayed at home ___ she was ill.", "because", ["so", "but", "however"], "Sabab — because."),
    C(2, "___ it was raining, we went for a walk.", "Although", ["Because", "Despite", "So"], "Although + gap — qarama-qarshilik."),
    C(2, "He is rich. ___, he isn't happy.", "However", ["Therefore", "Moreover", "Because"], "However — biroq (yangi gap boshida)."),
    C(2, "The hotel was cheap. ___, it was very clean.", "Moreover", ["However", "Otherwise", "Instead"], "Moreover — bundan tashqari (qo'shimcha)."),
    C(3, "___ the bad weather, the flight left on time.", "Despite", ["Although", "Even though", "However"], "Despite + ot."),
    C(3, "Hurry up, ___ you'll miss the bus.", "otherwise", ["therefore", "moreover", "whereas"], "otherwise — aks holda."),
    C(3, "Some people like tea, ___ others prefer coffee.", "whereas", ["therefore", "because", "unless"], "whereas — qiyoslash/zidlik."),
    O(3, "Complete: He trained hard; ___, he won the race. (one word, result)", ["therefore", "consequently", "thus"], "Natija bog'lovchisi."),
]

Q["E27"] = [
    C(2, "It's raining cats and ___.", "dogs", ["mice", "birds", "cows"], "Idioma — juda kuchli yomg'ir."),
    C(2, "Choose the correct collocation: ___ a decision", "make", ["do", "take up", "have"], "make a decision."),
    C(2, "Choose the correct collocation: ___ homework", "do", ["make", "take", "get"], "do homework."),
    C(3, "'Break the ice' means ___.", "to start a conversation in an awkward situation", ["to destroy something cold", "to be very angry", "to finish a project"], "Tanishuvdagi noqulaylikni yo'qotish."),
    C(3, "'A piece of cake' means something is ___.", "very easy", ["very tasty", "very small", "very expensive"], "Juda oson."),
    C(3, "'Once in a blue moon' means ___.", "very rarely", ["every month", "at night", "very soon"], "Juda kam."),
    C(3, "Choose the strong collocation: ___ rain", "heavy", ["strong", "big", "hard"], "heavy rain — kuchli yomg'ir."),
    C(3, "'To hit the books' means ___.", "to study hard", ["to throw books", "to buy books", "to stop studying"], "Jiddiy o'qimoq."),
    O(3, "Complete the idiom: Better late than ___. (one word)", ["never"], "Kech bo'lsa ham, umuman bo'lmaganidan yaxshi."),
]

Q["E32"] = [
    C(3, "Never ___ such a beautiful place.", "have I seen", ["I have seen", "I saw", "did I saw"], "Inkor ravishdan keyin inversiya."),
    C(3, "Not only ___ late, but he also forgot his books.", "was he", ["he was", "he is", "did he was"], "Not only... — inversiya."),
    C(3, "Hardly ___ arrived when it started to rain.", "had we", ["we had", "did we", "we have"], "Hardly had... when."),
    C(3, "Only after the exam ___ how easy it was.", "did I realize", ["I realized", "I did realize", "realized I"], "Only after... — inversiya: did + ega + V1."),
    C(3, "Little ___ that he was being watched.", "did he know", ["he knew", "knew he", "he did know"], "Little did he know."),
    C(3, "It was Ali ___ broke the window.", "who", ["which", "whom", "what"], "Cleft sentence: It was... who."),
    C(3, "What I need ___ a long holiday.", "is", ["are", "be", "being"], "What-cleft: What I need is..."),
    O(3, "Complete: Rarely ___ he go to the theatre. (one word)", ["does"], "Rarely + does + ega + V1."),
]

Q["E33"] = [
    C(2, "I wish I ___ taller.", "were", ["am", "will be", "would be"], "Hozirgi orzu: wish + Past (were)."),
    C(2, "I wish I ___ to the party yesterday.", "had gone", ["went", "have gone", "would go"], "O'tmishdagi afsus: wish + Past Perfect."),
    C(3, "I wish you ___ making that noise. It's annoying!", "would stop", ["stopped", "had stopped", "stop"], "Boshqaning harakatidan norozilik: wish + would."),
    C(3, "If only I ___ the answer now!", "knew", ["know", "had known", "will know"], "If only + Past — hozirgi orzu."),
    C(3, "She wishes she ___ speak Chinese.", "could", ["can", "will", "may"], "Qobiliyat haqida orzu — could."),
    C(3, "It's time we ___ home.", "went", ["go", "will go", "have gone"], "It's time + Past Simple."),
    O(3, "Complete: I wish I ___ (not / say) that yesterday. (3 words)", ["hadn't said", "had not said"], "wish + Past Perfect inkor."),
]

Q["E34"] = [
    C(1, "Everybody ___ the answer.", "knows", ["know", "are knowing", "have known"], "Everybody — birlik."),
    C(2, "The news ___ very good today.", "is", ["are", "were", "have been"], "news — sanalmaydigan, birlik."),
    C(2, "Neither my brother nor my parents ___ at home.", "are", ["is", "was", "has"], "Neither...nor — yaqinroq egaga moslashadi (parents)."),
    C(2, "Mathematics ___ my favourite subject.", "is", ["are", "were", "be"], "Fan nomlari (-ics) — birlik."),
    C(3, "A number of students ___ absent today.", "are", ["is", "was", "has been"], "A number of + ko'plik — ko'plik fe'l."),
    C(3, "The number of cars ___ increasing.", "is", ["are", "were", "have been"], "The number of — birlik."),
    C(3, "Each of the boys ___ a bike.", "has", ["have", "are having", "were"], "Each of — birlik."),
    O(2, "Complete: The police ___ looking for the thief. (one word)", ["are"], "police — har doim ko'plik."),
]

Q["E38"] = [
    C(1, "Choose the correct spelling of the word meaning «zarur»:", "necessary", ["neccessary", "necesary", "neccesary"], "necessary — bitta c, ikkita s."),
    C(2, "Choose the correct spelling of the word meaning «boshlanish»:", "beginning", ["begining", "beggining", "beginnig"], "begin → beginning (n ikkilanadi)."),
    C(2, "Choose the correct spelling of the word meaning «olmoq, qabul qilmoq»:", "receive", ["recieve", "receeve", "resieve"], "i before e, except after c."),
    C(2, "Which sentence is punctuated correctly?", "It's a nice day, isn't it?", ["Its a nice day, isn't it?", "It's a nice day isn't it.", "Its' a nice day, isnt it?"], "It's = it is; tag oldidan vergul, oxirida so'roq."),
    C(3, "Choose the correct spelling of the word meaning «turar joy»:", "accommodation", ["accomodation", "acommodation", "accommodaton"], "cc va mm."),
    C(3, "Which sentence uses the apostrophe correctly?", "The children's toys are in the box.", ["The childrens' toys are in the box.", "The childrens toys are in the box.", "The children toys' are in the box."], "children — ko'plik, -s siz: children's."),
    O(2, "Write the plural of 'city'. (one word)", ["cities"], "Undosh + y → ies."),
]

Q["E39"] = [
    C(2, "She saved money ___ buy a new laptop.", "in order to", ["so that", "because", "due to"], "Maqsad + fe'l — in order to."),
    C(2, "The match was cancelled ___ the rain.", "because of", ["because", "so that", "although"], "because of + ot."),
    C(3, "He spoke slowly ___ everyone could understand.", "so that", ["in order to", "due to", "because of"], "so that + gap — maqsad."),
    C(3, "The flight was delayed ___ fog.", "owing to", ["so as", "in case", "so that"], "owing to/due to + ot."),
    C(3, "Take an umbrella ___ it rains.", "in case", ["so that", "unless", "because of"], "in case — ehtiyot uchun."),
    C(3, "He was ___ tired that he fell asleep at once.", "so", ["such", "too", "very"], "so + sifat + that."),
    O(3, "Complete: It was ___ a good film that we watched it twice. (one word)", ["such"], "such + a + sifat + ot + that."),
]

Q["E40"] = [
    C(3, "___ the letter, she started to cry.", "Having read", ["Read", "Had read", "Being read"], "Perfect participle — avval sodir bo'lgan ish."),
    C(3, "The man ___ next to me was very friendly.", "sitting", ["sat", "who sitting", "was sitting"], "Present participle — reduced relative."),
    C(3, "___ in 1991, the company now employs 500 people.", "Founded", ["Founding", "Having founding", "Being founded in"], "Past participle — passiv ma'no."),
    C(3, "___ tired, he went to bed early.", "Feeling", ["Felt", "Being felt", "Having feel"], "Sabab ma'nosidagi participle."),
    C(3, "Most of the people ___ to the party came.", "invited", ["inviting", "who invited", "were invited"], "Past participle — passiv: taklif qilinganlar."),
    C(3, "___ the bus, I realized I had left my phone at home.", "Getting on", ["Got on", "To get on", "Get on"], "Bir vaqtda sodir bo'lgan ish."),
    O(3, "Complete: ___ (not / know) what to do, she called her father. (2 words)", ["Not knowing"], "Inkor participle: Not + -ing."),
]

Q["E35"] = [
    C(1, "This is my book and that is ___.", "yours", ["your", "you", "yours'"], "Egalik olmoshi (mustaqil): yours."),
    C(1, "She hurt ___ while cooking.", "herself", ["her", "hers", "sheself"], "Refleksiv olmosh."),
    C(2, "The dog wagged ___ tail.", "its", ["it's", "it", "its'"], "its — egalik; it's = it is."),
    C(2, "Is this car ___ or theirs?", "ours", ["our", "us", "our's"], "Mustaqil egalik — ours."),
    C(2, "We enjoyed ___ at the party.", "ourselves", ["us", "ourself", "our"], "Refleksiv — ourselves."),
    C(3, "They help ___ — he helps her and she helps him.", "each other", ["themselves", "theirselves", "them"], "O'zaro — each other."),
    O(2, "Complete: Is this pen ___ (she)? (one word)", ["hers"], "she → hers."),
]

Q["E6"] = [
    C(1, "I was born ___ 2008.", "in", ["on", "at", "by"], "Yil — in."),
    C(1, "The lesson starts ___ 9 o'clock.", "at", ["in", "on", "by"], "Aniq soat — at."),
    C(1, "We have English ___ Monday.", "on", ["in", "at", "by"], "Hafta kuni — on."),
    C(2, "The picture is ___ the wall.", "on", ["in", "at", "under"], "Sirt ustida — on."),
    C(2, "I'll meet you ___ the bus stop.", "at", ["in", "on", "into"], "Aniq nuqta — at."),
    C(2, "She has lived here ___ 2015.", "since", ["for", "from", "during"], "Boshlanish nuqtasi — since."),
    C(3, "I'll finish the report ___ Friday at the latest.", "by", ["until", "since", "during"], "by — kechi bilan shu vaqtgacha."),
    C(3, "We stayed awake ___ the night.", "during", ["for", "since", "by"], "during + ot (davomida)."),
    O(2, "Complete: I'm good ___ maths. (one word)", ["at"], "good at."),
]

# ------------------------------------------------------------------ YANGI MAVZULAR
NEW_TOPICS = [
    ("E41", 8, "Used to / would / be used to", "pro"),
    ("E42", 7, "Too / enough / so / such", "free"),
    ("E43", 9, "Causative: have / get something done", "pro"),
    ("E44", 9, "Indirect questions va so'z tartibi", "pro"),
    ("E45", 7, "Make / do va boshqa kollokatsiyalar", "free"),
    ("E46", 8, "Lug'at: ish va iqtisod", "pro"),
    ("E47", 6, "Lug'at: tabiat va hayvonlar", "free"),
    ("E48", 10, "Qarama-qarshilik: although / despite / unless", "ultra"),
]

Q["E41"] = [
    C(1, "I ___ live in Bukhara when I was a child.", "used to", ["use to", "am used to", "was used"], "O'tmishdagi odat — used to + V1."),
    C(1, "Did you ___ play football at school?", "use to", ["used to", "using to", "used"], "Savolda: did + use to."),
    C(2, "She ___ coffee, but now she drinks tea.", "didn't use to drink", ["didn't used to drink", "wasn't used to drink", "doesn't use to drink"], "Inkor: didn't use to."),
    C(2, "I'm used to ___ in a big city now.", "living", ["live", "lived", "to live"], "be used to + -ing — ko'nikkan."),
    C(2, "It took me a long time to get used to ___ on the left.", "driving", ["drive", "drove", "to drive"], "get used to + -ing — ko'nikmoq."),
    C(3, "Every summer my grandfather ___ take us fishing.", "would", ["was used to", "used", "will"], "would — o'tmishdagi takroriy harakat."),
    C(3, "We ___ have a dog. (state, not repeated action)", "used to", ["would", "were used to", "use to"], "Holat (have, live, be) bilan would emas, used to."),
    C(3, "He isn't used to ___ so early.", "getting up", ["get up", "got up", "gets up"], "be used to + -ing."),
    C(2, "There ___ be a cinema here, but they knocked it down.", "used to", ["would", "is used to", "use to"], "O'tmishdagi holat."),
    O(2, "Complete: When I was young, I ___ to swim in the river every day. (one word)", ["used"], "used to + V1."),
]

Q["E42"] = [
    C(1, "The coffee is ___ hot to drink.", "too", ["enough", "so", "such"], "too + sifat + to — haddan ortiq."),
    C(1, "He isn't old ___ to drive.", "enough", ["too", "so", "such"], "sifat + enough."),
    C(2, "We don't have ___ chairs for everyone.", "enough", ["too", "too many", "so"], "enough + ot."),
    C(2, "It was ___ a boring film that I fell asleep.", "such", ["so", "too", "enough"], "such + a + sifat + ot."),
    C(2, "The test was ___ easy that everyone passed.", "so", ["such", "too", "enough"], "so + sifat + that."),
    C(2, "There were ___ many people in the room that I couldn't breathe.", "so", ["such", "too", "enough"], "so many/much + ot + that."),
    C(3, "The box was too heavy for me ___.", "to lift", ["lifting", "lift it", "to lift it up it"], "too ... for sb to + V1."),
    C(3, "She speaks English ___ to work as a translator.", "well enough", ["enough well", "too well", "so well"], "ravish + enough."),
    C(3, "They are ___ kind people!", "such", ["so", "such a", "too"], "such + ko'plik ot (artiklsiz)."),
    O(2, "Complete: I'm ___ tired to go out tonight. (one word)", ["too"], "too + sifat + to."),
]

Q["E43"] = [
    C(2, "I ___ my hair cut yesterday.", "had", ["did", "made", "was"], "have something done — xizmatni boshqaga bajartirmoq."),
    C(2, "We're having our house ___ next week.", "painted", ["paint", "to paint", "painting"], "have + obyekt + V3."),
    C(2, "You should get your eyes ___.", "tested", ["test", "to test", "testing"], "get + obyekt + V3."),
    C(3, "She had her bag ___ on the bus.", "stolen", ["steal", "stole", "stealing"], "Noxush hodisa ham: had her bag stolen."),
    C(3, "I'll get the mechanic ___ the car.", "to repair", ["repaired", "repair", "repairing"], "get + shaxs + to-infinitive."),
    C(3, "I had the plumber ___ the leak.", "fix", ["to fix", "fixed", "fixing"], "have + shaxs + V1."),
    C(3, "Where do you ___ your clothes cleaned?", "have", ["make", "do", "let"], "have something done — savolda."),
    O(3, "Complete: I need to ___ my phone repaired. (one word: have/get)", ["have", "get"], "have/get + obyekt + V3."),
]

Q["E44"] = [
    C(2, "Could you tell me where ___?", "the station is", ["is the station", "the station", "does the station"], "Indirect question — darak so'z tartibi."),
    C(2, "Do you know what time ___?", "the film starts", ["does the film start", "starts the film", "the film does start"], "Yordamchi do ishlatilmaydi."),
    C(2, "I wonder ___ she will come.", "if", ["that", "does", "what if"], "Ha/yo'q savol — if/whether."),
    C(3, "Can you tell me how much ___?", "this costs", ["does this cost", "costs this", "is this cost"], "Darak tartib: ega + fe'l."),
    C(3, "I'd like to know why ___ late.", "you were", ["were you", "did you be", "you did be"], "Indirect: why you were."),
    C(3, "Have you any idea who ___ this?", "wrote", ["did write", "did wrote", "has wrote"], "who — ega bo'lsa, tartib o'zgarmaydi."),
    C(3, "Choose the correct sentence:", "I don't know where he lives.", ["I don't know where does he live.", "I don't know where he does live?", "I don't know where lives he."], "Darak so'z tartibi."),
    O(3, "Complete: Do you know where ___ (she / work)? (2 words)", ["she works"], "Indirect question — she works."),
]

Q["E45"] = [
    C(1, "___ your bed every morning!", "Make", ["Do", "Take", "Have"], "make the bed."),
    C(1, "I need to ___ the shopping.", "do", ["make", "take", "play"], "do the shopping."),
    C(2, "Don't ___ a noise — the baby is sleeping.", "make", ["do", "give", "take"], "make a noise."),
    C(2, "Could you ___ me a favour?", "do", ["make", "give", "take"], "do sb a favour."),
    C(2, "She ___ a mistake in the test.", "made", ["did", "took", "had"], "make a mistake."),
    C(2, "I ___ my best, but I failed.", "did", ["made", "took", "gave"], "do one's best."),
    C(2, "Let's ___ a break.", "take", ["do", "make", "have to"], "take a break."),
    C(3, "The company ___ a huge profit last year.", "made", ["did", "took", "got done"], "make a profit."),
    C(3, "He ___ a promise and kept it.", "made", ["did", "gave up", "took"], "make a promise."),
    C(3, "Exercise ___ you good.", "does", ["makes", "takes", "gives up"], "do sb good."),
    O(2, "Complete: Please ___ your homework now. (one word)", ["do"], "do homework."),
]

Q["E46"] = [
    C(1, "A person who works for a company is an ___.", "employee", ["employer", "employment", "employ"], "employee — xodim; employer — ish beruvchi."),
    C(1, "The money you get for your work every month is your ___.", "salary", ["fare", "fee", "fine"], "salary — oylik maosh."),
    C(2, "If you lose your job, you become ___.", "unemployed", ["retired", "promoted", "hired"], "unemployed — ishsiz."),
    C(2, "She was ___ to manager after three years.", "promoted", ["fired", "applied", "retired"], "promote — lavozimini oshirmoq."),
    C(2, "To ask for a job officially is to ___ for it.", "apply", ["hire", "employ", "resign"], "apply for a job."),
    C(2, "Money you pay to the government is called ___.", "tax", ["salary", "profit", "wage"], "tax — soliq."),
    C(3, "A general increase in prices is called ___.", "inflation", ["recession", "investment", "income"], "inflation."),
    C(3, "He decided to ___ and start his own business.", "resign", ["promote", "hire", "employ"], "resign — ishdan o'z ixtiyori bilan ketmoq."),
    C(3, "The money a company earns after paying all costs is ___.", "profit", ["debt", "loss", "loan"], "profit — foyda."),
    O(2, "Write the opposite of 'export': ___ (one word)", ["import"], "export ↔ import."),
]

Q["E47"] = [
    C(1, "A very large area of trees is a ___.", "forest", ["desert", "field", "lake"], "forest — o'rmon."),
    C(1, "A young dog is called a ___.", "puppy", ["kitten", "calf", "cub"], "puppy — kuchukcha."),
    C(1, "Which animal is a mammal?", "whale", ["shark", "eagle", "snake"], "Kit — sutemizuvchi."),
    C(2, "Animals that eat only plants are ___.", "herbivores", ["carnivores", "predators", "insects"], "herbivore — o'txo'r."),
    C(2, "A hot, dry place with very little rain is a ___.", "desert", ["valley", "jungle", "swamp"], "desert — cho'l."),
    C(2, "Bees live in a ___.", "hive", ["nest", "den", "kennel"], "hive — asalari uyasi."),
    C(2, "Animals in danger of disappearing are ___ species.", "endangered", ["dangerous", "extinct", "domestic"], "endangered — yo'qolib ketish xavfida."),
    C(3, "The natural home of an animal is its ___.", "habitat", ["habit", "inhabitant", "harbour"], "habitat — yashash muhiti."),
    C(3, "Some birds ___ to warmer countries in winter.", "migrate", ["hibernate", "emigrate", "evaporate"], "migrate — ko'chib o'tmoq (qushlar)."),
    O(2, "Write the plural of 'mouse'. (one word)", ["mice"], "Noto'g'ri ko'plik: mouse → mice."),
]

Q["E48"] = [
    C(2, "___ he was tired, he finished the work.", "Although", ["Despite", "In spite", "However"], "Although + gap."),
    C(2, "___ being tired, he finished the work.", "Despite", ["Although", "Even though", "Unless"], "Despite + -ing/ot."),
    C(3, "In spite ___ the noise, I slept well.", "of", ["from", "that", "—"], "in spite of + ot."),
    C(3, "You won't pass ___ you study harder.", "unless", ["if", "although", "despite"], "unless = if not."),
    C(3, "___ she is rich, she lives in a small flat.", "Even though", ["Despite", "In spite of", "Because"], "Even though — kuchli qarama-qarshilik."),
    C(3, "He went to work ___ he had a cold.", "even though", ["despite", "in spite of", "unless"], "Gap bilan — even though."),
    C(3, "___ the fact that it was late, they kept working.", "Despite", ["Although", "Unless", "However"], "Despite the fact that + gap."),
    C(3, "Strange ___ it may seem, I've never seen the sea.", "as", ["though as", "like", "despite"], "Adjective + as + ega + fe'l — qarama-qarshilik."),
    O(3, "Complete: I'll go ___ it rains. (2 words — even if)", ["even if"], "even if — hatto ... bo'lsa ham."),
]


def extend(packs: list) -> list:
    from .gen_v242 import _add
    for pack in packs:
        if pack.get("subject") != "english" or "dtm" not in (pack.get("modes") or []):
            continue
        names = {t["name"] for t in pack["topics"]}
        codes = {t["code"] for t in pack["topics"]}
        for code, grade, name, tier in NEW_TOPICS:
            if name not in names and code not in codes:
                pack["topics"].append({"code": code, "grade": grade, "name": name, "tier": tier, "block": "mutaxassislik"})
        _add(pack, Q)
    return packs
