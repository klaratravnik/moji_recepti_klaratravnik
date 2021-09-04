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



@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)