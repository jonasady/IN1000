from spillebrett import Spillebrett
#Importere klassen Spillebrett fra spillebrett.py

def main():
#Lager prosedyren hovedprogram

    storrelse = int(input("Dimensjoner for brettet: "))
    #Lager et inputfelt hvor brukeren velger dimensjonene for brettet som lagres i storrelse
    #og må være et heltall/int-element
    brett = Spillebrett (storrelse, storrelse)
    #Lager et objekt hvor brett erlik klassen Spillebrett med storrelse og storrelse som
    #parametre
    brett.tegnBrett()
    #Kaller på metoden tegnBrett i objektet brett, som tegner opp spillebrettet med tilfeldige
    #celler(1/3 sjans for at celler er levende)
    print("Antall levende:", brett.finnAntallLevende())
    #Printer finnAntallLevende med tilhørende tekst,
    #hvor objektet brett kobles, slik at metoden kjøres tilpasset brett.
    svar = input("")
    #Lager et tomt input-element, som lagres i svar
    while svar!= "q":
    #Om svar ikke erlik "q" vil while-løkken kjøres
        brett.oppdatering()
        #Kjører objektet brett gjennom metoden fra klassen Spillebrett: oppdatering
        print("Antall levende:", brett.finnAntallLevende())
        #Printer finnAntallLevende med tilhørende tekst,
        #hvor objektet brett kobles, slik at metoden kjøres tilpasset brett.
        brett.tegnBrett()
        #Kaller på metoden tegnBrett, som tegner brettet etter å ha kalt på oppdatering, slik
        #at celler endrer plass etter reglene
        svar = input("Trykk enter for aa fortsette og q dersom du vil avslutte")
        #Sier at svar skal være et nytt inputfelt som sier at dersom man trykker på q, vil
        #programmet slutte, og enter for å fortsette
main()
#Kaller på funksjonen hovedprogram
