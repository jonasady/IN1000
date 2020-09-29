liste_tall = [3,5,6]
#Lager en liste med tall i variabelen liste_tall
liste_tall.append(8)
#Legger til 8 i lista ved hjelp av append
print (liste_tall[0] , liste_tall[2])
#printer tall nr 0(det første tallet) i lista og tall nr 2(det tredje tallet) i lista
liste_navn = []
#lager en ny liste som lagres i variabelen liste_navn
ny_liste_tall = []
#lager en ny liste som lagres i variabelen ny_liste_tall
def navnfunksjon():
#starter en prosedyre ved navnet navnfunksjon
    liste_navn.append(input("Skriv inn et navn: "))
#Ber brukeren skrive inn et navn som legges inn i lista liste_navn ved hjelp av append()
navnfunksjon()
navnfunksjon()
navnfunksjon()
navnfunksjon()
#skriver ut prosedyren 4 ganger
if "Jonas" in liste_navn:
#if setningen sier om "Jonas" er i liste_navn vil tilførende print ("Du husket meg") skrives ut
    print ("Du husket meg")
else:
#om ikke premisset om at man skrev inn "Jonas" i inputfeltet er oppfylt vil else setningen skrive ut "du glemte meg"
    print ("Du glemte meg")

sum_tall_pluss = liste_tall[0] + liste_tall[1] +  liste_tall[2] + liste_tall[3]
#adderer de fire tallene i liste_tall med hverandre ved hjelp av å referere til dem. For eksempel vil
#tall nummer 4 kunne kalles opp ved hjelp av å skrive liste_tall[3]. Denne summen lagres i sum_tall_pluss
sum_tall_gange = liste_tall[0] * liste_tall[1] *  liste_tall[2] * liste_tall[3]
#Alle tallene i liste_tall multipliseres og lagres i sum_tall_gange
ny_liste_tall.append(sum_tall_pluss)
#legger til sum_tall_pluss i liste ny_liste_tall
ny_liste_tall.append(sum_tall_gange)
#legger til sum_tall_gange i liste ny_liste_tall
liste_tall_og_ny_liste = ny_liste_tall + liste_tall
#Lager en ny liste som legger til liste_tall og ny_liste_tall
print(liste_tall_og_ny_liste)
#printer ut den nye listen
liste_tall_og_ny_liste.pop(4)
liste_tall_og_ny_liste.pop(4)
#Fjerner de to siste verdiene i lista ved å bruke pop(4) to ganger. Her vil man først slette den nest
#siste verdien først for deretter å fjerne den siste verdien som blir pop(4) igjen
print(liste_tall_og_ny_liste )
#printer ut liste_tall_og_ny_liste
