import bottle
import os
from model import Model, SeznamReceptov, Recept

def nalozi_uporabnikovo_stanje():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    if uporabnisko_ime:
        return Model.preberi_datoteko(uporabnisko_ime)
    else:
        bottle.redirect("/prijava/")



def shrani_uporabnikovo_stanje(m):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    m.shrani_datoteko(uporabnisko_ime)



@bottle.get("/registracija/")
def registracija_get():
    return bottle.template("registracija.html", napake={}, polja={}, uporabnisko_ime=None)



@bottle.post("/registracija/")
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime že obstaja."}
        return bottle.template("registracija.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
        Model().shrani_datoteko(uporabnisko_ime)
        bottle.redirect("/")



@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napake={}, polja={}, uporabnisko_ime=None)



@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if not os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime ne obstaja."}
        return bottle.template("prijava.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
        bottle.redirect("/")



@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    print("piškotek uspešno pobrisan")
    bottle.redirect("/")



@bottle.get('/')
def osnovna_stran():
    m = nalozi_uporabnikovo_stanje()
    return bottle.template(
        'osnovna_stran.html',
        stPriljubljenih = m.steviloPriljubljenih(),
        recepti = m.seznamZaPrikaz.recepti if m.seznamZaPrikaz else [],
        seznami = m.seznamiReceptov,
        seznamZaPrikaz = m.seznamZaPrikaz,
        uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime"),
    )



@bottle.post("/zamenjaj-seznam-za-prikaz/")
def zamenjaj_seznam_za_prikaz():
    print(dict(bottle.request.forms))
    indeks = bottle.request.forms.getunicode("indeks")
    m = nalozi_uporabnikovo_stanje()
    seznam = m.seznamiReceptov[int(indeks)]
    m.seznamZaPrikaz = seznam
    shrani_uporabnikovo_stanje(m)
    bottle.redirect("/")



@bottle.get("/dodaj-seznam/")
def dodaj_seznam_get():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    return bottle.template("dodaj_seznam.html", napake={}, polja={}, uporabnisko_ime=uporabnisko_ime)



@bottle.post("/dodaj-seznam/")
def dodaj_seznam_post():
    ime = bottle.request.forms.getunicode("ime")
    polja = {"ime": ime}
    m = nalozi_uporabnikovo_stanje()
    napake = m.preveri_podatke(ime)
    if napake:
        return bottle.template("dodaj_seznam.html", napake=napake, polja=polja)
    else:
        seznam = SeznamReceptov(ime)
        m.dodajSeznam(seznam)
        shrani_uporabnikovo_stanje(m)
        bottle.redirect("/")



@bottle.post("/dodaj-recept/")
def dodaj_recept():
    ime = bottle.request.forms.getunicode("ime")
    sestavine = bottle.request.forms.getunicode("sestavine")
    postopek = bottle.request.forms.getunicode("postopek")
    recept = Recept(ime, sestavine, postopek, False)
    m = nalozi_uporabnikovo_stanje()
    m.dodajRecept(recept)
    shrani_uporabnikovo_stanje(m)
    bottle.redirect("/")



@bottle.post("/priljubljenost/")
def priljubljenost():
    indeks = bottle.request.forms.getunicode("indeks")
    m = nalozi_uporabnikovo_stanje()
    recept = m.seznamZaPrikaz.recepti[int(indeks)]
    recept.togglePriljubljenost()
    shrani_uporabnikovo_stanje(m)
    bottle.redirect("/")


@bottle.post("/odstrani-recept/")
def priljubljenost():
    indeks = bottle.request.forms.getunicode("indeks")
    m = nalozi_uporabnikovo_stanje()
    recept = m.seznamZaPrikaz.recepti[int(indeks)]
    m.odstraniRecept(recept)
    shrani_uporabnikovo_stanje(m)
    bottle.redirect("/")



@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)