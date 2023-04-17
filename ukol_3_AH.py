import json

with open('body.json', encoding='UTF-8')as file:
    prospech = json.load(file)
   
with open('prospech.json', mode='w', encoding='UTF-8')as file:
    for name,points in prospech.items():
        if prospech[name] >= 60:
           prospech[name] = 'Pass'
        else:
            prospech[name] = 'Fail'
    print(prospech)
    json.dump(prospech, file, ensure_ascii=False)
 



