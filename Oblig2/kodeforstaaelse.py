#1) Koden er ikke lovlig fordi streng(tekst) og float (heltall) ikke kan gå sammen i samme
#felt ved print. Her burde man ha tatt å gjort om variabelen b til en streng ved funksjonen
#str(b). variabelen b er satt som et tall i andre linje av koden, hvilket ikke blir lovlig

#2) Det første problemet en støter på om en kjører koden er først og fremst at terminalen
#sender ut en feilmelding og melder fra om at str og int er brukt om hverandre, og en såkalt "type Error".
#Dette er ikke en selvsagt feilmelding som oppklarer problemet vi har i koden, og kan være
#en utfordring å skjønne for å nøste opp i koden slik at den blir riktig.

#Om man så har fikset koden ved å skifte fra float til streng i den siste print setniningen har
#man ikke et else- eller elif-alternativ til if-setningen. Programmet vil ikke skrive ut noen ting
#om så man skriver inn et høyere tall enn 10 eller rett og slett skriver inn 10. Dette er
#et problem om man spør seg selv hvor hensiktsmessig det er å kunn svare på om tallet
#skrevet ned i inputlinja er større enn 10. Det burde være et alternativ, altså elif-
#eller else-setninger. Det er en gyldig kode om man kun bruker if, men hvor hensiktsmessig det er
#er det verdt å sette spørsmål til. I tillegg vil koden i siste linje skrive ut nummer + hei
#(om nummeret er mindre enn 10) uten mellomrom. Her kunne man satt et komma istedenfor "+"
#for å få et mellomrom og mer oversikt.


a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
