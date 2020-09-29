
maaltider_navn = {"Tor Hansen": ["tomatbønner, egg og bacon til frokst", "pastasalat til lunsj", "pizza grandiosa til middag"] }
#Lager en ordbok hvor navnet på beboeren er nøkkelverdien og lista som hører til nøkkelverdien med de tre måltidene.
def prosedyre():
#Lager en prosedyre med navnet prosedyre
    sok_navn = input("Søk på et navn: ")
    #Lager et inputfelt hvor brukeren skal skrive inn et navn
    if sok_navn in maaltider_navn:
    #Sier at om sok_navn, som er skrevet inn fra brukeren finnes som nøkkelverdi maaltider_navn vil nøkkelverdien med
    #tilhørende liste skrives ut.
        print (maaltider_navn[sok_navn])
    else:
        #om ikke premisset i if-setningen er oppfylt vil programmet skrive ut "Beboeren er ikke registrert".
        print("Beboeren er ikke registrert")
prosedyre()
#Skriver ut prosedyren

#3a) For å ha oversikt over kun brukernavn til IN1000-studenter ville jeg brukt en liste fordi man skal sette
#opp flere enkelverdier etterhverandre, som eksempelvis (toror200, feli33 etc...)
#men om man skal sammenligne navn og brukernavn ville jeg brukt en ordbok fordi man lett kan
#koble navn til brukernavn, for eksempel: liste = {totor200: Tor Torsen, feli33: Felix}

#3b) For å se poengene til studenter ved innlevering av oblig3 ville jeg ha brukt en ordbok fordi
#en er nødt til å koble navn til poeng. Da ville jeg eksempelvis brukt navn som nøkkelverdi for å finne
#tilhørende poeng

#3c) For å finne lotto-vinnere siste år ville jeg ha brukt en liste med navn. Siden oppgaven spør om man
#kun skal bruke navn etter hverandre, og ikke koble det opp mot dato er det naturlig å bruke liste.
#Listen har en og en verdi etterhverandre, og ikke flere verdier som hører til hverandre i like stor grad
#som ordbøker, som kobler en nøkkelverdi til andre verdier. Men siden det kun er navn man skal ha, og ikke
#tilhørende data som gjør at man må ha en nøkkelverdi, er det naturlig i dette tilfellet å bruke liste.

#3d) For å kartlegge allergier til gjester i et selskap ville jeg brukt mengde. Ved hjelp av mengde
#teller man antall ganger noen er allergisk mot noe. Ved å sette opp allergier i en mengde vil altså
#man kunne telle antall ganger eksempel gluten blir nevnt.
