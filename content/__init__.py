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
    return packs
