from flask import Flask, render_template
import othello.gra
app = Flask(__name__)

aktualna_gra = othello.gra.Gra()

@app.route('/')
@app.route('/gra', methods=['GET', 'POST'])
@app.route('/gra/<int:x>/<int:y>', methods=['GET'])
def gra(x=None, y=None):
    komunikat = ""
    if (x and y) is not None:
        komunikat = ""
        if aktualna_gra.wykonaj_ruch(x, y):
            aktualna_gra.aktualizuj_plansze(x, y)
            aktualna_gra.aktualizuj_wyniki()
            aktualna_gra.nastepny_gracz()
            if aktualna_gra.czy_koniec():
                zwyciezca = aktualna_gra.zwyciezca()
                komunikat = "Koniec gry! %s" % zwyciezca
            elif not aktualna_gra.czy_mozliwy_ruch():
                komunikat = "Brak mozliwosci ruchu"
                aktualna_gra.nastepny_gracz()
        else:
            komunikat = "Niepoprawny ruch"

    return render_template("gra.html", gra=aktualna_gra, komunikat=komunikat)

@app.route('/reset')
def reset():
    komunikat = "Gra zostala zresetowana"
    global aktualna_gra
    aktualna_gra = othello.gra.Gra()
    return render_template("gra.html", gra=aktualna_gra, komunikat=komunikat)