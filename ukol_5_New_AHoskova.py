teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
   
ranni_teploty = [t[0] for t in teploty]
nocni_teploty = [t[-1] for t in teploty]
poledni_nocni_teploty = [[t[1],t[3]]for t in teploty]
prumerne_teploty = [sum(den) / len(den) for den in teploty]

print(ranni_teploty)
print(nocni_teploty) 
print(poledni_nocni_teploty)
print(prumerne_teploty)