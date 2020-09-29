sporsmal = input("Liker du brus? ja/nei")
#skriver ut om du liker brus eller ikke og forventer svar
if sporsmal == "ja":
    #sjekker om svaret er "ja" ved hjelp av en if-setning, om så er tilfellet skrives setningen ut nedenfor
     print("Her har du en brus")
elif sporsmal == "nei":
    #om ikke svaret er "ja", vil elif setningen sjekke om svaret er "nei"
    print("Den er grei")
    #om svaret er "nei" vil "Den er grei" skrives ut
else:
#om hverken svaret er "nei" eller "ja" fra setningene overfor vil stemmer vil else setningen fange dette opp og skrive ut setningen nedenfor
    print("Det forstod jeg ikke helt")
