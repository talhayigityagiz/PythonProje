import csv

class Database:
    def __init__(self,nadideparcalar.):
        self.nadideparcalar = nadideparcalar
        
    def bilgi_kaydet(self, bilgi):
        with open(self.nadideparcalar, "a") as dosya:
            dosya.write(bilgi + "\n")