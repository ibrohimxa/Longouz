"""Fizika: issiqlik, molekulyar fizika va termodinamika (8- va 10-sinf)."""
import math
from ._dsl import C, O, M
from ._ph import N, ON, fmt
from . import figs_phys as F

R = 8.31
Q = {}

Q["P8.1"] = [
    C(1, "Temperaturaning SI dagi birligi?", "kelvin (K)", ["selsiy (°C)", "farengeyt (°F)", "joul (J)"], "SI: kelvin."),
    N(1, "27 °C necha kelvin? (T = t + 273)", 300, [246, 27, 327], "K", "27 + 273."),
    N(1, "400 K necha °C?", 127, [673, 400, 173], "°C", "400 − 273."),
    C(1, "Vakuumda issiqlik qanday uzatiladi?", "Nurlanish orqali", ["Konveksiya", "Issiqlik o'tkazuvchanlik", "Diffuziya"], "Moddasiz muhitda faqat nurlanish."),
    C(2, "Konveksiya qaysi muhitlarda bo'ladi?", "Suyuqlik va gazlarda", ["Faqat qattiq jismlarda", "Faqat vakuumda", "Faqat metallarda"], "Modda oqimi bilan."),
    C(2, "Jismning ichki energiyasini o'zgartirishning ikki usuli?", "Ish bajarish va issiqlik uzatish", ["Siqish va cho'zish", "Qizdirish va isitish", "Aylantirish va tebratish"], "Termodinamika."),
    C(2, "Qora rangli jismlar nurlanishni...", "yaxshi yutadi va yaxshi chiqaradi", ["yomon yutadi", "qaytaradi", "o'tkazadi"], "Qora jism."),
    N(2, "Selsiy shkalasida temperatura 25 °C ga ko'tarildi. Kelvin shkalasida qanchaga ortdi?", 25, [298, 248, 273], "K", "Bo'linma bir xil."),
    M(2, [("Issiqlik o'tkazuvchanlik", "metall sterjenning qizishi"), ("Konveksiya", "xonada isitgich ustidagi havo ko'tarilishi"), ("Nurlanish", "Quyoshdan Yerga issiqlik")], "Issiqlik uzatish turlari."),
    ON(3, "Suvning muzlash temperaturasi 0 °C, qaynash temperaturasi 100 °C. Farengeytda qaynash 212 °F. 50 °C necha °F? (°F = 1,8·°C + 32)", 122, "1,8·50 + 32 = 122."),
]

Q["P8.2"] = [
    C(1, "Qizdirish uchun zarur issiqlik miqdori formulasi?", "Q = cmΔt", ["Q = qm", "Q = λm", "Q = Lm"], "c — solishtirma issiqlik sig'imi."),
    N(1, "2 kg suvni 10 °C ga qizdirish uchun (c = 4200 J/(kg·°C)) kerak bo'lgan issiqlik?", 84000, [8400, 42000, 840], "J", "4200·2·10."),
    N(2, "0,5 kg mis (c = 400) 20 °C dan 100 °C gacha qizdirildi. Q?", 16000, [4000, 20000, 8000], "J", "400·0,5·80."),
    N(2, "Massasi 3 kg jism 600 J issiqlik olib 0,5 °C ga qizdi. c?", 400, [900, 360, 4000], "J/(kg·°C)", "c = Q/(mΔt) = 600/1,5."),
    N(3, "20 °C li 2 kg suvga 80 °C li 1 kg suv aralashtirildi. Muvozanat temperaturasi?", 40, [50, 60, 30], "°C", "(2·20 + 1·80)/3 = 40."),
    N(3, "10 °C li 3 kg suv va 90 °C li 1 kg suv aralashtirilsa, temperatura?", 30, [50, 40, 25], "°C", "(30+90)/4 = 30."),
    C(2, "Solishtirma issiqlik sig'imining birligi?", "J/(kg·°C)", ["J/kg", "J·°C", "W/m"], "c = Q/(mΔt)."),
    C(2, "Teng massali suv va mis bir xil Q olsa, qaysi biri ko'proq qiziydi?", "Mis (c kichik)", ["Suv", "Teng", "Hech biri"], "Δt = Q/(cm)."),
    ON(3, "Issiqlik sig'imi 500 J/°C bo'lgan idishga 1 kg 20 °C suv quyildi. Unga 100 °C li 0,5 kg suv qo'shilganda umumiy temperatura necha °C? (c suv = 4200)", 50.3, "(500·20 + 4200·20 + 2100·100)/(500 + 4200 + 2100) — yo'q: idish ham 20 °C: (10000+84000+210000)/6800 ≈ 44,7.") if False else ON(3, "1 kg 20 °C suvga 100 °C li 1 kg suv qo'shilsa, umumiy temperatura necha °C?", 60, "Teng massalar: (20+100)/2 = 60."),
]

