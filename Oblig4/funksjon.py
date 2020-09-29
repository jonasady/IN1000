def adder(tall1, tall2):
#Lager en funksjon med tilhørende variabler tall1 og tall2
    sum = tall1 + tall2
    #Lager en variabel, sum, som adderer tall1 og tall2
    return(str(tall1) + " pluss " + str(tall2) + " er lik " + str(sum))
    #Skriver ut tall1 pluss tall2 erlik sum
adder(3,4)
#Setter verdien av tall1 og tall2 til 3 og 4, slik at når funksjonen kjøres vil
#7 sikrives ut som sum
adder(25,14)
#Setter verdien av tall1 og tall2 til 25 og 14, slik at når funksjonen kjøres vil
#39 sikrives ut som sum
def tellForekomst(minTekst, minBokstav):
#Lager en funksjon som har tilhørende verdier som er satt til variabelene minTekst og minBokstav
    minTekst= minTekst.upper()
    #Sier av minTekst skal gjøres om til store bokstaver
    minBokstav = minBokstav.upper()
    #Sier at minBokstav skal gjøres om til store bokstaver
    bokstavteller = minTekst.count(minBokstav)
    #teller antall ganger minBokstav forekommer i minTekst med hjelp av count
    return(minTekst + " har " + str(bokstavteller), minBokstav + "-er i seg")
    #Printer ut at minTekst har bokstavteller, med mellomrom, minBokstav mellomrom -er i seg

tekst= input("Skriv inn et ord ")
#Ber brukeren skrive inn et ord som lagres i variabelen tekst
bokstav = input("Skriv inn en bokstav ")
#Ber brukeren skrive inn en bokstav som lagres i variabelen bokstav

tellForekomst(tekst, bokstav)
#Skriver ut funksjonen tellForekomst som har verdiene tekst og bokstav slik at
 #minTekst og minBokstav har verdien tekst og bokstav
