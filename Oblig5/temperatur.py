gjennomsnitts_tempraturer = open("tempratur.txt")
#Tar inn textfilen tempratur.txt, som lagres i gjennomsnitts_tempraturer
liste = []
#Lager en tom liste, med variabelnavn liste

for i in gjennomsnitts_tempraturer:
#Går gjennom gjennomsnitts_tempraturer i en for løkke
    verdi = i.split()
    #Splitter opp verdiene i variabelen "i"
    temperatur = verdi[0]
    #Sier at variabelen tempratur starter på den første verdien i lista verdi
    liste.append(temperatur)
    #Legger til temperatur i den tomme lista, med variabelnavn liste ved hjelp av append
print(liste)
#Printer ut liste
def gjennomsnitt_liste(listenavn):
#Lager en prosedyre med "listenavn" som paramenter
    sum = 0
    #Lager en variabel, sum, med verdien 0
    for i in listenavn:
    #Går igjennom paramenteret listenavn i en for-løkke
        sum = sum + float(i)
        #summerer opp alt i listenavn, ved å addere sum med i, som lagres igjen i sum
    return (sum/len(listenavn))
    #Returnerer sum delt på lengden av listenavn, ved hjelp av len. Dette blir gjennomsnittet

print("Gjennomsnittet for lista er " + str(gjennomsnitt_liste(liste)))
#Printer ut tekst og prosedyren gjennomsnitt_liste som har liste som kjøres gjennom i prosedyren 
#istedenfor paramenteret, listenavn.
