class Sang:
#Lager klassen Sang
    def __init__ (self, tittel, artist):
    #Lager konstrøktør med tittel og artist i tillegg til self
        self._tittel = tittel
        self._artist = artist
        #Definerer innstansevariabelene tittel og artist
    def spill(self):
        print("Spiller " + self._tittel + " av " + self._artist)
        #Printer self._tittel og self._artist med tilhørende tekst
    def sjekkArtist(self, navn):
    #Lager sjekkartist med navn og self som parameter
        liste = self._artist.split()
        #Splitter self._artist og lagrer det i liste
        navn =  navn.split()
        #splitter navn og lagrer det igjen i navn
        riktig = 0
        #Setter variabelen riktig til 0
        for i in liste:
        #Går gjennom liste i forløkke
            if i in navn:
            #Om i-gitte verdi finnes i liste navn vil riktig plusses med 1
                riktig += 1
        if riktig > 0:
        #Om riktig er større enn 1 vil det returnere True
            return True
        else:
        #Om ikke returnerer programmet False
            return False
    def sjekkTittel(self, tittel):
    #Lager sjekkTittel med parameter self og tittel

        if tittel.upper() == self._tittel.upper():
            return True
        #Alt i tittel og self._tittel gjøres om til store bokstaver og om de er like vil programmet returnere true
        else:
            return False
        #Om ikke vil det returnere false
    def sjekkArtistogTittel(self, navn, tittel):
    #Lager sjekkArtistogTittel med (self), navn og tittel som parameter
        if self.sjekkArtist(navn)== True and self.sjekkTittel(tittel) == True:
        #Sjekker om funksjonen sjekkArtist og sjekkTittel er true, om så er tiflelle returnerer programmet true
            return True
        else:
        #Om ikke returnerer programmet false
            return False
