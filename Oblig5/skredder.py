

#Skriv et beregningsprogram for skreddere med en
#funksjon som leser inn en fil (som du lager selv og leverer sammen med de andre
#filene) der hver linje beskriver et navn på et mål og selve målet i tommer. Formatet vil
#se slik ut:
#Skulderbredde 4
#Halsvidde 3.2
#Livvidde 10
#Hint: du kan bruke funksjonen .split() for å gjøre dette.
#La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi
#og returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål og
#benytter seg av tommerTilCm som du skrev tidligere for å skrive ut målene i
#centimeter

def tommerTilCentimeter(antallTommer):
#Lager prosedyren tommerTilCentimeter med paramenteret antallTommer
    assert antallTommer>0
    #Sier at antallTommer må være mer enn 0
    return antallTommer * 2.54
    #returnerer verdien av antallTommer ganger 2.54

maal = open("skredder.txt")
#Åpner textfilen skredder.txt, som lagres i variabelen maal
ordbok = {}
#Lager en tom ordbok med variabelnavnet ordbok
ordbokcentimeter = {}
#Lager en tom ordbok med variabelnavnet ordbokcentimeter
for i in maal:
#Går gjennom maal i en for-løkke
    liste = i.split()
    #Splitter opp verdiene i maal med å ta i.split(), verdiene lagres i variabelen liste
    navn = liste[0]
    #Setter den første verdien i liste som variabelen navn
    tall = liste[1]
    #Setter den andre verdien i liste som variabelen tall
    ordbok[navn.upper()]=tall
    #Legger til navn og tall i ordoken ordbok. navn er lagt som store bokstaver, ved hjelp av upper
    #slik at når brukeren skal søke på navn vil det ikke ha noe å si om det brukes store eller små
    #bokstaver. Her legges navn som nøkkelverdi og tall som innholdsverdi i ordboka
    ordbokcentimeter[navn.upper()]=tommerTilCentimeter(float(tall))
    #Gjør akkurat det samme som koden over, bare at innholdverdien fremkaller prosedyren
    #tommerTilCentimeter med tall som paramenterverdi
print("Mål i tommer:")
print(ordbok)
#Printer ut ordboka
print("\n Mål i centimeter:")
print(ordbokcentimeter)
#Printer ut ordboka: ordbokcentimeter
sok = input("\n Søk på et delnavn og få ut målene: ")
#Ber brukeren søke på et delnavn for å få ut målene, svaret lagres i variabelen sok
resultat = ""
#Lager et tomt strengelement som lagres i variabelen resultat
for i in ordbok:
#Går gjennom ordbok i "i" i en forløkke
    sok = sok.upper()
    #Sok blir gjort om til store bokstaver fordi nøkkelverdien i ordbok er satt som store bokstaver,
    #slik at store eller små bokstaver ikke skal ha noe å si når brukeren søker, slik blir det
    #enklere for brukeren å finne fram til nøkkelverdien
    resultat = ordbok[sok]
    #Resultat erlik ordbok med sok som nøkkelverdi, slik at innholdsverdien blir verdien
resultat_i_centimeter = tommerTilCentimeter(float(resultat))
#resultat_i_centimeter erlik prosedyren tommerTilCentimeter med resultat som tilhørende verdi, som
#erstattes med parameteret i prosedyren
print(resultat + " tommer eller " + str(resultat_i_centimeter)+ " centimeter er målene for " + sok)
#skriver ut resultat, resultat_i_centimeter og sok med tilhørende tekst
