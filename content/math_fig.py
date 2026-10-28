"""Matematika: chizmali (shaklli) savollar — geometriya, grafiklar, diagrammalar, fazoviy jismlar, to'plamlar."""
import math
from ._dsl import C, O, M, expand, validate
from ._ph import N, ON, fmt
from . import figs_math as G

BLOCK = ""

TOPICS = [
    ("MF.1", 8, "Uchburchak: tomonlar, burchaklar va yuza (chizma)", "free"),
    ("MF.2", 9, "Aylana, urinma va ichki chizilgan burchak (chizma)", "free"),
    ("MF.3", 8, "To'rtburchaklar va ularning yuzalari (chizma)", "free"),
    ("MF.4", 9, "Chiziqli va kvadrat funksiya grafiklari (chizma)", "free"),
    ("MF.5", 10, "Trigonometrik funksiya grafiklari (chizma)", "free"),
    ("MF.6", 9, "Diagrammalar va statistika (chizma)", "free"),
    ("MF.7", 10, "Fazoviy jismlar: hajm va sirt (chizma)", "free"),
    ("MF.8", 9, "To'plamlar va Venn diagrammasi (chizma)", "free"),
    ("MF.9", 9, "Koordinatalar tekisligi (chizma)", "free"),
]

_rt34 = G.right_triangle("3", "4", "x")
_rt512 = G.right_triangle("5", "x", "13")
Q = {}
Q["MF.1"] = [
    C(1, "Chizmada uchburchakning tomonlari 5, 6 va 7 ga teng. Perimetri qancha?", "18", ["16", "20", "210"], "5 + 6 + 7 = 18.", fig=G.triangle("a = 7", "b = 5", "c = 6")),
    N(2, "Chizmadagi to'g'ri burchakli uchburchakda katetlar 3 va 4. Gipotenuza x qancha?", 5, [7, 12, 3.5], "", "x² = 9 + 16 = 25.", fig=_rt34),
    N(2, "Chizmada gipotenuza 13, bitta katet 5. Ikkinchi katet x?", 12, [8, 18, 144], "", "x² = 169 − 25 = 144.", fig=_rt512),
    N(2, "Chizmadagi uchburchak (katetlar 3 va 4) yuzi qancha?", 6, [12, 7, 3.5], "", "S = 3·4/2 = 6.", fig=_rt34),
    C(2, "Uchburchak ichki burchaklarining yig'indisi necha gradus?", "180°", ["90°", "360°", "270°"], "Teorema.", fig=G.triangle("a", "b", "c")),
    C(2, "To'g'ri burchakli uchburchak uchun Pifagor teoremasi (chizmadagi belgilash: katetlar 3 va 4, gipotenuza x)?", "x² = 3² + 4²", ["x = 3 + 4", "x² = 4² − 3²", "x = 3·4"], "Gipotenuza kvadrati katetlar kvadratlari yig'indisiga teng.", fig=_rt34),
    N(3, "Uchburchak tomonlari 13, 14, 15 (Geron formulasi). Yuzi?", 84, [90, 105, 42], "", "p = 21; S = √(21·8·7·6) = 84."),
    ON(3, "To'g'ri burchakli uchburchakda katetlar 6 va 8. Gipotenuzaga tushirilgan balandlik necha? (kasr: 4,8)", 4.8, "h = ab/c = 48/10 = 4,8."),
    ON(3, "Uchburchakning ikki burchagi 50° va 60°. Uchinchi burchagi necha gradus?", 70, "180 − 110 = 70."),
    M(2, [("Teng yonli uchburchak", "ikki tomoni teng"), ("To'g'ri burchakli uchburchak", "bitta burchagi 90°"), ("Teng tomonli uchburchak", "barcha burchaklari 60°")], "Uchburchak turlari."),
]

Q["MF.2"] = [
    C(1, "Chizmada AOB markaziy burchak 80°. U tiralgan ACB ichki burchak necha gradus?", "40°", ["80°", "160°", "20°"], "Ichki burchak markaziy burchakning yarmiga teng.", fig=G.inscribed_angle()),
    C(2, "Aylanaga o'tkazilgan urinma urinish nuqtasidagi radiusga...", "perpendikulyar", ["parallel", "teng", "o'tkir burchak ostida"], "OT ⟂ PT.", fig=G.circle_tangent()),
    N(2, "Chizmada OT = r = 5 va OP = 13. Urinma PT?", 12, [8, 18, 144], "", "PT² = 169 − 25 = 144.", fig=G.circle_tangent()),
    C(2, "Diametrga tiralgan ichki burchak necha gradus?", "90°", ["45°", "180°", "60°"], "Yarim aylana yoyiga tiralgan."),
    N(3, "Radiusi 7 sm aylana uzunligi (π = 22/7)?", 44, [22, 154, 88], "sm", "2πr = 2·22/7·7 = 44."),
    N(3, "Radiusi 7 sm doira yuzi (π = 22/7)?", 154, [44, 308, 22], "sm²", "πr² = 22/7·49 = 154."),
    ON(3, "Markaziy burchak 120°, radius 6. Yoy uzunligi nechaga teng (π = 3 deb oling)?", 12, "l = 120/360·2·3·6 = 12."),
    ON(3, "Aylanada AB yoyi 100° bo'lsa, shu yoyga tiralgan ichki burchak necha gradus?", 50, "Yoyning yarmi."),
]

