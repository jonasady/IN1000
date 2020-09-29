class motorsykkel:
#Lager klassen motorsykkel
    def __init__(self, merke, registreringsnavn, km):
    #Legger til merke, registreringsnavn og km (i tillegg til self), som innstansvariabel
        self._merke = merke
        self._registreringsnavn = registreringsnavn
        self._km = km
        #Definerer merke, km og registreringsnavn fra innstansvariabelen


    def kjor(self, km):
        self._km += km
        #Plusser self_.km med km som er parameteret for funksjonen

    def hentKilometerAvstand(self):
        return self._km
        #Returner verdien self._km

    def skrivUt(self):
        print(" Merke: " + self._merke + "\n Registeringsnummer: " + str(self._registreringsnavn) + "\n Kilometer kjørt: " + str(self._km) + "\n")
    #Printer ut self._merke, self._registreringsnavn og self._km med tilhørende tekst
