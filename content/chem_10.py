"""Kimyo: 10-sinf — organik kimya asoslari va uglevodorodlar."""
from ._dsl import C, O, M

Q = {}

Q["K10.1"] = [
    C(1, "Organik birikmalarda uglerod atomi nechanchi valentli bo'ladi?", "IV valentli", ["II valentli", "III valentli", "VI valentli"], "Uglerod har doim to'rt valentli."),
    C(1, "Organik birikmalarning kimyoviy tuzilish nazariyasini kim yaratgan?", "A.M. Butlerov", ["F. Vyoler", "A. Kekule", "J. Berselius"], "Butlerov, 1861-yil."),
    C(1, "sp³ gibridlanishda bog' burchagi qancha?", "109°28'", ["120°", "180°", "90°"], "Tetraedrik tuzilish (alkanlar)."),
    C(2, "Etilen (C₂H₄) molekulasidagi uglerod atomlari qanday gibridlanishga ega?", "sp²", ["sp³", "sp", "gibridlanmagan"], "Qo'shbog'li uglerod — sp²."),
    C(2, "Atsetilen molekulasi qanday shaklga ega?", "Chiziqli (180°)", ["Tekis uchburchak", "Tetraedr", "Piramida"], "sp gibridlanish."),
    C(2, "Metan molekulasining fazoviy shakli qanday?", "Tetraedr", ["Chiziqli", "Tekis kvadrat", "Piramida"], "109°28' burchak."),
    C(2, "Uchlamchi bog'da nechta σ va π bog' bor?", "1 ta σ va 2 ta π", ["2 ta σ va 1 ta π", "3 ta σ", "3 ta π"], "Har qanday karrali bog'da faqat bitta σ."),
    M(2, [("sp³ gibridlanish", "109°28'"), ("sp² gibridlanish", "120°"), ("sp gibridlanish", "180°")], "Gibridlanish va bog' burchaklari."),
    C(3, "Propin CH₃–C≡CH molekulasida qanday gibrid holatdagi uglerod atomlari bor?", "1 ta sp³ va 2 ta sp", ["2 ta sp³ va 1 ta sp", "1 ta sp³, 1 ta sp², 1 ta sp", "3 ta sp"], "CH₃ — sp³; C≡C ning ikkala atomi — sp."),
    C(3, "Propen CH₂=CH–CH₃ molekulasida nechta σ-bog' bor?", "8", ["9", "7", "6"], "C–H: 6 ta; C–C: 2 ta (jumladan C=C dagi σ) → 8; π — 1 ta."),
    O(3, "CH₃–CH=CH–C≡CH molekulasida nechta π-bog' bor? (faqat son)", ["3", "uch"], "Qo'shbog'da 1 ta, uchlamchi bog'da 2 ta π."),
]

Q["K10.2"] = [
    C(1, "Izomerlar qanday moddalar?", "Tarkibi bir xil, tuzilishi va xossalari turlicha", ["Tuzilishi bir xil, tarkibi turlicha", "Tarkibi va xossalari bir xil", "Faqat bir sinfga mansub"], "Izomeriya hodisasi."),
    C(1, "Sis-trans izomeriya qaysi izomeriya turiga kiradi?", "Fazoviy (geometrik)", ["Zanjir izomeriyasi", "Funksional guruh izomeriyasi", "Sinflararo izomeriya"], "Qo'shbog' atrofida aylanish yo'qligi sababli."),
    C(1, "Optik izomeriya molekulada nima bo'lganda yuzaga keladi?", "Asimmetrik (xiral) uglerod atomi", ["Qo'shbog'", "Uchlamchi bog'", "Halqa"], "To'rtta turli o'rinbosarli C*."),
    C(2, "C₄H₁₀ tarkibli alkanning nechta izomeri bor?", "2", ["1", "3", "4"], "n-butan va izobutan."),
    C(2, "Aldegidning sinflararo izomeri qaysi?", "Keton", ["Spirt", "Karbon kislota", "Efir"], "C₃H₆O: propanal va propanon."),
    C(2, "Karbon kislotaning sinflararo izomeri qaysi?", "Murakkab efir", ["Aldegid", "Oddiy efir", "Spirt"], "CH₃COOH va HCOOCH₃."),
    C(2, "Etanol (C₂H₅OH) ning sinflararo izomeri qaysi?", "Dimetil efir", ["Asetaldegid", "Sirka kislota", "Etilen glikol"], "C₂H₆O: CH₃CH₂OH va CH₃–O–CH₃."),
    M(2, [("Propen C₃H₆", "siklopropan"), ("Butin-1 C₄H₆", "butadien-1,3"), ("Etanol C₂H₆O", "dimetil efir")], "Sinflararo izomer juftliklar."),
    C(3, "C₆H₁₄ tarkibli alkanning nechta strukturaviy izomeri bor?", "5", ["4", "6", "7"], "Geksan, 2-metilpentan, 3-metilpentan, 2,2-dimetilbutan, 2,3-dimetilbutan."),
    C(3, "Quyidagi alkenlardan qaysi biri sis-trans izomerga ega?", "Buten-2", ["Propen", "Buten-1", "2-metilpropen"], "Qo'shbog'dagi har bir C da turli o'rinbosarlar bo'lishi kerak."),
    O(3, "C₅H₁₂ tarkibli alkanning nechta izomeri bor? (faqat son)", ["3", "uch"], "Pentan, izopentan, neopentan."),
]

