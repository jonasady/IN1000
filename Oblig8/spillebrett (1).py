from random import randint
#Importerer randint fra random
from celle import Celle
#Importerer klassen Celle fra filen celle.py
class Spillebrett:
#Lager klassen Spillebrett
    def __init__(self, rader, kolonner):
        #Klassen har to(eller tre, om man teller med self) parametere: rader og kolonner
        self._kolonner = kolonner
        #Definerer kolonner i konstruktøren som self._kolonner
        self._rader = rader
        #Definerer rader i konstruktøren som self._rader
        self._rutenett = []
        #Lager en ny instansevariabel i konstruktøren, som er self._rutenett, med verdi som
        #en tom liste([])
        self._generasjonsnummer = 0
        #Lager igjen en ny instansevariabel, self._generasjonsnummer, med verdien ny
        self.lagRutenett()
        #Kaller på metoden lagRutenett(), som lager det todimensjonale rutenttet
        self._generer()
        #Kaller på metoden generer som setter verdier for hver enkelt celle i lagRutenett i starten


    def lagRutenett(self):
    #Oppretter en metode, lagRutenett(self)
        for rad in range(self._rader):
        #Lager en for-løkke som gås gjennom så mange ganger tallet self._rader er
            self._rutenett.append([])
            #Legger til en tomme lister antall ganger range(self._rader)
            for kolonner in range(self._kolonner):
            #Lager en for-løkke som gås gjennom så mange ganger self._kolonner er, i tilegg er
            #for-løkka lagt inn i "rader"-for-løkka slik at det legges til så mange verdier som
            #er nevnt i range(self._kolonner) i hver liste som er opprettet av rader-løkka.
                self._rutenett[rad].append(Celle())
                #Legger til så mange verdier av Celle som er i range(self._kolonner)
                #i en bestemt rad i self._rutenett
        #MERK! oppgaven sier at man skal "tegne" opp et rutenett i konstruktøren. Jeg har lagd en
        #metode og kalt den i konstruktøren. Dette mener jeg svarer på oppgaven, samtidig som man ikke
        #lager rutenettet "direkte" i kontruktøren, men kaller på metoden. Jeg har gjort dette slik
        #fordi det blir mer oversiktelig.

    def tegnBrett(self):
    #Lager metoden tegnBrett(self)
        print("\n"*20)
        #Printer et linjeskift 20 ganger, med dette er det ment at brettet tømmes for hver gang
        # man oppdaterer brettet
        for rad in range(self._rader):
        #Går gjennom range(self._rader), som også er mer forklart i linje 23
            print("\n")
            #Printer ut linjeskift for hver gang for løkka begynnner på en ny rad, slik at hver
            #rad printes, og ikke alle verdiene printes ut 1-og-1 på hver sin linje
            for kolonne in range(self._kolonner):
            #Går gjennom rad i en for-løkke igjen så mange ganger

                print(self._rutenett[rad][kolonne].hentStatusTegn(), end = " ")
                #Printer en bestemt verdi i self._rutenett gitt først med en plass som her er
                #representert med rad, deretter en kolonne, siden det er en nøstet liste. Deretter
                #henter programmet fram prosedyren hentStatusTegn(), som returnerer "." dersom den opprinnelige
                #verdien til den bestemte verdien i self._rutenett er False, og "O" dersom den er True. Her
                #er det også brukt end ="" slik at alle verdiene innenfor rad kommer på samme linje.
        print("\n"*2)
        #Legger til to linjeskift
        self._generasjonsnummer+=1
        #For hver gang tegnBrett blir kalt, blir også generasjonsnummeret
        print("Generasjonsnummer: " + str(self._generasjonsnummer))
        #Printer generasjonsnummer som streng med tilhørende tekst
    def oppdatering(self):
    #Lager metoden oppdatering
        doede_celler = []
        #Lager en tom liste, med variabelnavn "doede_celler"
        levende_celler = []
        #Lager en tom liste, med variabelnavn "levende_celler"

        for rad in range(self._rader):
        #Går gjennom range for self._rader i en for-løkke
            for kolonne in range(self._kolonner):
                #Går deretter gjennom range av self._kolonner i en for-løkke, innefor den forige
                #for-løkken slik at det blir en nøstet for-løkke
                teller = 0
                #Lager variabelen teller med verdi 0
                celle = self._rutenett[rad][kolonne]
                #Variabelen celle erlik self._rutenett[rad][kolonne], og kaller etter en bestemt verdi
                #i self._rutenett siden det er en nøstet liste.
                nabo_liste = self.finnNabo(rad,kolonne)
                #Lager naboliste som returnerer en liste med de 8 naboene til celle
                #ved å bruke metoden finnNabo med rad og kolonne som parametre

                for nabo in nabo_liste:
                #Går gjennom nabo_liste i en for-løkke
                     if nabo.erLevende():
                    #For hver verdi i nabo_liste, her representert ved nabo, returnerer True
                    #(funksjonen erLevende sjekker om verdien er True eller False) vil
                    #teller plusses med en
                        teller+=1

                if celle.erLevende():
                #If-sjekken godkjennes dersom celle returnerer True i metoden erLevende
                    if teller< 2 or teller> 3:
                    #Om teller er mindre enn 2 eller større enn 3 vil denne bestemte verdien av
                    #celle legges til i liste doede_celler
                        doede_celler.append(celle)

                else:
                #Her går alle verdiene som returnerer false, siden if-sjekken sjekker True
                    if teller == 3:
                    #Om teller erlik 3 vil celle legges til i levende_celler
                        levende_celler.append(celle)

        for j in doede_celler:
        #Går gjennom doede_celler i en for-løkke og bruker metoden settDoed for hver verdi i
        #liste som gjør at hver verdi vil returnere "."
            j.settDoed()
        for i in levende_celler:
        #Går gjennom levende_celler i en for-løkke og bruker metoden settLevende for hver verdi i
        #liste som gjør at hver verdi vil returnere "O"
            i.settLevende()

    def _generer(self):
    #Lager metoden _generer
        for rad in range(self._rader):
        #Går gjennom range for self._rader i en for-løkke
            for kolonne in range(self._kolonner):
            #Går deretter gjennom range av self._kolonner i en for-løkke, innefor den forige
            #for-løkken slik at det blir en nøstet for-løkke
                tilfeldigtall = randint(0, 2)
                #Lager tilfeldigtall, hvor verdien er et tilfeldig tall mellom 0 og 2(0,1 og 2)
                if tilfeldigtall == 0:
                #Om tilfeldigtall er 0 vil den bestemte verdien i self._rutenett, her gitt
                #med self._rutenett[rad][kolonne], gå gjennom metoden i klassen Celle settLevende()
                #og verdien blir "levende"
                    self._rutenett[rad][kolonne].settLevende()
                else:
                #Om tilfeldigtall ikke er 0 vil den bestemte verdien i self._rutenett, her gitt
                #med self._rutenett[rad][kolonne], gå gjennom metoden i klassen Celle settDoed()
                #og verdien blir "doed"
                    self._rutenett[rad][kolonne].settDoed()



    def finnAntallLevende(self):
    #Lager metoden finnAntallLevende
        levende = 0
        #Sier at variabelen levende erlik 0
        for rad in range(self._rader):
        #Går gjennom range for self._rader i en for-løkke
            for kolonne in range(self._kolonner):
            #Går deretter gjennom range av self._kolonner i en for-løkke, innefor den forige
            #for-løkken slik at det blir en nøstet for-løkke
                if self._rutenett[rad][kolonne].erLevende() == True:
                #Om den bestemte verdien av self._rutenett, som sjekkes i erLevende, som igjen
                #returnerer enten True eller False, er True vil levende plusses med en for
                #hver gang
                    levende += 1
        return levende
        #returnerer levende

    def finnNabo(self, rad,kolonne):
    #Lager metoden finnNabo, med parameterne rad og kolonne
        liste_nabo = []
        #Lager en tom liste, med variabelnavn liste_nabo
        for i in range(-1, 2):
        #Går gjennom tallene fra -1 til 2 i en for-løkke(-1,0,1 og 2)
            for x in range(-1, 2):
            #Går gjennom tallene fra -1 til 2 i en for-løkke(-1,0,1 og 2) innenfor den første
            #for-løkken slik at det blir en "nøstet" for-løkke på sett og vis
                rad_nabo= rad + x
                #Sier at rad_nabo erlik rad + x
                kolonne_nabo = kolonne + i
                #sier at kolonne_nabo erlik kolonne + i
                riktig = True
                #Lager variabelen riktig som erlik True
                if rad_nabo >= self._rader or rad_nabo < 0:
                #Om rad_nabo er større eller erlik self._rader eller rad_nabo er mindre enn
                #0 vil programmet returnerer False. Dette er for at naboene regnes innenfor
                #hjørnene i brettet
                    riktig = False

                elif kolonne_nabo >= self._kolonner or kolonne_nabo < 0:
                #Om kolonne_nabo er større eller erlik self._kolonner eller rad_kolonne er mindre enn
                        #0 vil programmet returnerer False. Dette er igjen for at naboene regnes innenfor
                        #hjørnene i brettet
                    riktig = False

                elif rad_nabo == rad and kolonne_nabo == kolonne:
                #Om rad_nabo erlik rad og kolonne_nabo erlik kolonne vil programmet returnere False.
                #Dette er fordi dette er kordinatene til cellen man vil finne naboene til, og deremed
                #ikke legge til cellen som man skal finne naboene i liste_nabo
                    riktig = False

                if riktig:
                #Om riktig= True vil den bestemte verdien som er gjennomgått i if og elif- sjekkene
                #legges til i liste_nabo
                    liste_nabo.append(self._rutenett[rad_nabo][kolonne_nabo])
        return liste_nabo
        #returnerer liste_nabo
