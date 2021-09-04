class Model:
    def __init__(self):
        self.seznamiReceptov = []
        self.seznamZaPrikaz = None
        #self.VSI_RECEPTI = 0
        #self.PRILJUBLJENI = 1


class SeznamReceptov:
    def __init__(self, ime):
        self.ime = ime
        self.recepti = []


class Recept:
    def __init__(self, ime, sestavine, postopek, priljubljen):
        self.ime = ime
        self.sestavine = sestavine
        self.postopek = postopek
        self.priljubljen = priljubljen