import csv

class Database:
    def __init__(self, filmİsmi, imdbPuani, filmYil, filmTür, filmSüre, filmFragman):
        self.nadideparcalar = nadideparcalar
        
    def bilgi_kaydet(self, bilgi):
        with open(self.nadideparcalar, "a") as dosya:
            dosya.write(bilgi + "\n")