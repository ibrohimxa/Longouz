"""Tayyor savollar va mavzular bazasi (tarix: sinflar kesimida; biologiya, kimyo, fizika, matematika: DTM)."""


def load_packs():
    packs = []
    try:
        from . import sci_figq
        sci_figq.apply()
    except ImportError:
        pass
    try:
        from . import history
        packs.append(history.pack())
    except ImportError:
        pass
    try:
        from . import biology
        packs.append(biology.pack())
    except ImportError:
        pass
    try:
        from . import chemistry
        packs.append(chemistry.pack())
    except ImportError:
        pass
    try:
        from . import physics
        packs.append(physics.pack())
    except ImportError:
        pass
    try:
        from . import native
        packs.append(native.pack())
    except ImportError:
        pass
    # Matematika: asosiy nazariy (mathematics.py) + chizmali (math_fig.py) birlashtiriladi
    try:
        from . import mathematics
        packs.append(mathematics.pack())
    except ImportError:
        pass
    try:
        from . import math_fig
        packs.append(math_fig.pack())
    except ImportError:
        pass
    for mod in ("english", "russian"):
        try:
            m = __import__(f"{__name__}.{mod}", fromlist=["pack"])
            packs.append(m.pack())
        except ImportError:
            pass
    # v215: hisoblanadigan (to'g'riligi kafolatlangan) qo'shimcha savollar
    try:
        from . import gen_v215
        gen_v215.extend(packs)
    except Exception as e:  # pragma: no cover
        import logging
        logging.getLogger(__name__).warning("gen_v215 yuklanmadi: %s", e)
    try:
        from . import gen_v217
        gen_v217.extend(packs)
    except Exception as e:  # pragma: no cover
        import logging
        logging.getLogger(__name__).warning("gen_v217 yuklanmadi: %s", e)
    apply_quota_tiers(packs)
    return packs


# Mavzu bo'yicha savol kvotasi: Bepul 25, Pro jami 60 (≈2,4×), Ultra jami ~125 (≈5×)
QUOTA_FREE, QUOTA_PRO, QUOTA_ULTRA = 25, 60, 125


def apply_quota_tiers(packs):
    """Har mavzudagi savollarni qiyinlik va turi bo'yicha aralashtirib, tartib bo'yicha tarifga biriktiradi:
    birinchi 25 ta -> Bepul, keyingi 35 ta -> Pro, qolgani -> Ultra. Bepul to'plamda yozma/moslashtirish ham bo'ladi."""
    import hashlib
    from collections import defaultdict
    for pack in packs:
        by_topic = defaultdict(list)
        for q in pack["questions"]:
            by_topic[q.get("topic")].append(q)
        for items in by_topic.values():
            def h(q):
                return hashlib.md5(q["question"].strip().lower().encode()).hexdigest()
            groups = defaultdict(list)
            for q in sorted(items, key=h):
                kind = "c" if q.get("qtype", "closed") == "closed" else "x"
                groups[(q.get("difficulty", 2), kind)].append(q)
            order = [(1, "c"), (2, "c"), (3, "c"), (2, "x"), (1, "x"), (2, "c"), (3, "x")]
            seq = []
            while any(groups.values()):
                for k in order:
                    if groups.get(k):
                        seq.append(groups[k].pop(0))
                for k in list(groups):
                    if k not in order and groups[k]:
                        seq.append(groups[k].pop(0))
            for i, q in enumerate(seq):
                n = len(seq)
                # savol kam bo'lsa ham pullik tariflarda qo'shimcha savol qolishi uchun ulush ishlatiladi
                f_cut = min(QUOTA_FREE, max(4, round(n * 0.45)))
                p_cut = min(QUOTA_PRO, max(f_cut + 1, round(n * 0.75)))
                q["min_plan"] = 0 if i < f_cut else (1 if i < p_cut else 2)
    return packs
