fahren = int(input("Skriv inn tempraturen i fahrenheit: "))
#Ber brukeren skrive inn tempratur i fahrenheit, tallet lagres som et tall ved hjelp
#av int og lagres i variabelen "fahren".
celcius = ((fahren)-32)*5/9
#variabelen fahren blir gjort om til celcius i variabelen celcius.
ny_celcius = "%.2f" % celcius
#varianelen ny_celcius sikrer at tallet i variabelen celcius er to desimaler
#og instruerer ved hjelp av "%.2f" som sier ifra om at det er gjeldende med
#to desimaler
print("Det blir", str(ny_celcius), "celcius")
#printer ut, her gjøres ny_celcius om til string fordi det er tekstelemeter
#inni print-elementet
