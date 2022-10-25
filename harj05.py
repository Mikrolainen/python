#mirko kohava
#harj5
#25.10.22


#nimede lisamine loendisse

nimed = []
for i in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)

print(f"viimane nimi: {nimed[-1]}")
nimed.sort()
print(nimed)


#opilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]

for opilane in opilased:
    print (f"{jrk}. {opilane}")
    jrk+=1
    
mitmes = int(input("mitmendat soovid muuta? "))-1
vaheta = input("lise uus nimi: ")
del opilased[mitmes]
opilased.insert(mitmes, vaheta)
print(opilased)

#duplikaatid

opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
puh_opilased = []
for opilane in opilased:
    if opilane not in puh_opilased:
        puh_opilased.append(opilane)

print(puh_opilased)
    
#venused
































