import json

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
    
    def v_slovar(self):
        return {
            "seznami": [s.v_slovar() for s in self.seznamiReceptov],
            "seznam_za_prikaz": self.seznamiReceptov.index(self.seznamZaPrikaz)
            if self.seznamZaPrikaz
            else None
        }

    @staticmethod
    def iz_slovarja(dict):
        m = Model()
        m.seznamiReceptov = [SeznamReceptov.iz_slovarja(dict_s) for dict_s in dict["seznami"]]
        if dict["seznam_za_prikaz"] is not None:
            m.seznamZaPrikaz = m.seznamiReceptov[dict["seznam_za_prikaz"]]
        return m

    def shrani_datoteko(self, ime_dat):
        with open(ime_dat, "w") as d:
            dict = self.v_slovar()
            json.dump(dict, d)

    @staticmethod
    def preberi_datoteko(ime_dat):
        with open(ime_dat) as d:
            dict = json.load(d)
            return Model.iz_slovarja(dict)


class SeznamReceptov:
    def __init__(self, ime):
        self.ime = ime
        self.recepti = []
    
    def dodajRecept(self, recept):
        self.recepti.append(recept)

    def odstraniRecept(self, recept):
        self.recepti.remove(recept)
    
    def v_slovar(self):
        return {
            "ime": self.ime,
            "recepti": [r.v_slovar() for r in self.recepti]
        }

    @staticmethod
    def iz_slovarja(dict):
        s = SeznamReceptov(dict["ime"])
        s.recepti = [Recept.iz_slovarja(dict_r) for dict_r in dict["recepti"]]
        return s


class Recept:
    def __init__(self, ime, sestavine, postopek, priljubljen):
        self.ime = ime
        self.sestavine = sestavine
        self.postopek = postopek
        self.priljubljen = priljubljen
    
    def v_slovar(self):
        return {
            "ime": self.ime,
            "sestavine": self.sestavine,
            "postopek": self.postopek,
        	"priljubljen": self.priljubljen
        }

    @staticmethod # Recept.iz_slovarja(s)
    def iz_slovarja(dict):
        return Recept(dict["ime"], dict["sestavine"], dict["postopek"], dict["priljubljen"])