Q["P8.3"] = [
    C(1, "Yoqilg'ining yonish issiqligi formulasi?", "Q = qm", ["Q = cmΔt", "Q = λm", "Q = Lm"], "q — solishtirma yonish issiqligi."),
    N(2, "0,2 kg ko'mir (q = 30 MJ/kg) yonganda ajraladigan issiqlik?", 6, [60, 0.6, 150], "MJ", "30·0,2."),
    N(2, "0 °C dagi 2 kg muzni eritish uchun (λ = 330 kJ/kg) issiqlik?", 660, [165, 330, 1320], "kJ", "λm."),
    N(2, "100 °C dagi 0,5 kg suvni bug'ga aylantirish (L = 2,3 MJ/kg)?", 1.15, [2.3, 4.6, 0.23], "MJ", "Lm."),
    C(2, "Chizmadagi isitish grafigida gorizontal qismlar nimani bildiradi?", "Fazaviy o'tish (erish, qaynash)", ["Jism sovishini", "Jism massasi kamayishini", "Issiqlik uzatilmayotganini"], "Temperatura o'zgarmaydi.", fig=F.heating_curve()),
    C(2, "Chizmada 3-bo'lak nimaga mos?", "Suvning isishi", ["Muzning erishi", "Bug'ning isishi", "Suvning qaynashi"], "100 °C gacha qizish.", fig=F.heating_curve()),
    N(3, "−10 °C dagi 1 kg muzni 0 °C gacha qizdirish (c = 2100) va eritish (λ = 330 kJ/kg) uchun jami issiqlik?", 351, [330, 21, 372], "kJ", "21 + 330 = 351 kJ."),
    N(3, "0 °C li 1 kg muzni 20 °C li suvga aylantirish (c = 4200; λ = 330 kJ/kg)?", 414, [330, 84, 246], "kJ", "330 + 84."),
    ON(3, "Plitka quvvati 1 kW, 100 °C da qaynayotgan suvning qancha massasi (kg) 2,3 MJ issiqlik bilan bug'lanadi? (L = 2,3 MJ/kg)", 1, "m = Q/L = 1 kg."),
    M(2, [("Erish", "Q = λm"), ("Bug'lanish", "Q = Lm"), ("Yonish", "Q = qm")], "Formulalar."),
]

Q["P8.4"] = [
    C(1, "Issiqlik dvigatelining FIK formulasi?", "η = A_f / Q_olingan", ["η = Q / A", "η = T₁·T₂", "η = A + Q"], "Foydali ish olingan issiqlikka nisbati."),
    N(2, "Dvigatel isitkichdan 500 J oldi, sovitkichga 300 J berdi. FIK?", 40, [60, 62.5, 80], "%", "A = 200; η = 200/500."),
    N(2, "Isitkich 600 K, sovitkich 300 K bo'lgan Karno dvigateli FIK?", 50, [200, 33, 100], "%", "η = 1 − 300/600."),
    N(3, "Karno sikli FIK = 40%, sovitkich 300 K. Isitkich temperaturasi?", 500, [750, 420, 200], "K", "T₁ = T₂/(1−η) = 300/0,6."),
    N(3, "FIK 25% dvigatel 800 J foydali ish bajardi. Isitkichdan olingan issiqlik?", 3200, [200, 1000, 6400], "J", "Q = A/η."),
    C(2, "Ichki yonuv dvigatelida to'rt takt tartibi?", "so'rish, siqish, ish yurishi, chiqarish", ["siqish, so'rish, chiqarish, ish", "ish, so'rish, siqish, chiqarish", "chiqarish, ish, siqish, so'rish"], "To'rt taktli sikl."),
    C(2, "Haqiqiy issiqlik dvigatelining FIK 100% bo'lishi mumkinmi?", "Yo'q (termodinamikaning ikkinchi qonuni)", ["Ha, ishqalanish bo'lmasa", "Ha, vakuumda", "Ha, katta quvvatda"], "Sovitkichsiz ishlamaydi."),
    ON(3, "Issiqlik dvigateli bir siklda isitkichdan 1200 J oladi va 900 J sovitkichga beradi. FIK necha foiz?", 25, "A = 300; η = 25%."),
    ON(3, "Isitkich 727 °C, sovitkich 27 °C. Karno FIK necha foiz? (K ga o'tkazing)", 70, "T₁ = 1000 K, T₂ = 300 K; η = 70%."),
]

