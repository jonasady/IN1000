
varer_pris = {"melk": 14.90, "brød": 24.90, "yogurt": 12.90, "pizza": 39.90}
#Lager en ordbok lagret i variabelen varer_pris, hvorav hvert varenavn er nøkkelverdien og prisen tilhører
print(varer_pris)
#printer ut ordboken

def vare_sporsmaal():
#Lager en prosedyre med navnet vare_sporsmaal
    varenavn = input("Skriv inn produktet: ")
    #Lager en variabel med inputfelt som ber brukeren skrive inn navnet på produktet
    pris = float(input("Skriv inn prisen til produktet: "))
    #Lager et inputfelt, hvor svaret blir lagret som flytall i variablen pris
    varer_pris[varenavn]= pris
    #Legger til varenavn og pris i ordboken varer_pris. Varenavn blir lagret som en
    #nøkkelverdi og pris som tilhørende verdi.

vare_sporsmaal()
vare_sporsmaal()
#Skriver ut prosedyren to ganger
print(varer_pris)
#Skriver ut ordboken varer_pris