Q["K10.3"] = [
    C(1, "Alkanlarning umumiy formulasi qaysi?", "CₙH₂ₙ₊₂", ["CₙH₂ₙ", "CₙH₂ₙ₋₂", "CₙH₂ₙ₋₆"], "To'yingan uglevodorodlar."),
    C(1, "CH₄ ning nomi qaysi?", "Metan", ["Etan", "Propan", "Butan"], "Eng sodda alkan."),
    C(1, "–CH₃ radikalining nomi qaysi?", "Metil", ["Etil", "Propil", "Vinil"], "Metan − H."),
    C(2, "–C₂H₅ radikalining nomi qaysi?", "Etil", ["Metil", "Propil", "Izopropil"], "Etan − H."),
    C(2, "CH₃–CH(CH₃)–CH₃ birikmaning IUPAC nomi qaysi?", "2-metilpropan", ["Butan", "2-metilbutan", "1-metilpropan"], "Eng uzun zanjir — 3 ta uglerod."),
    C(2, "Uchlamchi uglerod atomi nechta uglerod atomi bilan bog'langan?", "3 ta", ["1 ta", "2 ta", "4 ta"], "Birlamchi — 1, ikkilamchi — 2, uchlamchi — 3, to'rtlamchi — 4."),
    C(2, "Dekanning molekulyar formulasi qaysi?", "C₁₀H₂₂", ["C₁₀H₂₀", "C₉H₂₀", "C₁₀H₁₈"], "CₙH₂ₙ₊₂, n = 10."),
    M(2, [("Butan", "C₄H₁₀"), ("Geksan", "C₆H₁₄"), ("Oktan", "C₈H₁₈")], "Alkanlar formulalari."),
    C(3, "2,2-dimetilbutan molekulasida nechta birlamchi uglerod atomi bor?", "4", ["3", "5", "2"], "CH₃–C(CH₃)₂–CH₂–CH₃: uchta CH₃ C2 da va bitta oxirgi CH₃."),
    C(3, "Molyar massasi 114 g/mol bo'lgan alkanning formulasi qaysi?", "C₈H₁₈", ["C₇H₁₆", "C₉H₂₀", "C₆H₁₄"], "14n + 2 = 114 → n = 8."),
    O(3, "Vodorodga nisbatan zichligi 22 bo'lgan alkanning molekulyar formulasini yozing.", ["C3H8", "C₃H₈", "propan"], "M = 44 → 14n + 2 = 44 → n = 3."),
]

