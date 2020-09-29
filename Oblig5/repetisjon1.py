mineOrd = []
#Lager en tom liste med navnet "mine ord"

def slaaSammen(streng1 , streng2):
#Lager en prosedyre med streng1 og streng2 som paramentere
    sammen = streng1 + streng2
    #Lager en variabel som slår sammen streng1 og streng2, dette lagres i variabelen sammen
    return sammen
    #Returnerer variabelen sammen


def skrivUt(liste):
#Lager en ny prosedyre med navnet skrivUt hvor liste er parameteret
    for i in liste:
    #Går igjennom lista i en forløkke og printer ut verdi for verdi ved å printe ut "i"
        print(i)

svar = input(" Skriv hva du vil, om du ønkser å stoppe så skriv inn s: ")
#Skriver ut et inputfelt til brukeren hvor brukeren skal skrive inn. Svaret
#lagres i variabelen svar
while svar.lower() != "s":
#While løkke som sier at så lenge brukeren ikke skriver inn s vil løkken fortsette å gå

    if svar.lower() == "i":
    #If-setning som har som premiss at brukeren skriver inn "i"
        inp1 = input("Skriv inn: ")
        #Ber brukeren skrive inn en verdi, dette lagres i inp1
        inp2 = input("Skriv inn: ")
        #Ber brukeren skrive inn en verdi, dette lagres i inp2
        sammen = slaaSammen(inp1, inp2)
        #Lager en variabel, sammen, hvor prosedyren slaaSammen, med verdiene inp1 og inp2 er verdien
        #til sammen
        mineOrd.append(sammen)
        #Legger sammen i lista mineOrd

    elif svar.lower() == "u":
    #Om brukeren skriver inn u vil lista mineOrd skrives ut
        skrivUt(mineOrd)

    svar = input("ønsker du å fortsette? Om ikke, skriv inn s: ")
    #Om brukeren ikke skriver inn s, u eller i vil programmet skrive ut dette inputfeltet, som
    #igjen lagrer svaret til brukeren i variabelen svar

print("Programmet er avsluttet")
#Om s er trykket vil while-løkka slutte og "programmet er avsluttet" vil bli printet.
