
def overeni_cisla(cislo):       
    if len(cislo) == 9:
        return True
    elif cislo [:4] == ('+420') and len(cislo) == 13:
        return True
    else:
        return False
        exit()
       

def cena_zpravy(zprava, cena_za_znak=3):
    if len(zprava) <= 180:
        print(f'Zpráva bude za {cena_za_znak} Kč.')
    elif len(zprava) <= 360:
        print(f'Zpráva bude za {cena_za_znak *2} Kč.')
    elif len (zprava) <= 540:
        print(f'Zpráva bude za {cena_za_znak *3} Kč.')
    else:
        print(f'Zpráva bude za {cena_za_znak *4} Kč.')
    
    
 
cislo = input('Zadejte telefonní číslo:\n')

if overeni_cisla(cislo) == True:
    zprava = input('Zadejte text zprávy:\n')
    cena_zpravy(zprava)
else: 
    print('Chybné telefonní číslo.')








    



