from model import Model, SeznamReceptov, Recept

DODAJ_SEZNAM = 1
BRISI_SEZNAM = 2
DODAJ_RECEPT = 3
BRISI_RECEPT = 4
ZAMENJAJ_SEZNAM = 5
IZHOD = 6
DODAJ_PRILJUBLJENIM = 7
ODSTRANI_IZ_PRILJUBLJENIH = 8

IME_DAT = "model.json"
try:
    m = Model.preberi_datoteko(IME_DAT)
except FileNotFoundError:
    m = Model()

def dodaj_seznam():
    s = SeznamReceptov(input("Vnesi ime seznama: "))
    m.dodajSeznam(s)

def brisi_seznam():
    print("Izberite seznam, za izbris.")
    s = izberi_seznam()
    m.odstraniSeznam(s)

def dodaj_recept():
    print("Vnesite podatke novega recepta.")
    r = Recept("Kuhana jajca", "Jajce", "Skuhaj jajce", False)  # za testiranje
    m.dodajRecept(r)

def brisi_recept():
    r = izberi_recept()
    m.odstraniRecept(r)

def zamenjaj_seznam():
    print("Izberite seznam, na katerega bi preklopili: ")
    s = izberi_seznam()
    m.zamenjajAktualniSeznam(s)

def izberi_seznam():
    i = 1
    for seznam in m.seznamiReceptov:
        print(f"{i}.: {seznam.ime}")
        i += 1
    return m.seznamiReceptov[(int(input("Vnesi stevilko seznama: "))) - 1]

def izberi_recept():
    i = 1
    for recept in m.seznamZaPrikaz.recepti:
        print(f"{i}.: {recept.ime}")
        i += 1
    return m.seznamZaPrikaz.recepti[(int(input("Vnesi stevilko recepta: "))) - 1]

def izpisi_recept(recept): # tukaj se lahko se kej doda
    return (f"{recept.ime}")

def seznam_za_prikaz():
    print("IZPISUJEM RECEPTE")
    if m.seznamZaPrikaz:
        for recept in m.seznamZaPrikaz.recepti:
            print(f"- {izpisi_recept(recept)}")
    else:
        print("Dodajte prvi seznam.")
        dodaj_seznam()

def izberi_ukaz(ukazi):
    for (st, opis) in ukazi:
        print(opis)
    return int(input("Izberite naslednji ukaz: "))

while True:
    seznam_za_prikaz()
    ukaz = izberi_ukaz(
        [
            (DODAJ_SEZNAM, "1. Dodaj nov seznam"),
            (BRISI_SEZNAM, "2. Briši seznam"),
            (DODAJ_RECEPT, "3. Dodaj recept"),
            (BRISI_RECEPT, "4. Brisi recept"),
            (ZAMENJAJ_SEZNAM, "5. Zamenjaj seznam"),
            (IZHOD, "6. Izhod")
        ]
    )
    if ukaz == DODAJ_SEZNAM:
        dodaj_seznam()
    elif ukaz == BRISI_SEZNAM:
        brisi_seznam()
    elif ukaz == DODAJ_RECEPT:
        dodaj_recept()
    elif ukaz == BRISI_RECEPT:
        brisi_recept()
    elif ukaz == ZAMENJAJ_SEZNAM:
        zamenjaj_seznam()
    elif ukaz == IZHOD:
        m.shrani_datoteko(IME_DAT)
        print("Nasvidenje!")
        break