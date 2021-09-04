class Model:
    def __init__(self):
        self.seznamiReceptov = []
        self.seznamZaPrikaz = None
        #self.VSI_RECEPTI = 0
        #self.PRILJUBLJENI = 1
    
    def dodajSeznam(self, seznam):
        self.seznamiReceptov.append(seznam)
        if not self.seznamZaPrikaz:
            self.seznamZaPrikaz = seznam

    def odstraniSeznam(self, seznam): # kle so bugi še (kaj če tega seznama sploh ni?, kaj prikazati, ko je seznamReceptov prazen itd.)
        self.seznamiReceptov.remove(seznam)

    def zamenjajAktualniSeznam(self, seznam):
        self.seznamZaPrikaz = seznam

    def dodajRecept(self, recept):
        #self.seznamiReceptov[self.VSI_RECEPTI].dodajRecept(recept)
        if self.seznamZaPrikaz is not None:    # kle je še mau za razmislt kako to use dela
            self.seznamZaPrikaz.dodajRecept(recept)

    def odstraniRecept(self, recept):
        #self.seznamiReceptov[self.VSI_RECEPTI].odstraniRecept(recept)
        self.seznamZaPrikaz.odstraniRecept(recept)


class SeznamReceptov:
    def __init__(self, ime):
        self.ime = ime
        self.recepti = []
    
    def dodajRecept(self, recept):
        self.recepti.append(recept)

    def odstraniRecept(self, recept):
        self.recepti.remove(recept)


class Recept:
    def __init__(self, ime, sestavine, postopek, priljubljen):
        self.ime = ime
        self.sestavine = sestavine
        self.postopek = postopek
        self.priljubljen = priljubljen