Q["K10.4"] = [
    C(1, "Galogenli alkanlarga natriy ta'sir ettirib alkan olish reaksiyasi kim nomi bilan ataladi?", "Vyurs reaksiyasi", ["Dyuma reaksiyasi", "Kolbe reaksiyasi", "Kucherov reaksiyasi"], "2R–Cl + 2Na → R–R + 2NaCl."),
    C(1, "Karbon kislota tuzlarini ishqor bilan suyuqlantirish reaksiyasi kim nomi bilan ataladi?", "Dyuma reaksiyasi", ["Vyurs reaksiyasi", "Konovalov reaksiyasi", "Markovnikov"], "Zanjir bitta C ga qisqaradi."),
    C(1, "Karbon kislota tuzlari eritmasini elektroliz qilib alkan olish usuli kim nomi bilan ataladi?", "Kolbe reaksiyasi", ["Vyurs reaksiyasi", "Dyuma reaksiyasi", "Fisher–Tropsh"], "Anodda alkan va CO₂ ajraladi."),
    C(2, "CH₃COONa + NaOH → (suyuqlantirish) reaksiyasida qaysi mahsulotlar hosil bo'ladi?", "CH₄ va Na₂CO₃", ["C₂H₆ va Na₂CO₃", "CH₃OH va Na₂O", "CO₂ va CH₃ONa"], "Dyuma reaksiyasi."),
    C(2, "2CH₃CH₂Cl + 2Na → ? reaksiyada qaysi alkan hosil bo'ladi?", "Butan", ["Etan", "Propan", "Geksan"], "Zanjir ikki barobar uzayadi: C₂ + C₂ = C₄."),
    C(2, "Vyurs reaksiyasida uglerod zanjiri qanday o'zgaradi?", "Uzayadi", ["Qisqaradi", "O'zgarmaydi", "Halqaga aylanadi"], "Ikki radikal birikadi."),
    C(2, "Fisher–Tropsh sintezida qaysi moddalardan alkanlar olinadi?", "CO va H₂ (sintez-gaz)", ["CH₄ va O₂", "C va N₂", "CO₂ va H₂O"], "CO + H₂ → alkanlar + H₂O."),
    M(2, [("Vyurs reaksiyasi", "galogenalkan + Na"), ("Dyuma reaksiyasi", "karboksilat + NaOH (suyuqlantirish)"), ("Kolbe reaksiyasi", "karboksilat eritmasini elektroliz qilish")], "Alkanlar olinish usullari."),
    C(3, "CH₃Cl va C₂H₅Cl aralashmasiga Na ta'sir ettirilganda nechta turli alkan hosil bo'ladi?", "3", ["1", "2", "4"], "Etan, propan va butan."),
    C(3, "C₂H₅COONa + NaOH → (suyuqlantirish) reaksiyasida qaysi alkan hosil bo'ladi?", "Etan", ["Metan", "Propan", "Butan"], "Zanjir bitta C ga qisqaradi: C₃ → C₂."),
    O(3, "8,2 g CH₃COONa (M = 82) NaOH bilan suyuqlantirilganda n.sh. da necha litr metan hosil bo'ladi? (faqat son)", ["2,24", "2.24"], "n = 0,1 mol → V = 2,24 l."),
]

Q["K10.5"] = [
    C(1, "Alkanlar uchun qaysi reaksiya turi xos?", "Radikal o'rin olish", ["Elektrofil birikish", "Polimerlanish", "Gidratatsiya"], "Faqat σ-bog'lar bor."),
    C(1, "Alkanlar bromli suvni rangsizlantiradimi?", "Yo'q", ["Ha, darhol", "Faqat qizdirilganda", "Faqat yorug'likda"], "To'yingan uglevodorodlar birikish reaksiyasiga kirishmaydi."),
    C(1, "Metan yonganda qanday mahsulotlar hosil bo'ladi?", "CO₂ va H₂O", ["CO va H₂", "C va H₂", "CH₃OH"], "CH₄ + 2O₂ → CO₂ + 2H₂O."),
    C(2, "Alkanlarni galogenlashda vodorod atomi qaysi uglerodda eng oson almashadi?", "Uchlamchi uglerodda", ["Birlamchi uglerodda", "Ikkilamchi uglerodda", "Hammasida bir xil"], "Uchlamchi > ikkilamchi > birlamchi."),
    C(2, "Konovalov reaksiyasi nima?", "Alkanlarni suyultirilgan HNO₃ bilan nitrlash", ["Alkanlarni galogenlash", "Alkenlarni gidratatsiyalash", "Alkinlarni gidrogenlash"], "140 °C va bosim ostida."),
    C(2, "1500 °C da metan parchalanganda qaysi asosiy mahsulot hosil bo'ladi?", "Atsetilen", ["Etilen", "Etan", "Benzol"], "2CH₄ → C₂H₂ + 3H₂."),
    C(2, "AlCl₃ ishtirokida alkanlar bilan qanday jarayon boradi?", "Izomerlanish", ["Polimerlanish", "Gidrogenlash", "Gidratatsiya"], "Normal alkan tarmoqlangan alkanga aylanadi."),
    M(2, [("CH₄ + Cl₂ (yorug'lik)", "CH₃Cl + HCl"), ("CH₄ (1000 °C)", "C + 2H₂"), ("2CH₄ (1500 °C)", "C₂H₂ + 3H₂")], "Metan reaksiyalari."),
    C(3, "0,5 mol CH₄ ortiqcha xlor bilan to'liq xlorlansa (CCl₄ hosil bo'lguncha), necha mol HCl ajraladi?", "2 mol", ["1 mol", "0,5 mol", "4 mol"], "CH₄ + 4Cl₂ → CCl₄ + 4HCl: 0,5 · 4 = 2."),
    C(3, "44,8 l (n.sh.) metan yonganda necha litr CO₂ hosil bo'ladi?", "44,8 l", ["22,4 l", "89,6 l", "11,2 l"], "CH₄ + 2O₂ → CO₂ + 2H₂O: hajmlar 1 : 1."),
    O(3, "2CH₄ → C₂H₂ + 3H₂. 44,8 l (n.sh.) metandan necha litr H₂ hosil bo'ladi? (faqat son)", ["67,2", "67.2"], "n(CH₄) = 2 mol → n(H₂) = 3 mol → 67,2 l."),
]

