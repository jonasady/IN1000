def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()

#Programmet starter med å lage en prosedyre med navnet minFunksjon. Prosedyren har ikke noen
#parametere. Videre er det lagt en for-løkke som gjennomgås 2 ganger. Deretter er variabelen
#c definert som 2 og printes ut. Siden c+= 1 er skrevet etter print vil c alltid være 2. Om c hadde vært
#definert utenfor løkka og c+= 1 hadde stått før print ville c blitt plusset med 1 to ganger. Videre er
#b definert som verdien 10. b plusses videre med a, hvorav a ikke er definert slik at det blir en
#ugyldig kode. På neste linje printes b ut og deretter returnerer man verdien b, men på grunn av
#at koden er ugyldig fordi a ikke er definert vil ikke noe printes ut. Løkken går som sagt
#gjennom dette to ganger.

#Deretter er det lagt inn en ny prosedyre med navnet hovedprogram, som også ikke har noen tilhørende
#parametere. På neste linje er a definert som 42 og b definert som 0. Programmet printer videre ut b.
#Så blir b definert som a, slik at begge verdiene b og a erlik 42. Så kaller man på funksjonen minFunksjon
#og sier at a = minFunksjon(), slik at a erlik minFunksjon, istedenfor 42. Så printer man ut b, som er
#42 og a, som er minFunksjon, som er ulovlig kode, slik at ingenting printes ut. Til slutt kaller man på
#funksjonen hovedprogram().
