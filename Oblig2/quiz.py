
#Skriv ut "velkommen til quiz!"
print("Velkommen til quiz!")

#Lag deretter 3 spørsmål om valgfritt tema. Brukeren skal selv skrive inn
#svaret i et inputfelt og programmet skal skrive ut feil- eller riktig
#svar.
def feil_svar():
    print("Feil svar!")
#lager en prosedyre slik at man slipper å skrive "Feil svar" gjentatte ganger
def riktig_svar():
    print("Riktig svar!")
    #lager en prosedyre slik at man slipper å skrive "Riktig svar" gjentatte ganger

#Lag et poengsystem hvor brukeren får oppgitt hvor mange poeng brukeren
#har på slutten av quizen
poeng = 0
#lager en variabel for poeng som adderes ettersom man får rett

sporsmaal1 = input("Hva er hovedstaten i Italia?")
#skriver ut et inputfelt hvor brukeren må selv skrive inn
if (sporsmaal1 == "Milano"):
#Sier om Milano er skrevet inn i inputfeltet vil hendelsene i de to radene nedover skje
    riktig_svar()
    #skriver ut prosedyren
    poeng = poeng + 1
    #adderer 1 poeng med variabelen "poeng" slik at variabelen poeng nå blir 0+1, altså 1
else:
    #om ikke svaret er Milano vil prosedyren nederst bli skrevet ut
    feil_svar()


sporsmaal2 = input("Hvilken farge har Napoleons hvite hest?")
#skriver ut et inputfelt hvor brukeren må selv skrive inn
if (sporsmaal2 == "hvit"):
    #Sier om hvit er skrevet inn i inputfeltet vil hendelsene i de to radene nedover skje
    riktig_svar()
    poeng = poeng + 1
    #adderer 1 poeng med variabelen "poeng" slik at variabelen poeng nå blir eksempelvis 1+1,
    #altså 2 om man har et poeng fra før, om ikke blir poeng 1 om man har riktig på dette spørsmålet
else:
    feil_svar()
    #om ikke svaret er hvit vil prosedyren nederst bli skrevet ut
sporsmaal3 = int(input("Hvor mange partier er det på Stortinget?"))
#skriver ut et inputfelt hvor svaret til brukeren blir lagret som et tall med int og
#svaret blir lagret i variabelen sporsmaal3
if (sporsmaal3 == 9):
#Om sporsmaal3 er 9 vil de to neste linjene skrives ut
    riktig_svar()
    poeng = poeng + 1
else:
    feil_svar()
#Til slutt skal programmet skrive ut "Det var det, takk for innsatsen"
#når quizen er ferdig i tillegg til totale poeng
print("Det var det, takk for innsatsen. Poeng: " + str(poeng))
#Skriver ut tekst i tillegg til poeng, som er gjort om til en streng for å være gyldig med
#resten av string-elementene i print-feltet.
