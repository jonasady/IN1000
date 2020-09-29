salgstall = open("salgstall.txt")
#Åpner text-filen salgstall.txt
def innlesning(filnavn):
#Lager funksjonen innlesning med filnavn som parameter
    ordbok = {}
    #Lager en ny ordbok med variabelnavn ordbko
    for i in filnavn:
    #Går gjennom filnavn i en for-løkke
        liste = i.split()
        #Splitter verdi for verdi i filnavn, som er i, og legger til dette i en liste
        navn = liste[0]
        #Sier at navn settes som første verdi i liste og vil senere teller oppover i liste
        tall = liste[1]
        #Setter tall som andre verdi  i liste og vil senere teller oppover i liste
        ordbok[navn]=tall
        #Legger til navn og tall i ordbok, med navn som nøkkelverdi og tall som innholdsverdi
    return ordbok
    #Returnerer ordboka

def maandendensSalgsperson(ordbok):
#Lager en funksjon, maandendensSalgsperson, med ordbok som parameter
    liste = []
    #Lager en tom liste, med variabelnavn liste
    for i in ordbok:
    #Går gjennom ordboka i en for løkke
        liste.append(int(ordbok[i]))
        #Legger til innholdsverdiene i liste
        storst = liste[0]
        #Sier at variabel storst erlik liste[0], altså første verdien i liste
        for storre in liste:
        #Går gjennom liste i en for-løkke
            if storre>storst:
            #Om storre er større enn storst vil storst være storre, og verdien som Returneres er i, slik at personen som storst tilhører returnerer
                storst = storre
                return i
def totaltAntallSalg(ordbok):
#Lager funksjonen totaltAntallSalg, med ordbok som parameter
    sum = 0
    #Lager variabelen sum som erlik 0
    for i in ordbok:
    #Går gjennom ordbok i en for-løkke
        sum += int(ordbok[i])
        #Sum plusses med innholdsverdiene i ordboka, som settes til et heltall
    return sum
    #funksjonen returnerer sum
def gjennomsnittSalg(ordbok):
#Lager en funksjon som heter gjennomsnittSalg med ordbok som parameter
    gjennomsnitt = totaltAntallSalg(ordbok)/len(ordbok)
    #Variabelen gjennomsnitt tar opp funksjonen totaltAntallSalg, med ordbok som argument, og deler deretter med lengden på ordboka
    return gjennomsnitt
    #gjennomsnittSalg returnerer gjennomsnitt

def hovedprogram():
#Lager prosedyren hovedprogram
    ordbok_salg = innlesning(salgstall)
    #Variabelen ordbok_salg tar inn funksjonen innlesning og salgstall som argument, slik at det blir er oversiktelig med variabelen ord_boksalg når
    #man skal skrive ut, og ikke hele funksjonen med argument
    person = maandendensSalgsperson(ordbok_salg)
    #Variabelen person lagres med verdien fra funksjonen maandendensSalgsperson med orbok_salg som argument
    antall_salg = ordbok_salg[person]
    #Variabelen antall_salg lages som ordbok_salg med person som nøkkelverdi som får frem innholdsverdien
    totalt = totaltAntallSalg(ordbok_salg)
    #Lagerer variabelen totalt som funksjonen totaltAntallSalg med ord_boksalg som argument
    gjennomsnitt = gjennomsnittSalg(ordbok_salg)
    #Lagerer variabelen gjennomsnitt som funksjonen gjennomsnittSalg med ordbok_salg som arguemnt
    print("\nMånedens selger er " + person + " med " + str(antall_salg) + " salg " )
    print("\n Totale salg: " + str(totalt) + "\n Antall selgere: " + str(len(ordbok_salg)) + "\n Gjennomsnitt for salg: " + str(gjennomsnitt))
    #Printer ut alle variabelene som er referert til over, med tilhørende tekst og formatering til str om det har vært nødvendig
hovedprogram()
#Kaller på hovedprogram
