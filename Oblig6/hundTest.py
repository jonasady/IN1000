from hund import hund
#Importerer klassen hund
def hovedprogram():
#Lager prosedyren hovedprogram
    min_hund = hund(10, 8)
    #Lager et nytt objekt, min_hund, som har verdiene 10, som er vekt, og alder, som er satt til 8, fra klassen hund

    for i in range(3):
    #Lager en for-løkke som går igjennom min_hund.spring() 3 ganger
        min_hund.spring()


    for i in range(5):
    #Lager en for-løkke som går gjennom min_hund.spis(1) 3 ganger, slik at hunden vil "spise 3 ganger
        min_hund.spis(1)

    assert min_hund.vekt() == 15
    #Sjekker om at vekten stemmer overens med det som er menningen

    min_hund.vekt_og_alder()
    #Skriver ut vekt og alder med metoden vekt_og_alder() i klassen
hovedprogram()
#Skriver ut hovedprogram
