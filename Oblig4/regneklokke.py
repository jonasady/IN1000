tall = ""
#Lager variabelen tall som står som en åpen string
tall_liste = []
#Lager en liste som lagres i variabelen tall_liste
sum =0
#Lager en variabel sum som har verdien 0
while tall!=0:
#Lager en whileløkke som sier at så lenge tall ikke er 0 vil løkken kjøres
    tall = int(input("Skriv inn et tall "))
    #Ber brukeren skrive inn et tall som lagres på nytt i variabelen tall
    tall_liste.append(tall)
    #Legger til tall i tall_liste

for a in tall_liste:
#Lager en for-løkke som skriver ut tall_liste som skrives ut dersom brukeren skriver 0 i det tidligere
#inputfeltet
    print(a)

for b in tall_liste:
#Går gjennom talliste, verdi for verdi, og summerer opp alle tallene i lista
    sum = sum + b
print("Summen av tallene blir " + str(sum))

minst = tall_liste[0]
#Setter minst som første verdi i tall_liste
stoerst = tall_liste[0]
#Setter stoerst som første verdi i tall_liste

for mindre in tall_liste:
#Går gjennom talliste
    if mindre < minst:
    #Om minst er større enn mindre, hvor mindre er første verdi i tall_liste vil minst være mindre
        minst = mindre
print(str(minst)+ " er det minste tallet")
#minst skrives ut
for storre in tall_liste:
    if storre >stoerst:
    #Om storre er større enn stoerst, hvor storre er første verdi i tall_liste vil stoerst være storre
        stoerst = storre
print(str(stoerst) + " er det største tallet")
#Skriver ut stoerst
