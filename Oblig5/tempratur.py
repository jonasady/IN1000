gjennomsnitts_tempraturer = open("tempratur.txt")
liste = []

for i in gjennomsnitts_tempraturer:
    verdi = i.split()
    temperatur = verdi[0]
    liste.append(temperatur)
print(liste)

def gjennomsnitt_liste(listenavn):
    sum = 0
    for i in listenavn:
        sum = sum + float(i)
    return (sum/len(listenavn))

print("Gjennomsnittet for lista er " + str(gjennomsnitt_liste(liste)))
