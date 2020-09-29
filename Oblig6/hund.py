class hund:
#Lager klassen hund
    def __init__(self, vekt, alder):
    #Legger til vekt og alder som innstansvariabel
        self._vekt=vekt
        self._alder=alder
        self._metthet = 10
        #Definerer innstansvariabelene, i tillegg til å definere self._metthet
    def spring(self):
    #lager metoden spring
        self._metthet-=1
        #Trekker fra self._metthet med 1
        if 5>self._metthet:
        #Om self._metthet er midnre enn 5 vil vekten gå ned med 1
            self._vekt-=1

    def spis(self, mat):
    #Lager metoden spis, med mat som argument
        self._metthet+= mat
        #Plusser på self._metthet med mat
        if 7<self._metthet:
        #Om self._metthet er større enn 7 vil self._vekt plusses på med 1
            self._vekt+= 1

    def vekt(self):
        return self._vekt
        
    def vekt_og_alder(self):
        #Skriver ut vekt og alder med tilhørende tekst
        print("Vekt:" +str(self._vekt) + " Kg"+ "\nAlder: "+ str(self._alder) + " år")
