class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne:
            return "Potvrzuji zapůjčení vozidla." 
              
        else: 
            return "Vozidlo není k dispozici." 

    def get_info(self):
        return f"Osobní automobil {self.typ_vozidla} vlastní registrační značku {self.registracni_znacka}."


peugeot = Auto("4A2_3020", "Peugeot_403_Cabrio","47534")
skoda = Auto("1P3_4747", "Škoda_Octavia", "41253")

objednavka_auta = input("Jaké auto si přejete vypůjčit? Na výběr máte ze značek Peugeot a Škoda:\n")

if objednavka_auta == "Peugeot" or objednavka_auta == "peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())

elif objednavka_auta == "Škoda" or objednavka_auta == "škoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())

pujcene_auto = input("Jaké auto si přejete vypůjčit? Na výběr máte ze značek Peugeot a Škoda:\n")







    







