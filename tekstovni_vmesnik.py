from model import Model, SeznamReceptov, Recept

DODAJ_SEZNAM = 1
BRISI_SEZNAM = 2
DODAJ_RECEPT = 3
BRISI_RECEPT = 4
ZAMENJAJ_SEZNAM = 5
IZHOD = 6
DODAJ_PRILJUBLJENIM = 7
ODSTRANI_IZ_PRILJUBLJENIH = 8


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