Q["P10.1"] = [
    C(1, "MKT ning asosiy qoidalaridan biri?", "Modda zarrachalardan iborat va ular doim betartib harakatda", ["Modda uzluksiz", "Zarralar tinch turadi", "Zarralar o'zaro ta'sirlashmaydi"], "Uchta qoida."),
    N(1, "Avogadro doimiysi taxminan?", 6.02e23, [6.02e22, 1.6e-19, 6.63e-34], "mol⁻¹", "N_A."),
    N(2, "2 mol moddada nechta molekula bor?", 1.204e24, [6.02e23, 3.01e23, 1.204e23], "", "2·6,02·10²³."),
    N(2, "Suvning molyar massasi 18 g/mol. 36 g suv necha mol?", 2, [18, 0.5, 648], "mol", "36/18."),
    N(3, "180 g suvdagi molekulalar soni?", 6.02e24, [6.02e23, 3.01e24, 1.08e26], "", "10 mol·N_A."),
    N(3, "Bitta suv molekulasining massasi taxminan? (M = 18 g/mol)", 2.99e-26, [3e-23, 1.8e-26, 6e-26], "kg", "m₀ = M/N_A = 0,018/6,02·10²³."),
    C(2, "Brovn harakati qaysi zarrachalarda kuzatiladi?", "Suyuqlikdagi mayda zarrachalarda", ["Faqat qattiq jismlarda", "Faqat vakuumda", "Faqat atomlarda"], "Zarrachaga molekulalar urilishi."),
    ON(3, "Gazning 3,01·10²³ ta molekulasi necha mol?", 0.5, "ν = N/N_A."),
    M(2, [("ν", "modda miqdori"), ("M", "molyar massa"), ("N_A", "Avogadro doimiysi")], "Belgilar."),
]

Q["P10.2"] = [
    C(1, "Ideal gaz MKT asosiy tenglamasi?", "p = (1/3) n m₀ v²", ["p = nkT²", "p = m₀v", "p = n/m₀"], "Bosim molekulalar zichligi va kinetik energiyaga bog'liq."),
    C(1, "Molekulalar o'rtacha kinetik energiyasi temperaturaga...", "to'g'ri proporsional", ["teskari proporsional", "bog'liq emas", "kvadratiga teskari"], "Ē = 3kT/2."),
    N(2, "T = 300 K da molekulaning o'rtacha kinetik energiyasi (k = 1,38·10⁻²³)?", 6.21e-21, [4.14e-21, 1.38e-21, 6.21e-23], "J", "3kT/2 = 1,5·1,38e-23·300."),
    N(2, "Gaz temperaturasi 4 marta oshsa, o'rtacha kvadratik tezlik necha marta ortadi?", 2, [4, 16, 1.41], "marta", "v ∼ √T."),
    N(3, "Kislorod (M = 32 g/mol) T = 300 K da v_kv? (R = 8,31)", 483.4, [900, 241, 150], "m/s", "√(3RT/M) = √(3·8,31·300/0,032) ≈ 483,4."),
    C(2, "Bolsman doimiysi bilan universal gaz doimiysi orasidagi bog'lanish?", "R = k·N_A", ["R = k/N_A", "R = k + N_A", "R = k²"], "R = 8,31 J/(mol·K)."),
    N(3, "Bosim 2·10⁵ Pa, molekulalar konsentratsiyasi 3·10²⁵ m⁻³. O'rtacha kinetik energiya (p = 2/3·n·Ē)?", 1e-20, [4e-20, 3e-21, 6.7e-21], "J", "Ē = 3p/(2n) = 6e5/6e25 = 1e-20."),
    ON(3, "Gaz molekulalari o'rtacha kvadratik tezligi 400 m/s edi. Temperaturasi 4 marta oshirilsa, tezlik necha m/s bo'ladi?", 800, "v ∼ √T → 2·400."),
]

