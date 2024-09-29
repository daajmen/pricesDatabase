class ReceiptData:
    def __init__(self):
        self.datum = None
        self.beskrivning = None
        self.artikelnummer = None
        self.antal = None
        self.pris = None
        self.summa = None
        self.butik = None 

    # Metod för att uppdatera datum
    def set_datum(self, datum):
        self.datum = datum
    
    # Metod för att uppdatera artikelnummer
    def set_artikelnummer(self, artikelnummer):
        self.artikelnummer = artikelnummer
    
    # Metod för att uppdatera beskrivning
    def set_beskrivning(self, beskrivning):
        self.beskrivning = beskrivning
    
    # Metod för att uppdatera antal
    def set_antal(self, antal):
        self.antal = antal
    
    # Metod för att uppdatera pris
    def set_pris(self, pris):
        self.pris = pris
    
    # Metod för att uppdatera summa
    def set_summa(self, summa):
        self.summa = summa

    # Metod för att uppdatera butik
    def set_butik(self, butik):
       self.butik = butik

 # En extra metod för att visa all data i kvittot
    def visa_data(self):
        return {
            "datum": self.datum,
            "artikelnummer": self.artikelnummer,
            "beskrivning": self.beskrivning,
            "antal": self.antal,
            "pris": self.pris,
            "summa": self.summa,
            "butik": self.butik
        }

