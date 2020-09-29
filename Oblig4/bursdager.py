# Oppgave 6)
#Lag et program som får brukeren til å skrive inn 2 navn med 2 tilhørende bursdager.
#La så brukeren søke på navnet og tilhørende bursdag skrives ut.

navn = ""
#Lager variabelen navn som en tom string/""
index = 0
#Lager variabelen index som har verdien 0
liste = {}
#Lager en ordbok som er lagret i variabelen liste
for i in range(2):
#Sier for-løkka skal ha en range på 2. Det vil si at for-løkka gjennomgås 2 ganger
    navn = input("Skriv inn navn: ")
    #SKriver ut et inputfelt hvor brukeren skal skrive inn et navn
    bursdag = input("Skriv inn bursdag: ")
    #Skriver ut et inputfelt hvor brukeren skal skrive inn en bursdag
    liste[navn] = bursdag
    #Legger til navn som nøkkelverdi i ordboken liste og bursdag som innholdsverdi
for i in liste:
#Går gjennom lista og skriver ut bursdag og dato ved å referere til innholds- og
#nøkkelverdien i orboken liste
    print(str(i) + " har bursdag " + str(liste[i]))

index = input("Søk på navn og finn bursdag ")
#Ber brukeren skrive inn et navn som lagres i variabelen index
if index in liste:
#Om index, altså det brukeren har skrevet inn i siste inputfelt, finnes i liste vil
#det skrives ut navn og innholdsverdien til navn i lista
    print (index + " har bursdag " + liste[index])
else:
#Om ikke index stemmer i if-setningen skrives else-setningen ut
    print("Skriv in et gyldig navn")