Q["P10.3"] = [
    C(1, "Mendeleyev–Klapeyron tenglamasi?", "pV = (m/M)RT", ["pV = mRT", "p/V = νRT", "pT = νRV"], "Ideal gaz holat tenglamasi."),
    N(2, "1 mol ideal gaz T = 300 K, V = 0,0249 m³ da bosim (R = 8,31)?", 100120, [10000, 250000, 8310], "Pa", "νRT/V = 8,31·300/0,0249 ≈ 100 120."),
    N(2, "2 mol gaz 400 K da 8,31 litr hajm egallaydi. Bosim? (R = 8,31)", 800000, [400000, 1600000, 8000], "Pa", "2·8,31·400/0,00831 = 800 000 Pa."),
    N(3, "Hajmi 2 m³ idishda 0,5 mol gaz, T = 200 K. Bosim (R = 8,31)?", 415.5, [831, 83.1, 4155], "Pa", "νRT/V = 0,5·8,31·200/2."),
    N(3, "Massasi 28 g azot (M = 28) 300 K da 10 l idishda. Bosim (R = 8,31)?", 249300, [24930, 498600, 83100], "Pa", "ν = 1; p = 8,31·300/0,01."),
    N(3, "Gaz zichligi ρ = 1,2 kg/m³, M = 0,029 kg/mol, T = 300 K. Bosim?", 103200, [51600, 206400, 10320], "Pa", "p = ρRT/M = 1,2·8,31·300/0,029 ≈ 103 152."),
    C(2, "Temperatura 2 marta oshsa, hajm o'zgarmasa, bosim...", "2 marta oshadi", ["2 marta kamayadi", "o'zgarmaydi", "4 marta oshadi"], "p/T = const."),
    ON(3, "Gaz 0 °C va 10⁵ Pa da 2 m³ hajm egallaydi. Xuddi shu bosimda 273 °C gacha qizdirilsa, hajmi necha m³ bo'ladi?", 4, "V₁/T₁ = V₂/T₂: 2/273 = V/546."),
    ON(3, "Idishda gaz 300 K da 2 atm bosimda. Temperatura 450 K gacha oshirilsa (V = const), bosim necha atm?", 3, "p₂ = 2·450/300 = 3."),
]

Q["P10.4"] = [
    C(1, "Boyl–Mariott qonuni qaysi jarayon uchun?", "Izotermik", ["Izobar", "Izoxor", "Adiabatik"], "pV = const (T = const).", fig=F.isoprocess("isotherm")),
    C(1, "Izobar jarayonda doimiy kattalik?", "bosim", ["hajm", "temperatura", "massa va temperatura"], "Gey-Lyussak: V/T = const."),
    C(1, "Izoxor jarayonda (Sharl qonuni) o'zgarmas kattalik?", "hajm", ["bosim", "temperatura", "zichlik ortadi"], "p/T = const."),
    C(2, "Chizmada p–V diagrammada qaysi jarayon tasvirlangan?", "Izotermik", ["Izobar", "Izoxor", "Adiabatik"], "Giperbola.", fig=F.isoprocess("isotherm")),
    C(2, "Chizmada p–V tekisligida gorizontal chiziq qaysi jarayon?", "Izobar", ["Izoxor", "Izotermik", "Adiabatik"], "p = const.", fig=F.isoprocess("isobar")),
    C(2, "p–V tekisligida vertikal chiziq qaysi jarayon?", "Izoxor", ["Izobar", "Izotermik", "Adiabatik"], "V = const.", fig=F.isoprocess("isochore")),
    N(3, "Gaz izotermik siqildi: hajmi 6 l dan 2 l gacha. Dastlabki bosim 1·10⁵ Pa. Oxirgi bosim?", 300000, [100000, 33333, 600000], "Pa", "p₂ = p₁V₁/V₂."),
    N(3, "Gaz izobar kengayib, T 300 K dan 450 K gacha oshdi. Hajmi V₁ = 4 l edi. V₂?", 6, [2.67, 9, 8], "l", "V₂ = V₁T₂/T₁."),
    ON(3, "Izoxor jarayonda gaz 27 °C dan 327 °C gacha qizdirilsa, bosim necha marta ortadi?", 2, "600 K / 300 K = 2."),
    M(2, [("Izotermik", "T = const"), ("Izobar", "p = const"), ("Izoxor", "V = const")], "Izojarayonlar."),
]

