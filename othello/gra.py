class Gra:
    def __init__(self):
        self.plansza = [[0] * 8 for i in range(8)]
        self.wymiar_x = range(0, 8)
        self.wymiar_y = range(7, -1, -1)
        self.czarny_wynik = 0
        self.bialy_wynik = 0
        self.aktualny_gracz = "czarny"
        self.plansza[3][4] = "bialy"
        self.plansza[3][3] = "czarny"
        self.plansza[4][4] = "czarny"
        self.plansza[4][3] = "bialy"
        self.aktualizuj_wyniki()

    def nastepny_gracz(self):
        if self.aktualny_gracz == "czarny":
            self.aktualny_gracz = "bialy"
        else:
            self.aktualny_gracz = "czarny"

    def aktualny_stan(self, x, y):
        if self.plansza[x][y] == 0:
            return "puste"
        else:
            return self.plansza[x][y]

    def wykonaj_ruch(self, x, y):
        if (self.plansza[x][y] == 0) and (len(self.mozliwy_ruch(x, y)) > 0):
            self.plansza[x][y] = self.aktualny_gracz
            return True
        else:
            return False

    def aktualizuj_wyniki(self):
        wyniki_czarny = 0
        wyniki_bialy = 0
        for wiersz in self.plansza:
            for pole in wiersz:
                if pole == "czarny":
                    wyniki_czarny = wyniki_czarny + 1
                elif pole == "bialy":
                    wyniki_bialy = wyniki_bialy + 1
        self.czarny_wynik = wyniki_czarny
        self.bialy_wynik = wyniki_bialy

    def poza_plansza(self, x, y):
        if (-1 < x < 8) and (-1 < y < 8):
            return False
        else:
            return True

    def aktualizuj_plansze(self, x_start, y_start):
        do_zaktualizowania = self.mozliwy_ruch(x_start, y_start)
        self.aktualizuj_pole(do_zaktualizowania)

    def aktualny_przeciwnik(self):
        if self.aktualny_gracz == "czarny":
            return "bialy"
        else:
            return "czarny"

    def aktualizuj_pole(self, do_zaktualizowania):
        for x, y in do_zaktualizowania:
            self.plansza[x][y] = self.aktualny_gracz

    def czy_koniec(self):
        for wiersz in self.plansza:
            for pole in wiersz:
                if pole == 0:
                    return False
        return True

    def zwyciezca(self):
        self.aktualizuj_wyniki()
        if self.czarny_wynik > self.bialy_wynik:
            return "Wygrywa czarny!"
        elif self.bialy_wynik > self.czarny_wynik:
            return "Wygrywa bialy!"
        else:
            return "Remis!"

    def czy_mozliwy_ruch(self):
        for x in self.wymiar_x:
            for y in self.wymiar_y:
                if self.plansza[x][y] == 0:
                    if len(self.mozliwy_ruch(x, y)) > 0:
                        return True
        return False

    def mozliwy_ruch(self, x_start, y_start):
        do_zaktualizowania = []
        for x_kierunek, y_kierunek in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:

            x = x_start
            y = y_start
            x = x + x_kierunek
            y = y + y_kierunek
            mozliwe_do_zaktualizowania = []
            if self.poza_plansza(x, y):
                print("Poza plansza (%d, %d)" % (x, y))
                continue

            while self.plansza[x][y] == self.aktualny_przeciwnik():
                print("Przeciwnik (%d, %d)" % (x, y))
                mozliwe_do_zaktualizowania.append((x, y))
                print("Mozliwe do zaktualizowania")
                print(mozliwe_do_zaktualizowania)
                x = x + x_kierunek
                y = y + y_kierunek
                if self.poza_plansza(x, y):
                    print("Poza plansza (%d, %d)" % (x, y))
                    break

            if self.poza_plansza(x, y):
                print("Poza plansza (%d, %d)" % (x, y))
                continue
            if self.plansza[x][y] == 0:
                print("Puste pole (%d, %d)" % (x, y))
                continue
            if self.plansza[x][y] == self.aktualny_gracz:
                print("Moje pole (%d, %d)" % (x, y))
                do_zaktualizowania = do_zaktualizowania + mozliwe_do_zaktualizowania
        print("Pelna tablica do zaktualizowania")
        print(do_zaktualizowania)
        return do_zaktualizowania