Q["MF.3"] = [
    N(1, "Chizmadagi to'g'ri to'rtburchak tomonlari 8 va 6. Yuzi?", 48, [14, 28, 24], "", "S = 8·6.", fig=G.rect_diagonals("8", "6")),
    N(2, "Shu to'g'ri to'rtburchakning diagonali?", 10, [14, 7, 48], "", "√(64+36) = 10.", fig=G.rect_diagonals("8", "6")),
    N(2, "Chizmadagi parallelogrammning asosi 10, balandligi 4. Yuzi?", 40, [60, 20, 24], "", "S = a·h.", fig=G.parallelogram("10", "6", "4")),
    N(2, "Chizmadagi trapetsiya asoslari 12 va 6, balandligi 5. Yuzi?", 45, [90, 60, 30], "", "S = (12+6)/2·5.", fig=G.trapezoid("12", "6", "5", "5")),
    N(3, "Trapetsiyaning o'rta chizig'i (asoslar 12 va 6)?", 9, [18, 6, 72], "", "(12 + 6)/2.", fig=G.trapezoid("12", "6", "5", "5")),
    N(3, "Rombning diagonallari 10 va 24. Tomoni?", 13, [17, 34, 26], "", "√(25 + 144) = 13."),
    C(2, "To'g'ri to'rtburchakning diagonallari...", "teng va kesishish nuqtasida teng ikkiga bo'linadi", ["o'zaro perpendikulyar va teng", "har doim teng emas", "parallel"], "Xossa.", fig=G.rect_diagonals("a", "b")),
    ON(3, "Kvadratning diagonali 6√2. Yuzi necha?", 36, "a = 6; S = 36."),
    ON(3, "Parallelogrammning yuzi 48, balandligi 6. Asosi necha?", 8, "a = 48/6 = 8."),
]

Q["MF.4"] = [
    C(1, "Chizmada y = kx + b to'g'ri chizig'i (0; 1) va (1; 3) nuqtalardan o'tadi. Uning tenglamasi?", "y = 2x + 1", ["y = x + 1", "y = 2x − 1", "y = x + 2"], "k = 2, b = 1.", fig=G.graph_linear(2, 1, dots=[(0, 1, "A"), (1, 3, "B")])),
    N(2, "Shu chiziq x = 4 da y qiymati?", 9, [8, 5, 7], "", "2·4 + 1.", fig=G.graph_linear(2, 1, dots=[(0, 1, "A"), (1, 3, "B")])),
    C(2, "Chizmadagi parabola y = x² − 2x − 3 grafigi. Uning nollari (x o'qi bilan kesishish nuqtalari)?", "x = −1 va x = 3", ["x = 1 va x = −3", "x = 0 va x = 2", "x = −3 va x = 3"], "x² − 2x − 3 = 0.", fig=G.graph_parabola(1, -2, -3, show=[(-1, 0, ""), (3, 0, ""), (1, -4, "V")])),
    C(2, "Shu parabolaning uchi (V) koordinatalari?", "(1; −4)", ["(−1; 0)", "(0; −3)", "(3; 0)"], "x₀ = −b/2a = 1; y₀ = 1 − 2 − 3 = −4.", fig=G.graph_parabola(1, -2, -3, show=[(-1, 0, ""), (3, 0, ""), (1, -4, "V")])),
    N(2, "y = x² − 2x − 3 funksiyaning x = 0 dagi qiymati (grafik y o'qi bilan kesishadi)?", -3, [3, -1, 1], "", "y(0) = −3.", fig=G.graph_parabola(1, -2, -3)),
    C(3, "Chizmada parabola shoxlari yuqoriga yo'nalgan. Bu nimani bildiradi?", "a > 0", ["a < 0", "a = 0", "c > 0"], "y = ax² + bx + c da a > 0.", fig=G.graph_parabola(1, -2, -3)),
    ON(3, "y = x² − 4x + 3 funksiyaning eng kichik qiymati necha?", -1, "Uchi (2; −1)."),
    ON(3, "To'g'ri chiziq (0; 2) va (2; 8) nuqtalardan o'tadi. Burchak koeffitsiyenti k necha?", 3, "k = (8−2)/2 = 3."),
]