Q["K10.6"] = [
    C(1, "Alkenlarning umumiy formulasi qaysi?", "CₙH₂ₙ", ["CₙH₂ₙ₊₂", "CₙH₂ₙ₋₂", "CₙH₂ₙ₋₆"], "Bitta qo'shbog'li uglevodorodlar."),
    C(1, "Etilenning molekulyar formulasi qaysi?", "C₂H₄", ["C₂H₆", "C₂H₂", "C₃H₆"], "Eng sodda alken."),
    C(1, "Alkenlarning sifat reaksiyasi qaysi?", "Bromli suvni rangsizlantirish", ["Fenolftaleinni qizartirish", "Ohakli suvni loyqalatish", "Kumush ko'zgu reaksiyasi"], "Br₂ qo'shbog'ga birikadi."),
    C(2, "Markovnikov qoidasiga ko'ra propen + HBr reaksiyasida qaysi mahsulot asosiy?", "2-brompropan", ["1-brompropan", "1,2-dibrompropan", "Propanol"], "H ko'p vodorodli uglerodga birikadi."),
    C(2, "Zaysev qoidasiga ko'ra spirtlar degidratatsiyasida H qaysi uglerod atomidan ajraladi?", "Vodorodi eng kam uglerod atomidan", ["Vodorodi eng ko'p uglerod atomidan", "Birlamchi uglerod atomidan", "Qaysi bo'lsa ham farqi yo'q"], "Qo'shbog' ko'proq o'rinbosarli bo'ladi."),
    C(2, "Vagner reaksiyasida alken KMnO₄ ning neytral eritmasi bilan reaksiyaga kirishsa, nima hosil bo'ladi?", "Ikki atomli spirt (glikol) va MnO₂ cho'kmasi", ["Karbon kislota va CO₂", "Alkan", "Galogenalkan"], "3C₂H₄ + 2KMnO₄ + 4H₂O → 3C₂H₄(OH)₂ + 2MnO₂↓ + 2KOH."),
    C(2, "Etanolni konsentrlangan H₂SO₄ bilan 170 °C da qizdirganda qaysi modda hosil bo'ladi?", "Etilen", ["Dietil efir", "Etan", "Atsetilen"], "Molekula ichida degidratatsiya."),
    M(2, [("Br₂ (suv) bilan", "rangsizlanish, dibromalkan"), ("KMnO₄ (neytral) bilan", "glikol va MnO₂ cho'kmasi"), ("H₂ (Ni) bilan", "alkan")], "Alkenlar reaksiyalari."),
    C(3, "Peroksid ishtirokida propen HBr bilan reaksiyaga kirishsa, qaysi mahsulot hosil bo'ladi?", "1-brompropan", ["2-brompropan", "1,2-dibrompropan", "Propan"], "Xarash effekti — Markovnikov qoidasiga teskari."),
    C(3, "5,6 l (n.sh.) etilen bromli suv bilan to'liq reaksiyaga kirishsa, necha gramm Br₂ sarflanadi?", "40 g", ["80 g", "20 g", "160 g"], "n(C₂H₄) = 0,25 mol → m(Br₂) = 0,25 · 160 = 40 g."),
    O(3, "Molyar massasi 56 g/mol bo'lgan alkenning molekulyar formulasini yozing.", ["C4H8", "C₄H₈", "buten"], "14n = 56 → n = 4."),
]

