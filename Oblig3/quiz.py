#Oppgave: Lag en quiz hvor du har lagret svarene i en liste. Quizen skal inneholde et spørsmål som
#har flere svar. Til sammen skal det være 3 spørsmål. Brukeren skal få beskjed om svaret var riktig
#eller feil.
print ("Velkommen til quiz")
#Printer ut velkommen til quiz
def riktig_svar():
    print("Riktig svar!")
#Lager en prosedyre som skriver ut "Riktig svar!" om den blir fremkallet
def feil_svar():
    print("Galt svar!")
#Lager en prosedyre som skriver ut "Galt svar!" om den blir fremkallet
svar_sporsmaal = ["ERNA SOLBERG", ["LENNON", "MCARTNEY", "HARRISON", "STARR"], "BRUSSEL"]
#Lager en liste (svar_sporsmaal) som gir fasiten til spørsmålene. svar_sporsmaal[1] er en liste inni
#lista fordi det er flere svar som er riktig.
sporsmaal1 = input ("Hvem er statsminister i Norge? ")
#Ber brukeren skrive inn, svaret blir lagret i variabelen sporsmaal1
if sporsmaal1.upper() in svar_sporsmaal[0]:
#Sjekker om sporsmaal1 finnes i den første verdien i lista svar_sporsmaal ved å skrive
#svar_sporsmaal[0]. Det skal ikke ha noe å si om brukeren skriver feil med store og små
#bokstaver fordi sporsmaal1.upper() gjør svaret til store bokstaver og alle string-elementene i svar_sporsmaal
#er lagret med store bokstaver
    riktig_svar()
    #skriver ut prosedyren riktig_svar
else:
    feil_svar()
    #om ikke sporsmaal1 stemmer med den første verdien i svar_sporsmaal vil prosedyren feil_svar
    #skrives ut
sporsmaal2 = input("Nevn etternavnet til et medlem i The Beatles: ")
#Ber brukeren skrive inn, svaret blir lagret i variabelen sporsmaal2
if sporsmaal2.upper() in svar_sporsmaal[1]:
    #Om sporsmaal2 finnes i verdiene i lista svar_sporsmaal[1], som igjen en egen liste i listen svar_sporsmaal,
    #vil prosedyren riktig_svar skrives ut. Igjen skal det ikke ha noe å si om man bruker store eller små
    #bokstaver
    riktig_svar()

else:
    feil_svar()
#om ikke sporsmaal2 stemmer med den første verdien i svar_sporsmaal vil prosedyren feil_svar
#skrives ut
sporsmaal3 = input("Hva er hovedstaten i Belgia?" )
#Ber brukeren skrive inn, svaret blir lagret i variabelen sporsmaal3
if sporsmaal3.upper() in svar_sporsmaal[2]:
#Om verdien i sporsmaal3 finnes i tredje verdien i svar_sporsmaal ved hjelp av å skrive svar_sporsmaal[2] vil
#prosedyren riktig_svar() skrives ut
#Om brukeren skriver inn store eller små bokstaver i variabelen sporsmaal3 skal det ikke ha noe å si.
    riktig_svar()

else:
#Om ikke if-setningen stemmer overens vil else-setningen skrive ut prosedyren feil_svar()
    feil_svar()
print("Takk for innsatsen!")
#Printer ut "Takk for innsatsen!"
