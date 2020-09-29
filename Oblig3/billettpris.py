def prosedyre_navn():
#Lager en prosedyre med navnet prosedyre_navn
    alder = int(input("Skriv inn alderen din: "))
    #Ber brukeren skrive inn alderen, dette blir lagret som et heltall med int() i variablen alder
    billettpris = 0
    #Lager vriabelen billettpris som har verdien 0

    if alder <= 17:
    #Sier at om alderen er 17 eller mindre vil bilettpris bli 30
        billettpris = 30
    elif alder > 17 and alder < 63:
    #Sier at om alder er mer enn 17 og mindre enn 63 vil billettpris være 50
        billettpris = 50
    else:
    #Om ikke kravene i elif- eller if setningen være oppfylt vil bilettpris være 35. Det skjer om
    #brukeren skriver et tall som er 63 eller høyere
        billettpris = 35

    print("Du er " + str(alder) + " år og må betale " + str(billettpris) + " kr for en bilett")
    #Printer ut tekst kombinert med alder og bilettpris, som er gjort om til en streng for å
    #være lovlig kode.
prosedyre_navn()
prosedyre_navn()
prosedyre_navn()
prosedyre_navn()
#Skriver ut prosedyren 4 ganger

#4) Brukere vil kunne skrive useriøse høye aldere, som blir menningsløse data i dette kodesettet.
# Om eksempelvis brukeren skriver inn 200 år vil ikke programmet ha noe tak og ta inn alderen
#og skrive ut at man må betale 35kr for en bilett. Man burde i denne koden derfor sette et tak med en gang
#med en if kode som sier eksempelvis at om alderen er høyere enn 110 vil man ikke kunne få ut noen bilettpris.
