liczba_akcji = int(input())


class Biblioteka():
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.ewidencja = 1

spis = {}

class Czytelnik:
    def __init__(self, imie_nazw):
        self.imie_nazw = imie_nazw
        self.ile_wypo = 0
        self.spis = {}

czytelnicy = {}

def akcje(akcja, tytul, autor, rok=None):
    def dodaj(tytul, autor, rok):
        if tytul in spis:
            spis[tytul].ewidencja += 1
        else:
            spis[tytul] = Biblioteka(tytul, autor, rok)
        return True


    def wypozycz(imie_nazw, tytul):
        if czytelnicy[imie_nazw].ile_wypo == 3:
            return False
        else:
            if tytul in spis:
                if spis[tytul].ewidencja >= 1 and tytul not in czytelnicy[imie_nazw].spis:
                    czytelnicy[imie_nazw].ile_wypo += 1
                    spis[tytul].ewidencja -= 1
                    czytelnicy[imie_nazw].spis[tytul] = tytul
                    return True
            return False


    def oddaj(imie_nazw, tytul):
        if imie_nazw in czytelnicy:
            if tytul in czytelnicy[imie_nazw].spis:
                czytelnicy[imie_nazw].ile_wypo -= 1
                spis[tytul].ewidencja += 1
                del czytelnicy[imie_nazw].spis[tytul]
                return True
        return False


    if akcja == 'dodaj':
        return dodaj(tytul, autor, rok)
    elif akcja == 'wypozycz':
        if tytul not in czytelnicy:
            czytelnicy[tytul] = Czytelnik(tytul)
        return wypozycz(imie_nazw=tytul, tytul=autor)
    elif akcja == 'oddaj':
        return oddaj(imie_nazw=tytul, tytul=autor)




for ilosc in range(liczba_akcji):
    nowa = eval(input())
    akcja = nowa[0].strip()
    tytul = nowa[1].strip()
    autor = nowa[2].strip()
    if len(nowa) > 3:
        rok = nowa[3]
        print(akcje(akcja, tytul, autor, rok))
    else:
        print(akcje(akcja, tytul, autor))