_cy = F.pv_cycle([(1, 1), (1, 3), (3, 3), (3, 1)])
Q["P10.5"] = [
    C(2, "Chizmadagi p–V siklida 1→2 jarayon qaysi?", "Izoxor (bosim ortadi)", ["Izobar", "Izotermik", "Adiabatik"], "V = const, p ortadi.", fig=_cy),
    C(2, "Chizmadagi siklda 2→3 jarayon qaysi?", "Izobar kengayish", ["Izoxor", "Izotermik siqilish", "Adiabatik"], "p = const, V ortadi.", fig=_cy),
    N(3, "Chizmadagi sikl (p birlikda 10⁵ Pa, V litrda 10⁻³ m³): p = 1 va 3 (10⁵ Pa), V = 1 va 3 (10⁻³ m³). Siklda bajarilgan ish?", 400, [200, 800, 100], "J", "A = (3−1)·10⁵·(3−1)·10⁻³ = 2·10⁵·2·10⁻³ = 400 J.", fig=_cy),
    C(3, "Shu sikl V–T koordinatasida qanday ko'rinadi (1→2 izoxor, 2→3 izobar)?", "1→2 vertikal emas: V = const → nuqta T o'zgaradi, vertikal chiziq", ["Giperbola", "Aylana", "Nuqta"], "Izoxor V–T da vertikal chiziq.", ) if False else C(3, "p–V diagrammadagi izoxorik jarayon V–T tekisligida qanday chiziq bo'ladi?", "V o'qiga parallel emas: T o'zgaradi, V o'zgarmaydi — gorizontal chiziq (V = const)", ["Koordinata boshidan o'tuvchi qiya chiziq", "Giperbola", "Aylana"], "V = const → V–T da T o'qiga parallel.") if False else C(3, "Izobarik jarayon V–T koordinatalarida qanday ko'rinadi?", "Koordinata boshidan o'tuvchi qiya to'g'ri chiziq", ["Gorizontal chiziq", "Giperbola", "Vertikal chiziq"], "V = (νR/p)·T."),
    C(3, "Izoxorik jarayon p–T koordinatalarida qanday?", "Koordinata boshidan o'tuvchi qiya to'g'ri chiziq", ["Giperbola", "Gorizontal chiziq", "Parabola"], "p = (νR/V)·T."),
    C(3, "Izotermik jarayon V–T tekisligida qanday?", "T o'qiga perpendikulyar vertikal chiziq", ["Giperbola", "Qiya chiziq", "Gorizontal chiziq"], "T = const."),
    N(3, "Yopiq siklda gaz ish bajaradi: p–V diagrammada sikl yuzi 6 J ga teng. 5 ta shunday sikl ishi?", 30, [6, 1.2, 36], "J", "Har sikl 6 J."),
    C(2, "Siklda soat mili yo'nalishida aylanish nimani bildiradi (p–V da)?", "Gaz musbat (foydali) ish bajaradi", ["Gaz ustida ish bajariladi", "Ish nolga teng", "Gaz sovutiladi"], "Yuqori shoxda kengayish ko'proq ish."),
    ON(3, "p–V da sikl to'rtburchak: p₁ = 1·10⁵, p₂ = 4·10⁵ Pa; V₁ = 2, V₂ = 5 litr. Sikl ishi necha J?", 900, "(4−1)·10⁵·(5−2)·10⁻³ = 900 J."),
    ON(3, "Izobarik kengayish: p = 2·10⁵ Pa, hajm 3 l dan 8 l gacha ortdi. Gaz ishi necha J?", 1000, "A = pΔV = 2·10⁵·5·10⁻³ = 1000."),
]

Q["P10.6"] = [
    C(1, "Dalton qonuni?", "Aralashma bosimi komponentlar parsial bosimlari yig'indisiga teng", ["Aralashma bosimi o'rtacha", "Bosim temperaturaga bog'liq emas", "Faqat bir gaz bosimi"], "p = p₁ + p₂ + ..."),
    N(2, "Idishda 2·10⁵ Pa va 3·10⁵ Pa parsial bosimli ikki gaz. Umumiy bosim?", 500000, [1e5, 600000, 250000], "Pa", "Yig'indi."),
    N(2, "Aralashma: 1 mol He va 3 mol Ar. Ar parsial bosimi umumiy 4·10⁵ Pa da?", 300000, [100000, 400000, 133333], "Pa", "Mol ulushi 3/4."),
    N(3, "Idishda 28 g N₂ (M = 28) va 4 g H₂ (M = 2): umumiy mol soni?", 3, [32, 2, 1], "mol", "1 + 2."),
    N(3, "Shu aralashma (ν = 3 mol, V = 0,0249 m³, T = 300 K): bosim (R = 8,31)?", 300360, [100120, 600720, 150180], "Pa", "νRT/V = 3·8,31·300/0,0249 = 300 361."),
    C(2, "Ikki gaz aralashmasida har birining parsial bosimi...", "agar yolg'iz o'sha hajmni egallasa bo'ladigan bosimga teng", ["umumiy bosimga teng", "nolga teng", "massa bilan teskari"], "Ta'rif."),
    ON(3, "2 l idishda 3 atm bosimli gaz va 3 l idishda 2 atm bosimli gaz mavjud. Idishlar ulanganda (T = const) yangi bosim necha atm? (5 l hajm)", 2.4, "p = (3·2 + 2·3)/5 = 2,4."),
    ON(3, "Havo tarkibi: 80% N₂, 20% O₂ (mol bo'yicha). Umumiy bosim 100 kPa. O₂ parsial bosimi necha kPa?", 20, "0,2·100."),
]

