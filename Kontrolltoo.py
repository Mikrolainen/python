# mirko kohava it22
#kontrolltoo
#21.11

import random

temp = []

loop = 1

while loop==1:
    kord = int(input("Mitu arvu tahad kuvada?: "))
    vahemik = int(input("Mis arvu vahemikus tahad alustada?: "))
    vahemi = int(input("Mis arvu vahemikus tahad lõpetada?: "))
    

    for i in range(kord):
        randid = random.randint(vahemik,vahemi)
        temp.append(randid)
        
    print(f"Viimati mõõdetud tulemus on: {temp[-1]} ")
    print(f"Väiksem temperatuur on {min(temp)} ")
        
    print(f"Suurim temperatuur on {max(temp)} ")
    
    loop = int(input("Kas soovite uuesti teha?(1/0): "))
print("Head aega!")










