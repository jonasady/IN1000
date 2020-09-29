print("Utregninger: ")
#Skriver ut "Utregninger: "
brukerTall1 = int(input("Skriv inn et tall: "))
#Ber brukeren om å skrive inn et tall, tallet lagres i variabelen brukerTall1
brukerTall2 = int(input("Skriv inn et tall til: "))
#Ber brukeren om å skrive inn et tall, tallet lagres i variabelen brukerTall2
def addisjon(tall1, tall2):
#Lager en prosedyre med to parametere; tall1 og tall2
    return tall1+tall2
    #returnerer summen av tall1 og tall2, altså tall1 + tall2


def subtraksjon(tall1, tall2):
#Lager en prosedyre med to parametere; tall1 og tall2
    return tall1-tall2
    #Returnerer verdien av tall1 minus tall2


def divisjon(tall1, tall2):
#Lager en prosedyre med to parametere; tall1 og tall2
    return tall1/tall2
    #Returnerer verdien av tall1 delt på tall2


assert addisjon(3, 4) == 7
assert addisjon(-20, -3) == -23
assert addisjon(14, -6) == 8
#Bruker assert for å sjekke om addisjonsfunksjonen fungerer slik den skal med verdier
#i de to paramenterne og svaret

assert subtraksjon(-4, 3) == -7
assert subtraksjon(-14, -4) == -10
assert subtraksjon(11, 3)== 8
#Bruker assert for å sjekke om funksjonen subtraksjon fungerer slik den skal med verdier
#i de to paramenterne og svaret
assert divisjon(20, 5) == 4
assert divisjon (-24, -8)== 3
assert divisjon (12, -4)== -3
#Bruker assert for å sjekke om funksjonen divisjon fungerer slik den skal med verdier
#i de to paramenterne og svaret
def tommerTilCentimeter(antallTommer):
#Lager en prosedyre som heter tommerTilCentimeter med parameteret antallTommer
    assert antallTommer>0
    #antallTommer må være mer enn 0
    return antallTommer * 2.54
    #returnerer verdien av antallTommer ganger 2.54


def skrivBeregninger():
#Lager en prosedyre som heter skrivBeregninger
    print("\n Resultat for summering: " + str(addisjon(brukerTall1, brukerTall2)))
    #Printer ut tekst og fremkaller prosedyren addisjon med tilhørende verdier for paramenter, som
    #i dette tilfelle er brukerTall1 og brukerTall2
    print("Resultat for subtraksjon: " + str(subtraksjon(brukerTall1, brukerTall2)))
    #Printer ut tekst og fremkaller prosedyren subtraksjon med tilhørende verdier for paramenter, som
    #i dette tilfelle er brukerTall1 og brukerTall2
    print("Resultat for divisjon: " + str(divisjon(brukerTall1, brukerTall2)))
    #Printer ut tekst og fremkaller prosedyren divisjon med tilhørende verdier for paramenter, som
    #i dette tilfelle er brukerTall1 og brukerTall2
    print("\n Fra tommer til centimeter")
    #Skriver ut "Fra tommer til centimeter"
    tommerInput = float(input("Skriv inn tommer: "))
    #Ber brukeren skrive inn antall tommer, svaret lagres i variabelen tommerInput
    print("Resultat: " + str(tommerTilCentimeter(tommerInput)))
    #Skriver ut prosedyren tommerTilCentimeter med tommmerInput som verdi for paramenteret

skrivBeregninger()
#Skriver ut prosedyren skrivBeregninger()