Q["P10.7"] = [
    C(1, "Nisbiy namlik formulasi?", "φ = p / p_to'yingan · 100%", ["φ = p·p_t", "φ = ρ·T", "φ = p_t/p"], "Bug' bosimining to'yingan bosimga nisbati."),
    C(1, "Shudring nuqtasi nima?", "Bug' to'yinadigan temperatura", ["Suvning qaynash nuqtasi", "Muzlash nuqtasi", "Eng issiq temperatura"], "Bug' to'yinib, kondensatsiya boshlanadi."),
    C(1, "Suv qaynash temperaturasi tashqi bosim ortganda...", "ortadi", ["kamayadi", "o'zgarmaydi", "nolga teng"], "Tog'da past, bosim idishda yuqori."),
    N(2, "20 °C da to'yingan bug' bosimi 2,3 kPa. Haqiqiy bosim 1,15 kPa. Nisbiy namlik?", 50, [100, 25, 200], "%", "1,15/2,3."),
    N(3, "Absolyut namlik 10 g/m³, to'yingan bug' zichligi 20 g/m³. Nisbiy namlik?", 50, [200, 10, 30], "%", "10/20."),
    C(2, "To'yingan bug' bosimi temperatura ortganda...", "tez ortadi (chiziqli emas)", ["kamayadi", "o'zgarmaydi", "chiziqli kamayadi"], "Eksponentsial o'sish."),
    C(2, "To'yingan bug' bosimi hajmga...", "bog'liq emas", ["to'g'ri proporsional", "teskari proporsional", "kvadratik bog'liq"], "Faqat temperaturaga bog'liq."),
    ON(3, "Havo 50% namlikda, to'yingan bug' bosimi 4 kPa. Bug' bosimi necha kPa?", 2, "0,5·4."),
    ON(3, "Xonada nisbiy namlik 40%. To'yingan bug' zichligi 25 g/m³ bo'lsa, absolyut namlik necha g/m³?", 10, "0,4·25."),
]

Q["P10.8"] = [
    C(1, "Sirt taranglik koeffitsiyenti formulasi?", "σ = F / l", ["σ = F·l", "σ = F / S", "σ = m / V"], "Kuch chegara uzunligiga."),
    C(1, "Suv shisha kapilyarida...", "ko'tariladi (xo'llaydi)", ["pasayadi", "joyida qoladi", "qaynaydi"], "Menisk botiq."),
    C(1, "Simob shisha kapilyarida...", "pasayadi (xo'llamaydi)", ["ko'tariladi", "tebranadi", "o'zgarmaydi"], "Menisk qavariq."),
    N(2, "σ = 0,07 N/m bo'lgan suvli plyonkaning bir tomoni 10 cm. Kuch?", 0.007, [0.7, 0.07, 0.0007], "N", "F = σl = 0,07·0,1."),
    N(3, "Kapillyarda suv ko'tarilish balandligi: σ = 0,07 N/m, ρ = 1000, r = 0,5 mm, g = 10 (to'liq xo'llash). h?", 0.028, [0.014, 0.056, 0.28], "m", "h = 2σ/(ρgr) = 0,14/(1000·10·0,0005·1) = 0,028 m."),
    C(2, "Kapillyar diametri kichiklashsa, ko'tarilish balandligi...", "ortadi", ["kamayadi", "o'zgarmaydi", "nolga teng"], "h ∼ 1/r."),
    N(3, "Sovun pufagi (ikki sirt), σ = 0,04 N/m, r = 2 cm. Qo'shimcha bosim (Δp = 4σ/r)?", 8, [4, 16, 2], "Pa", "4·0,04/0,02."),
    ON(3, "Suv tomchisi radiusi 1 mm, σ = 0,07 N/m. Laplas bosimi (Δp = 2σ/r) necha Pa?", 140, "2·0,07/0,001 = 140."),
    ON(3, "Kapillyar ichida suv balandligi 4 sm. Radiusi 2 marta kichik kapillyarda balandlik necha sm?", 8, "h ∼ 1/r."),
]