Q["MF.5"] = [
    C(1, "Chizmada y = sin x grafigi. Uning eng katta qiymati?", "1", ["0", "2", "π"], "−1 ≤ sin x ≤ 1.", fig=G.graph_trig("sin")),
    C(2, "y = sin x funksiyaning eng kichik musbat davri?", "2π", ["π", "π/2", "4π"], "Davr 2π.", fig=G.graph_trig("sin")),
    C(2, "Chizmada y = 2cos 2x grafigi. Amplitudasi?", "2", ["1", "4", "π"], "Amplituda — koeffitsiyent 2.", fig=G.graph_trig("cos", 2, 2)),
    C(2, "Shu funksiyaning davri?", "π", ["2π", "π/2", "4π"], "T = 2π/2 = π.", fig=G.graph_trig("cos", 2, 2)),
    N(2, "y = sin x grafigi x = π/2 da qiymati?", 1, [0, -1, 2], "", "sin(π/2) = 1.", fig=G.graph_trig("sin")),
    C(3, "y = cos x grafigi y o'qini qaysi nuqtada kesadi?", "(0; 1)", ["(0; 0)", "(0; −1)", "(π; 0)"], "cos 0 = 1."),
    ON(3, "y = 3 sin x funksiyaning eng katta qiymati necha?", 3, "Amplituda 3."),
    ON(3, "y = sin 4x funksiyaning davri π ning necha baravariga teng? (o'nli kasr bilan yozing)", 0.5, "T = 2π/4 = π/2 = 0,5·π."),
]

Q["MF.6"] = [
    N(1, "Chizmadagi ustunli diagrammada I, II, III, IV guruhlar 20, 35, 15, 30. Jami?", 100, [90, 110, 80], "", "20+35+15+30 = 100.", fig=G.bar_chart(["I", "II", "III", "IV"], [20, 35, 15, 30], 40)),
    N(2, "Shu ma'lumotlarning o'rtacha qiymati?", 25, [30, 20, 35], "", "100/4.", fig=G.bar_chart(["I", "II", "III", "IV"], [20, 35, 15, 30], 40)),
    C(2, "Qaysi guruhda ko'rsatkich eng katta?", "II", ["I", "III", "IV"], "35 eng katta.", fig=G.bar_chart(["I", "II", "III", "IV"], [20, 35, 15, 30], 40)),
    C(2, "Doiraviy diagrammada A sektor 40%. Markaziy burchagi?", "144°", ["40°", "72°", "120°"], "0,4·360.", fig=G.pie_chart([("A", 40), ("B", 25), ("C", 20), ("D", 15)])),
    N(2, "Doiraviy diagramma 200 ta o'quvchi. B sektor 25%. B ga tegishli o'quvchilar?", 50, [25, 40, 75], "", "200·0,25.", fig=G.pie_chart([("A", 40), ("B", 25), ("C", 20), ("D", 15)])),
    N(3, "Ma'lumotlar: 20, 35, 15, 30. Mediana?", 25, [27.5, 30, 20], "", "Tartiblangan: 15, 20, 30, 35 → (20+30)/2 = 25."),
    ON(3, "Doiraviy diagrammada C sektor 20%. Markaziy burchagi necha gradus?", 72, "0,2·360."),
    ON(3, "Ma'lumotlar 4, 8, 6, 5, 7: arifmetik o'rtacha necha?", 6, "30/5."),
]

Q["MF.7"] = [
    N(1, "Chizmada kub qirrasi a = 4. Hajmi?", 64, [16, 48, 12], "", "V = a³.", fig=G.cube_like("cube", "a = 4", "a")),
    N(2, "Shu kubning to'la sirti?", 96, [64, 24, 48], "", "6a² = 96.", fig=G.cube_like("cube", "a = 4", "a")),
    N(2, "Silindr r = 3, h = 5. Hajmi (π ni qoldiring: faqat π oldidagi son)?", 45, [15, 30, 90], "π", "V = πr²h = 45π.", fig=G.cube_like("cylinder", "r = 3", "h = 5")),
    N(2, "Konus r = 3, h = 4. Yasovchisi?", 5, [7, 12, 25], "", "l = √(9+16) = 5.", fig=G.cube_like("cone", "r = 3", "h = 4")),
    N(3, "Konus r = 3, h = 4. Hajmi (π oldidagi son)?", 12, [36, 24, 6], "π", "V = πr²h/3 = 12π.", fig=G.cube_like("cone", "r = 3", "h = 4")),
    N(3, "Muntazam to'rtburchakli piramida asosi a = 6, balandligi h = 4. Hajmi?", 48, [144, 24, 96], "", "V = a²h/3 = 48.", fig=G.cube_like("pyramid", "a = 6", "h = 4")),
    ON(3, "Tomonlari 3, 4, 5 bo'lgan to'g'ri burchakli parallelepiped hajmi necha?", 60, "3·4·5."),
    ON(3, "Silindr r = 2, h = 5. Yon sirti π ning necha baravari? (2πrh = 20π)", 20, "2·2·5 = 20."),
]

