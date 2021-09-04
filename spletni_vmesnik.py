import bottle
import os
from model import Model, SeznamReceptov, Recept


@bottle.get('/')
def osnovna_stran():
    m = nalozi_uporabnikovo_stanje() # dodaj funkcijo za branje modela
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