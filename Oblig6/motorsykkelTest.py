from motorsykkel import motorsykkel
#Importerer klassen motorsykkel fra filen motorsykkel

def hovedprogram():
#Lager et nytt prosedyren, hovedprogram
    motorsykkel1 = motorsykkel("Harvey Davidson", 2321245, 234)
    motorsykkel2 = motorsykkel("Toyota", 2030504, 190)
    motorsykkel3 = motorsykkel("Honda" , 2030505, 321)
    #Lager tre nye objekter med forskjellige klasseverdier
    motorsykkel1.skrivUt()
    motorsykkel2.skrivUt()
    motorsykkel3.skrivUt()
    #Skriver ut disse objektene med prosedyren skrivUt() i klassen motorsykkel
hovedprogram()
#Kaller på hovedprogram