Q["K10.7"] = [
    C(1, "Alkadienlarning umumiy formulasi qaysi?", "CₙH₂ₙ₋₂", ["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₄"], "Ikkita qo'shbog'li uglevodorodlar."),
    C(1, "Divinil (butadien-1,3) ning formulasi qaysi?", "CH₂=CH–CH=CH₂", ["CH₂=C=CH–CH₃", "CH₃–CH=CH–CH₃", "CH≡C–CH₂–CH₃"], "Konyugirlangan dien."),
    C(1, "Izopren qaysi birikmaning nomi?", "2-metilbutadien-1,3", ["Butadien-1,3", "2-metilpropen", "Pentin-1"], "CH₂=C(CH₃)–CH=CH₂."),
    C(2, "CH₂=C=CH₂ qanday dien turiga kiradi?", "Kumulirlangan", ["Konyugirlangan", "Izolirlangan", "Siklik"], "Qo'shbog'lar yonma-yon."),
    C(2, "Kauchukni oltingugurt bilan qizdirish jarayoni qanday ataladi?", "Vulkanizatsiya", ["Polimerlanish", "Kreking", "Gidrogenlash"], "Rezina va ebonit olinadi."),
    C(2, "Konyugirlangan dienlarga yuqori haroratda galogen birikkanda asosan qaysi mahsulot hosil bo'ladi?", "1,4-birikish mahsuloti", ["1,2-birikish mahsuloti", "Faqat 2,3-birikish", "Birikmaydi"], "Yuqori haroratda qo'shbog' markazga siljiydi."),
    C(2, "Butadien-1,3 ortiqcha vodorod bilan (Ni) to'liq gidrogenlansa, nima hosil bo'ladi?", "Butan", ["Buten-1", "Buten-2", "Siklobutan"], "CH₂=CH–CH=CH₂ + 2H₂ → C₄H₁₀."),
    M(2, [("CH₂=C=CH₂", "kumulirlangan dien"), ("CH₂=CH–CH=CH₂", "konyugirlangan dien"), ("CH₂=CH–CH₂–CH=CH₂", "izolirlangan dien")], "Dienlar turlari."),
    C(3, "Butadien-1,3 ga past haroratda (−80 °C) 1 mol Br₂ birikkanda asosiy mahsulot qaysi?", "3,4-dibrombuten-1", ["1,4-dibrombuten-2", "1,2,3,4-tetrabrombutan", "2,3-dibrombutan"], "Past haroratda 1,2-birikish ustun."),
    C(3, "5,4 g butadien-1,3 (M = 54) ni to'liq gidrogenlash uchun n.sh. da necha litr H₂ kerak?", "4,48 l", ["2,24 l", "8,96 l", "6,72 l"], "n = 0,1 mol; 2 mol H₂ / mol → 0,2 mol = 4,48 l."),
    O(3, "Butadien-1,3 molekulasida nechta π-bog' bor? (faqat son)", ["2", "ikki"], "Ikkita qo'shbog' — ikkita π."),
]