Q["MF.8"] = [
    N(1, "Venn diagrammasida faqat A da 5 ta, faqat B da 7 ta, ikkalasida 3 ta element. |A|?", 8, [5, 12, 15], "", "5 + 3 = 8.", fig=G.venn("A", "B", "5", "7", "3")),
    N(2, "Shu diagrammada |B|?", 10, [7, 12, 15], "", "7 + 3 = 10.", fig=G.venn("A", "B", "5", "7", "3")),
    N(2, "Shu diagrammada A ∪ B elementlari soni?", 15, [10, 8, 18], "", "5+7+3 = 15.", fig=G.venn("A", "B", "5", "7", "3")),
    N(2, "A ∩ B elementlari soni?", 3, [15, 5, 7], "", "Kesishma.", fig=G.venn("A", "B", "5", "7", "3")),
    C(2, "Faqat A ga tegishli bo'lgan elementlar to'plami (diagrammada chap qism) qanday belgilanadi?", "A \\ B", ["B \\ A", "A ∩ B", "A ∪ B"], "Ayirma.", fig=G.venn("A", "B", "", "", "")),
    N(3, "|A| = 12, |B| = 9, |A ∩ B| = 4. |A ∪ B|?", 17, [21, 25, 13], "", "12 + 9 − 4."),
    ON(3, "Sinfda 30 o'quvchi: 18 tasi ingliz, 15 tasi nemis tili o'rganadi, 6 tasi ikkalasini. Hech qaysi tilni o'rganmaydiganlar soni necha?", 3, "18+15−6 = 27; 30−27 = 3."),
    ON(3, "|A| = 20, |A ∪ B| = 30, |A ∩ B| = 5. |B| necha?", 15, "30 = 20 + |B| − 5."),
]

Q["MF.9"] = [
    N(1, "Chizmada A(1; 2) va B(4; 2) nuqtalar. AB uzunligi?", 3, [5, 6, 2], "", "|4−1| = 3.", fig=G.coord_points([(1, 2, "A"), (4, 2, "B")], segs=[((1, 2), (4, 2))])),
    N(2, "Chizmadagi A(1; 2), B(4; 2), C(4; 5) uchburchakning AC tomoni (√ ostida): AC² = ?", 18, [9, 6, 3], "", "AC² = 3² + 3² = 18.", fig=G.coord_points([(1, 2, "A"), (4, 2, "B"), (4, 5, "C")], segs=[((1, 2), (4, 2)), ((4, 2), (4, 5)), ((1, 2), (4, 5))])),
    N(2, "Shu uchburchak yuzi?", 4.5, [9, 3, 6], "", "S = 3·3/2 = 4,5.", fig=G.coord_points([(1, 2, "A"), (4, 2, "B"), (4, 5, "C")], segs=[((1, 2), (4, 2)), ((4, 2), (4, 5)), ((1, 2), (4, 5))])),
    C(2, "Chizmadagi B(4; 2) nuqta qaysi chorakda?", "I chorak", ["II chorak", "III chorak", "IV chorak"], "x > 0, y > 0.", fig=G.coord_points([(4, 2, "B")])),
    N(3, "(1; 2) va (7; 10) nuqtalar orasidagi masofa?", 10, [14, 8, 6], "", "√(36+64) = 10."),
    N(3, "(2; 4) va (8; −2) kesma o'rtasining koordinatalari yig'indisi (x + y)?", 6, [5, 12, 10], "", "O'rta: (5; 1); 5 + 1 = 6."),
    ON(3, "A(0; 0), B(6; 0), C(0; 8) uchburchakning yuzi necha?", 24, "6·8/2."),
    ON(3, "A(−2; 3) nuqtaning y o'qiga nisbatan simmetrigi (x koordinatasi) necha?", 2, "(2; 3)."),
]

_BANKS = Q


def pack():
    topics, questions = [], []
    for code, grade, name, tier in TOPICS:
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": BLOCK})
        questions.extend(expand(name, grade, _BANKS.get(code, []), BLOCK))
    problems = validate(questions)
    if problems:
        import logging
        logging.getLogger(__name__).warning("Matematika chizmali bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "math", "modes": ["dtm", "certificate"], "topics": topics, "questions": questions}
