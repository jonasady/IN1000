min_setning = input("Skriv inn en setning: ")
#Skriver ut "Skriv ut setning til brukeren", svaret til brukeren lagres i variabelen
#min_setning
def funksjon_ord(inp):
#Lager en prosedyre med tilhørende variabel inp
    ord_teller = 0
    #Lager en variabel som har verdien null og heter ord_teller
    for index in inp:
    #Lager en forløkke til inp som går igjennom antall bokstaver
        ord_teller += 1
        #teller for hver gang forløkka gjennomkjøres, altså for hver bokstav teller den
    return ord_teller
    #returnerer verdien i ordteller
def funksjon_setning(inp):
#Lager en funksjon som heter funksjon_setning som har tilhørende verdi som er inp
    setning_liste = inp.split()
    #Splitter opp inp slik at hvert ord inngår i en liste
    ordbok = {}
    #Lager en ordbok med variabelnavn ordbok

    for i in setning_liste:
    #Går gjennom setning_liste i en forløkke
        ordbok[i]=setning_liste.count(i)
        #Legger til "i" i ordboka som nøkkelverdi, som er gitt ved et ord. Deretter
        #gis antall ganger ordet inngår i setning_liste med hjelp av count.

    for i in ordbok:
    #går igjennom ordbok i en for-løkke
        ganger = ""
        #variabelen ganger blir gitt som en lokal variabel og har verdi ""/tom string
        bokstav = ""
        #variabelen bokstav blir gitt som en lokal variabel og har verdi ""/tom string
        if ordbok[i]== 1:
        #Om innholdsverdien i gitt nøkkelverdi (antall ganger ordet går igjen) erlik 1 vil
        #den definisjonen av ganger under gjelde
            ganger = "gang"
        else:
        #Om ikke innholdsverdien for gitt verdi (i) ikke erlik 1 vil den definisjonen av ganger
        #under gjelde
            ganger = "ganger"
        if funksjon_ord(i)==1:
        #Om innholdsverdien i gitt nøkkelverdi (antall ganger ordet går igjen) erlik 1 vil
        #den definisjonen av ganger under gjelde
            bokstav = "bokstav"
        else:
        #Om ikke innholdverdien for gitt verdi (i) ikke erlik 1 vil den definisjonen av ganger
        #under gjelde
            bokstav = "bokstaver"

        print(i+ " forekommer " + str(ordbok[i]), ganger +" og har " + str(funksjon_ord(i)) , bokstav)
        #Printer ut i og gitt ord i lista i tillegg til å skrive ut innholdverdien til gitt nøkkelverdi av ordbok,
        #som er antall ganger ordet forekommer. Så skrives variabelen ganger ut, i tillegg til å fremkalle
        #funksjon_ord, med verdien i. Variabelen bokstav skrives også ut.
funksjon_setning(min_setning)
#Skriver ut funksjon_setning med min_setning som verdi.