Q["K10.8"] = [
    C(1, "Alkinlarning umumiy formulasi qaysi?", "CₙH₂ₙ₋₂", ["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₆"], "Bitta uchlamchi bog'li uglevodorodlar."),
    C(1, "Atsetilenning molekulyar formulasi qaysi?", "C₂H₂", ["C₂H₄", "C₂H₆", "C₆H₆"], "H–C≡C–H."),
    C(1, "Laboratoriyada atsetilen qanday olinadi?", "CaC₂ ga suv ta'sir ettirib", ["CaCO₃ ni qizdirib", "Etanolni degidratatsiyalab", "Metanni xlorlab"], "CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂."),
    C(2, "Kucherov reaksiyasida atsetilen suv bilan (Hg²⁺) reaksiyaga kirishsa, nima hosil bo'ladi?", "Sirka aldegidi (etanal)", ["Etanol", "Sirka kislota", "Etilen glikol"], "C₂H₂ + H₂O → CH₃CHO (keto-enol tautomeriya)."),
    C(2, "Atsetilen aktiv ko'mir ustida 600 °C da trimerlansa, nima hosil bo'ladi?", "Benzol", ["Toluol", "Siklogeksan", "Stirol"], "3C₂H₂ → C₆H₆ (Zelinskiy)."),
    C(2, "Atsetilen ortiqcha H₂ bilan (Ni) to'liq gidrogenlansa, qaysi mahsulot hosil bo'ladi?", "Etan", ["Etilen", "Metan", "Propan"], "C₂H₂ + 2H₂ → C₂H₆."),
    C(2, "Uchlamchi bog'ning uchida joylashgan alkinlarni qaysi reagent bilan aniqlash mumkin?", "Kumush oksidning ammiakli eritmasi", ["Ohakli suv", "NaCl eritmasi", "Fenolftalein"], "Cho'kma (kumush asetilenid) hosil bo'ladi."),
    M(2, [("C₂H₂ + H₂O (Hg²⁺)", "CH₃CHO"), ("3C₂H₂ (C, 600 °C)", "C₆H₆"), ("C₂H₂ + 2H₂ (Ni)", "C₂H₆")], "Atsetilen reaksiyalari."),
    C(3, "Quyidagilardan qaysi biri Ag₂O ning ammiakli eritmasi bilan cho'kma hosil qiladi?", "Propin", ["Butin-2", "Pentin-2", "Geksin-3"], "Faqat uchlamchi bog'i chekkada bo'lgan alkinlar (terminal)."),
    C(3, "6,4 g CaC₂ (M = 64) suv bilan reaksiyaga kirishsa, n.sh. da necha litr atsetilen olinadi?", "2,24 l", ["4,48 l", "1,12 l", "6,4 l"], "n(CaC₂) = 0,1 mol = n(C₂H₂)."),
    O(3, "0,1 mol atsetilen necha mol Br₂ ni biriktirib to'liq to'yinadi? (faqat son)", ["0,2", "0.2", "0,2 mol", "0.2 mol"], "C₂H₂ + 2Br₂ → C₂H₂Br₄."),
]

Q["K10.9"] = [
    C(1, "Benzolning molekulyar formulasi qaysi?", "C₆H₆", ["C₆H₁₂", "C₆H₁₄", "C₅H₆"], "Aromatik uglevodorod."),
    C(1, "Benzol qatori arenlarining umumiy formulasi qaysi?", "CₙH₂ₙ₋₆", ["CₙH₂ₙ₋₂", "CₙH₂ₙ₊₂", "CₙH₂ₙ"], "n ≥ 6."),
    C(1, "Benzol bromli suvni rangsizlantiradimi?", "Yo'q", ["Ha, darhol", "Faqat nurda", "Faqat qizdirilganda"], "Benzol halqasi barqaror."),
    C(2, "Benzol Br₂ bilan FeBr₃ ishtirokida reaksiyaga kirishsa, qaysi mahsulotlar hosil bo'ladi?", "C₆H₅Br va HBr", ["C₆H₆Br₂", "C₆H₁₂Br₆", "C₆H₅OH va HBr"], "Elektrofil o'rin olish."),
    C(2, "Benzolni nitrlash uchun qaysi aralashma ishlatiladi?", "Konsentrlangan HNO₃ va H₂SO₄", ["Suyultirilgan HCl", "NaOH va H₂O", "HNO₃ va NaCl"], "Nitrlovchi aralashma."),
    C(2, "Benzol halqasida uglerod–uglerod bog'lari qanday?", "Barchasi tenglashgan (oraliq)", ["Uchta oddiy, uchta qo'sh bog' navbatlashadi", "Barchasi oddiy bog'", "Barchasi uchlamchi bog'"], "Bog' uzunligi ~0,140 nm."),
    C(2, "Benzol 3H₂ bilan Ni ishtirokida reaksiyaga kirishsa, nima hosil bo'ladi?", "Siklogeksan", ["Geksan", "Geksen", "Toluol"], "C₆H₆ + 3H₂ → C₆H₁₂."),
    M(2, [("Benzol + Br₂ (FeBr₃)", "C₆H₅Br + HBr"), ("Benzol + HNO₃ (H₂SO₄)", "C₆H₅NO₂ + H₂O"), ("Benzol + 3H₂ (Ni)", "C₆H₁₂")], "Benzol reaksiyalari."),
    C(3, "Toluol kislotali muhitda KMnO₄ bilan oksidlanganda qaysi mahsulot hosil bo'ladi?", "Benzoy kislota", ["Fenol", "Stirol", "Siklogeksan"], "C₆H₅–CH₃ → C₆H₅–COOH."),
    C(3, "7,8 g benzol (M = 78) to'liq nitrlansa, necha gramm nitrobenzol (M = 123) hosil bo'ladi?", "12,3 g", ["7,8 g", "15,6 g", "24,6 g"], "n = 0,1 mol → 0,1 · 123 = 12,3 g."),
    O(3, "Benzol molekulasida jami nechta σ-bog' bor? (faqat son)", ["12", "12 ta"], "6 ta C–C va 6 ta C–H σ-bog'."),
]

