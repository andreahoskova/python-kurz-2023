
def overeni_cisla(cislo):       
    if len(cislo) == 9:
        return True
    elif cislo [:4] == ('+420') and len(cislo) == 13:
        return True


import math      

def cena_zpravy(zprava, cena_za_znak = 3):
    pocet_bloku = math.ceil(len(zprava) / 180) 
    cena_zpravy = pocet_bloku * cena_za_znak
    print(f'Cena sms zprávy bude {cena_zpravy} Kč.')
   

cislo = input('Zadejte telefonní číslo:\n')

if overeni_cisla(cislo):
    zprava = input('Zadejte text zprávy:\n')
    cena_zpravy(zprava)
else: 
    print('Chybné telefonní číslo.')





    