Q["P10.9"] = [
    C(1, "Mexanik kuchlanish formulasi?", "σ = F / S", ["σ = F·S", "σ = ΔL/L", "σ = E·F"], "Kuch ko'ndalang kesim yuzasiga."),
    C(1, "Nisbiy deformatsiya?", "ε = ΔL / L₀", ["ε = L₀/ΔL", "ε = F/S", "ε = E·σ"], "Uzayish nisbiy qiymati."),
    C(1, "Guk qonunining umumiy ko'rinishi?", "σ = E·ε", ["σ = ε/E", "σ = E/ε", "σ = F·ε"], "E — Yung moduli."),
    N(2, "Sterjenga 2000 N kuch, kesimi 4 mm² (4·10⁻⁶ m²). Kuchlanish?", 5e8, [5e5, 8e3, 2e5], "Pa", "2000/4e-6 = 5·10⁸."),
    N(3, "Yung moduli 2·10¹¹ Pa, kuchlanish 4·10⁸ Pa. Nisbiy uzayish?", 0.002, [0.0005, 0.02, 500], "", "ε = σ/E."),
    N(3, "Uzunligi 2 m sterjenning nisbiy uzayishi 0,001. Absolyut uzayish?", 0.002, [0.02, 2, 0.001], "m", "ΔL = ε·L₀ = 0,002."),
    C(2, "Plastik deformatsiya nima?", "Kuch olingach saqlanib qoladigan deformatsiya", ["Kuch olingach yo'qoladigan", "Hech qachon yuz bermaydigan", "Faqat suyuqlikda"], "Qoldiq deformatsiya."),
    C(2, "Mo'rt jism...", "kam deformatsiyada sinadi", ["juda cho'ziladi", "qizdirilganda cho'ziladi", "hech qachon sinmaydi"], "Masalan shisha."),
    ON(3, "Mis sim (E = 1·10¹¹ Pa) kuchlanishi 2·10⁸ Pa. Nisbiy uzayish necha foiz?", 0.2, "ε = 0,002 → 0,2%."),
]

_pv = F.pv_cycle([(1, 1), (1, 3), (3, 3), (3, 1)])
Q["P10.10"] = [
    C(1, "Termodinamikaning birinchi qonuni?", "Q = ΔU + A", ["Q = ΔU − A faqat", "Q = A/ΔU", "ΔU = Q·A"], "Energiyaning saqlanish qonuni."),
    N(1, "Gaz 300 J issiqlik oldi va 100 J ish bajardi. ΔU?", 200, [400, 300, 100], "J", "ΔU = Q − A."),
    N(2, "Bir atomli ideal gazning ichki energiyasi 2 mol, T = 300 K (R = 8,31)?", 7479, [2493, 4986, 14958], "J", "U = (3/2)νRT = 1,5·2·8,31·300 = 7479 J."),
    N(2, "Izoxor jarayonda gaz 500 J issiqlik oldi. Bajarilgan ish?", 0, [500, 250, 1000], "J", "V = const → A = 0."),
    N(2, "Izotermik kengayishda ideal gaz 400 J issiqlik oldi. Ish?", 400, [0, 200, 800], "J", "ΔU = 0 → A = Q."),
    N(3, "Izobar jarayonda p = 2·10⁵ Pa, ΔV = 0,003 m³. Ish?", 600, [60, 6000, 300], "J", "A = pΔV."),
    N(3, "Bir atomli gaz izobar kengayib, ish 400 J. Olingan issiqlik (Q = 5A/2)?", 1000, [400, 600, 1600], "J", "Q = ΔU + A = 1,5A + A."),
    C(2, "Izotermik siqishda ideal gaz ichki energiyasi...", "o'zgarmaydi", ["ortadi", "kamayadi", "nolga teng"], "ΔU = 0 (T = const)."),
    C(2, "Chizmadagi sikl (1→2→3→4→1) soat strelkasi bo'yicha. Gaz...", "foydali ish bajaradi", ["ish bajarmaydi", "sovitiladi", "faqat siqiladi"], "To'g'ri sikl.", fig=_pv),
    ON(3, "Bir atomli ideal gazga izobar jarayonda 500 J issiqlik berildi. Ichki energiya necha J ga ortdi?", 300, "Q = (5/2)A → A = 200; ΔU = 300."),
    M(2, [("Izoxorik", "A = 0"), ("Izotermik", "ΔU = 0"), ("Adiabatik", "Q = 0")], "Birinchi qonunning xususiy hollari."),
]

