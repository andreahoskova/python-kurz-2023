sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

code = input("Zadej kod součástky:\n")
amount = 0

if code in sklad:
  amount = int(input("Zadej množství:\n"))
else:
  print("Součástka není skladem.")
  exit()

if amount > sklad[code]:
  print("Prodat lze omezené množství kusů.")
  sklad.pop(code) 
  print(sklad)
elif amount <= sklad[code]:
  print("Poptávku lze uspokojit v plné výši.")
  sklad[code] = sklad[code] - amount
  print(sklad)
