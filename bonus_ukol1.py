#všechna písmena velká
jmeno_a_prijmeni = input('Zadej své jméno a příjmení:\n')
print(jmeno_a_prijmeni.upper())

#všechna písmena malá
jmeno_a_prijmeni = input('Zadej své jméno a příjmeni:\n')
print(jmeno_a_prijmeni.lower())

#standardní varianta - první písmeno vždy velké


#křestní jméno zkrácené na první písmeno a příjmení, 
#pokud je křestní jméno delší než 5 znaků, jinak 
#vypíše standardní variantu

#vyprintování iniciálu jména a příjmení uživatele:
jmeno = input('Zadej jméno:\n')
prijmeni = input('Zadej příjmeni:\n')
inicialy = jmeno[0] + prijmeni[0]
print('Iniciály:', inicialy.upper())