Q["P10.11"] = [
    C(1, "Adiabatik jarayonda...", "issiqlik almashinuvi yo'q (Q = 0)", ["T = const", "V = const", "p = const"], "Tez jarayon yoki izolyatsiya."),
    C(2, "Adiabatik kengayishda gaz temperaturasi...", "pasayadi", ["ortadi", "o'zgarmaydi", "nolga teng"], "A = −ΔU > 0."),
    C(2, "p–V diagrammada adiabata izotermaga nisbatan...", "tikroq", ["yotiqroq", "bir xil", "to'g'ri chiziq"], "γ > 1."),
    C(2, "Termodinamikaning ikkinchi qonuni nimani ta'kidlaydi?", "Issiqlik o'z-o'zidan sovuqdan issiqqa o'tmaydi", ["Energiya yo'qoladi", "FIK 100% bo'ladi", "Entropiya kamayadi"], "Jarayonlar qaytmas."),
    N(3, "Adiabatik jarayonda gaz 300 J ish bajardi. Ichki energiya o'zgarishi?", -300, [300, 0, 600], "J", "Q = 0 → ΔU = −A."),
    N(3, "Karno sikli: T₁ = 500 K, T₂ = 300 K. Isitkichdan 1000 J olinsa, sovitkichga beriladigan issiqlik?", 600, [400, 300, 1000], "J", "Q₂ = Q₁T₂/T₁ = 1000·0,6."),
    N(3, "Shu siklda foydali ish?", 400, [600, 200, 1000], "J", "A = Q₁ − Q₂."),
    ON(3, "Karno dvigatelida T₁ = 400 K, FIK = 25%. Sovitkich temperaturasi necha K?", 300, "T₂ = T₁(1 − η)."),
    C(2, "Entropiya izolyatsiyalangan sistemada...", "kamaymaydi", ["doim kamayadi", "doim nolga teng", "faqat sovishda ortadi"], "ΔS ≥ 0."),
]

Q["P10.12"] = [
    N(2, "0 °C dagi 100 g muz (λ = 330 kJ/kg) to'liq erishi uchun issiqlik?", 33, [330, 3.3, 66], "kJ", "0,1·330."),
    N(3, "−20 °C li 1 kg muzga 100 °C li suv quyilganda butunlay erib, 0 °C li suv bo'lishi uchun kamida qancha suv? (c_muz = 2100, λ = 330 000, c_suv = 4200)", 0.9, [0.45, 1.8, 0.5], "kg", "(2100·20 + 330000)/(4200·100) = 372000/420000 ≈ 0,886 ≈ 0,9."),
    N(3, "100 °C li 0,1 kg bug' (L = 2,3 MJ/kg) 0 °C gacha sovitilganda ajraladigan issiqlik (suv c = 4200)?", 272000, [230000, 42000, 188000], "J", "230000 + 42000."),
    N(3, "0 °C dagi 0,2 kg muzga 0,05 kg 100 °C bug' kiritildi (λ = 330 kJ/kg, L = 2,3 MJ/kg, c = 4200). Muz erishi uchun 66 kJ kerak; bug' kondensatsiyasi 115 kJ beradi. Muz to'liq eriydimi?", "Ha, issiqlik yetarli", ["Yo'q, issiqlik yetmaydi", "Faqat yarmi eriydi", "Aniqlab bo'lmaydi"], "115 kJ > 66 kJ.") if False else C(3, "0 °C dagi 0,2 kg muz erishi uchun 66 kJ kerak. 0,05 kg 100 °C bug' kondensatsiyalansa 115 kJ ajraladi. Muz to'liq eriydimi?", "Ha, issiqlik yetarli", ["Yo'q, issiqlik yetmaydi", "Faqat yarmi eriydi", "Aniqlab bo'lmaydi"], "115 kJ > 66 kJ."),
    C(2, "Issiqlik balansi tenglamasida ajralgan va olingan issiqlik...", "teng bo'ladi (izolyatsiyalangan sistemada)", ["ajralgani ko'p", "olingani ko'p", "nolga teng"], "Q_ber = Q_ol."),
    ON(3, "500 g 55 °C suvga necha gramm 0 °C muz tashlansa, muz butunlay erib, umumiy temperatura 0 °C bo'ladi? (c = 4200, λ = 330 000 J/kg; faqat gramm)", 350, "0,5·4200·55 = 115 500 J; m = 115 500/330 000 = 0,35 kg = 350 g."),
    ON(3, "0,5 kg 40 °C suvni 0 °C gacha sovitishda ajralgan issiqlik necha kJ? (c = 4200)", 84, "0,5·4200·40 = 84000 J = 84 kJ."),
]
