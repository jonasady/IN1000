
maaned1 = input("Skriv inn en måned  ")
#skriver ut et spørsmål hvor brukeren selv kan svare, her er svaret lagret i variabelen maaned1
dag1 = input("Skriv inn en dag i valgte måned ")
#skriver ut et spørsmål hvor brukeren selv kan svare, her er svaret lagret i variabelen dag1
maaned2 = input("Skriv inn en ny måned ")
#skriver ut et spørsmål hvor brukeren selv kan svare, her er svaret lagret i variabelen maaned2
dag2 = input ("Skriv inn en ny dag til sistvalgte måned ")
#skriver ut et spørsmål hvor brukeren selv kan svare, her er svaret lagret i variabelen dag2
if (maaned1==maaned2 and dag1==dag2):
#kjører en if setning som sier at om variablene maaned1 og maaned2 i tillegg til dag1 og dag2 er like vil setningen nedenfor skrives ut
        print("samme dato!")
elif (maaned1>maaned2 or dag1>dag2):
#setningen nedenfor skrives ut om maaned1 er større enn maaned2 og/eller om dag1 er større enn dag2 ved hjelp av en elif-setning om if setningen over ikke er korrekt
    print ("feil rekkefølge")
else:
#om hverken if- eller elif-setningen er riktig vil else setingen skrives ut
    print("riktig rekkefølge")
