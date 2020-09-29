class Celle:
#Lager klassen Celle
    def __init__(self):
    #Lager konstruktøren, som ikke tar i mot noe parameter
        self._celle = "doed"
        #Lager instansevariabel self._celle som har verdien "doed"
    def settDoed(self):
    #Lager metoden settDoed
        self._celle = "doed"
        #Sier at self._celle erlik "doed"

    def settLevende(self):
    #Lager metoden settLevende
        self._celle = "levende"
        #Sier at self._celle erlik "levende"

    def erLevende(self):
    #Lager metoden erLevende
        if self._celle == "levende":
        #Om self._celle erlik "levende" vil metoden returnere True
            return True
        else:
        #Om ikke self._celle erlik "levende" vil programmet returnere False
            return False

    def hentStatusTegn(self):
    #Lager metoden hentStatusTegn
        if self.erLevende():
        #Om metoden erLevende er True vil metoden returnere "O"
            return "O"
        else:
        #Om ikke erLevende er True vil metoden returnere "."
            return "."
