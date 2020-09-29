steder = []
#Lager en liste som lagres i variabelen steder
avreisedatoer = []
#Lager en liste som lagres i variabelen avreisedatoer
klesplagg = []
#Lager en liste som lagres i variabelen klesplagg
reiseplan = []
#Lager en variabel som lagres i variabelen reiseplan

for steder_lokke in range(4):
#Løkka gjennomgås 4 ganger ved hjelp av range(4)
    inp = input("Skriv inn ditt reisemål: ")
    #Skriver ut "skriv inn ditt reisemål" for deretter at brukeren skal skrive inn.
    # Svaret til brukeren lagres i variabelen inp
    steder.append(inp)
    #Legger til variabelen inp i lista steder

for avreise_lokke in range(5):
#Løkka gjennomgås 5 ganger ved hjelp av range(5)
    inp = input("Skriv inn avreisedatoer: ")
    #SKriver ut inputfelt til brukeren som lagres i variabelen inp
    avreisedatoer.append(inp)
    #Legger til inp i lista avreisedatoer, inp fra den forrige løkka vil ikke legges til
    #fordi det er en lokal variabel
for klesplagg_lokke in range(5):
#Løkka gjennomgås 5 ganger ved hjelp av range(5)
    inp = input("Skriv inn klesplagg: ")
    #SKriver ut inputfelt til brukeren som lagres i variabelen inp
    klesplagg.append(inp)
    #Legger til inp i lista klesplagg, inp fra den forrige løkka vil ikke legges til
    #fordi det er en lokal variabel
reiseplan = [steder] + [avreisedatoer] + [klesplagg]
#Legger til steder, avreisedatoer og klesplagg i reiseplan. Lista fungerer slik at
#eksempelvis å få tilgang til en verdi i steder må man først skrive inn reiseplan[0]
#for så å finne en til verdi ved å for eksempel skrive reiseplan[0][1]
for reiseplan_lokke in reiseplan:
#For-løkke som gjennomgår reiseplan lista og printer ut lista
    print(reiseplan_lokke)

index1 = int(input("Skriv inn et tall til tilhørende liste "))
#Ber brukeren skrive inn et tall til tilhørende liste, svaret lagres i variabelen
#index1
index1 = index1 -1
#Tar inn svaret til brukeren og legger til minus 1 fordi kordinatsystemet til lister starter
#på 0
if index1 <= len(reiseplan):
#Om index en er mindre eller erlik lengden på lsite vil tilhørende delen av lista skrives ut
    print(reiseplan[index1])
    index2 = int(input("Skriv inn tall nummeret til en verdi på valgt liste: "))
    #Ber brukeren skrive inn en ny verdi fra den allerede valgte listen
    index2 = index2 - 1
    #1 trekkes fra index2 fordi kordinatsystemet for lister starter med 0
    if index2 <=len(reiseplan[index1]):
    #Om index2 er mindre eller erlik lengden til reiseplan[index1] så vil
    #reiseplan[index1][index2] skrives ut, altså den bestemte verdien i en av
    #de tre listene
        print(reiseplan[index1][index2])
    else:
    #Om ikke index2 erlik eller er mindre lengden på reiseplan[index1] vil ugyldig input
    #skrives ut
        print("Ugyldig input!")

else:
#Om ikke index1 erlik eller er mindre lengden på reiseplan vil ugyldig input skrives ut
    print("Ugyldig input!")
