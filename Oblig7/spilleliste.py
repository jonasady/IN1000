from sang import Sang
#Importerer klassen Sang fra filen sang.py

class Spilleliste:
#Lager en klasse: Spilleliste
    def __init__(self, listenavn):
    #Lager tilhørende konstruktør, som er listenavn
        self._sanger = []
        #Lager en tom liste, som er lagret i self._sanger
        self._navn = listenavn
        #Lager tilhørende instansvariabel til listenavn som er self._navn

    def lesFraFil(self, filnavn):
    #Lager lesFraFil, med self og filnavn som parameter
        fil = open(filnavn)
        #Åpner filen som er gitt i verdien av i filnavn og lagres i fil
        for linje in fil:
        #Går gjennom fil i en forløkke
            alleData = linje.strip().split(';')
            #Splitter enkeltverdiene i fil og striper for linjeskift
            sang = Sang(alleData[0] , alleData[1])
            #Legger til verdier i klassen sang som er første og andre verdi i alle data og går gjennom alle punktene i listen(med hjelp fra for-løkka)
            self._sanger.append(sang)
            #Legger til sang i lista self._sanger
        return fil
        #Returnerer fil
        fil.close()
        #Stenger fil
    def leggTilSang(self, nySang):
    #Lager leggTilSang, med parameter nySang
        return self._sanger.append(nySang)
        #Returnerer self._sanger, hvorav nySang er legget til i lista

    def fjernSang(self, sang):
    #Lager fjernSang med parameter sang
        return self._sanger.remove(sang)
        #Returnerer self._sanger, hvorav sang er fjernet, som også er parameter (sang)

    def spillSang(self, sang):
    #Lager spillSang med sang som parameter
        return sang.spill()
        #Returner sang, med funksjonen spill som er en funksjon fra sang.py som er importert

    def spillAlle(self):
    #Lager spillAlle
        for i in self._sanger:
        #Går gjennom self._sanger i en for-løkke
            i.spill()
            #Skriver funksjonen spill() hvorav i er lagt som tilhørende verdi

    def finnSang(self, tittel):
    #Lager finnSang med tittel som parameter
        for i in self._sanger:
        #Går igjennom self._sanger i for-løkke
            if i.sjekkTittel(tittel) == True:
            #Om sjekkTittel med tittel for parameter er True vil programmet returnere i
                return i
        return None
        #Om ikke vil det returnere None

    def hentArtistUtvalg(self,artistnavn):
    #Lager hentArtistUtvalg med artistnavn som parameter
        sangliste = []
        #Lager listen sangliste
        for i in self._sanger:
        #Går gjennom sanger i en for-løkke
            if i.sjekkArtist(artistnavn) == True:
            #Om i.sjekkartist med artistnavn som verdi for parameteret er true vil i legges til i listen sangliste
                sangliste.append(i)
        return sangliste
        #Returnerer sangliste