Q["K10.10"] = [
    C(1, "Uglevodorodlar to'liq yonganda qanday mahsulotlar hosil bo'ladi?", "CO₂ va H₂O", ["CO va H₂", "C va H₂O", "CH₃OH va H₂"], "Kislorod yetarli bo'lganda."),
    C(1, "CₙH₂ₙ (alken) yonganda hosil bo'lgan CO₂ va H₂O mollari nisbati qanday?", "1 : 1", ["1 : 2", "2 : 1", "2 : 3"], "n CO₂ va n H₂O hosil bo'ladi."),
    C(1, "Gazning vodorodga nisbatan zichligi D(H₂) qanday topiladi?", "D = M(gaz) / 2", ["D = M(gaz) / 29", "D = M(gaz) · 2", "D = 22,4 / M"], "M(H₂) = 2 g/mol."),
    C(2, "D(H₂) = 14 bo'lgan alkenning formulasi qaysi?", "C₂H₄", ["C₃H₆", "C₄H₈", "CH₄"], "M = 28 → 14n = 28 → n = 2."),
    C(2, "Molyar massasi 58 g/mol bo'lgan alkan qaysi?", "C₄H₁₀", ["C₃H₈", "C₅H₁₂", "C₄H₈"], "14n + 2 = 58 → n = 4."),
    C(2, "Tarkibi 85,7% C va 14,3% H, D(H₂) = 28 bo'lgan uglevodorodning formulasi qaysi?", "C₄H₈", ["C₂H₄", "C₃H₆", "C₄H₁₀"], "M = 56; C : H = 1 : 2 → (CH₂)ₙ, n = 4."),
    C(2, "Havoga nisbatan zichligi 1,52 (M(havo) = 29) bo'lgan gazning molyar massasi taxminan qancha?", "44 g/mol", ["29 g/mol", "58 g/mol", "22 g/mol"], "1,52 · 29 ≈ 44."),
    M(2, [("D(H₂) = 8", "CH₄ (M = 16)"), ("D(H₂) = 14", "C₂H₄ (M = 28)"), ("D(H₂) = 15", "C₂H₆ (M = 30)")], "Nisbiy zichlik va uglevodorodlar."),
    C(3, "0,1 mol uglevodorod yonganda 8,96 l CO₂ (n.sh.) va 7,2 g H₂O hosil bo'ldi. Uning formulasi qaysi?", "C₄H₈", ["C₄H₁₀", "C₃H₈", "C₄H₆"], "n(CO₂) = 0,4 → C = 4; n(H₂O) = 0,4 → H = 8."),
    C(3, "1,4 g alken 8 g Br₂ ni biriktirdi (M(Br₂) = 160). Alkenning formulasi qaysi?", "C₂H₄", ["C₃H₆", "C₄H₈", "C₅H₁₀"], "n = 0,05 mol → M = 1,4 : 0,05 = 28."),
    O(3, "Alkinning vodorodga nisbatan zichligi 20 ga teng. Uning molekulyar formulasini yozing.", ["C3H4", "C₃H₄", "propin"], "M = 40 → 14n − 2 = 40 → n = 3."),
]
