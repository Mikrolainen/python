#mirko
#1.11.22
#funktsioonid
import math

def kuup(a):
    print(f"kuubi ruumala on {a**3}")
def kera(r):
    print(f"kera ruumala on {round(4/3*math.pi*r**3,2)}")
def koonus(h):
    print(f"koonuse ruumala on {round(math.pi*h*2)}")
def silinder(g):
    print(f"silindri ruumala on {round(math.pi*g*2)}")

loop = 1
while loop ==1:
    print("********* LEIAME RUUMALA **********")
    valik = int(input("1.kuup\n2. kera\n3. koonus\n4, silinder\n5. välju\nTee valik 1-5: "))
    if valik == 1:
        a = int(input("lisa kuubi üks külg: "))
        kuup(a)
    elif valik == 2:
        r = int(input("lisa kera raadius: "))
        kera(r)
    elif valik == 3:
        h = int(input("lisa koonuse suurus: "))
        koonus(h)
    elif valik == 4:
        g = int(input("lisa silindri suurus: "))
        silinder(g)
    elif valik == 5:
        loop = 0
    else:
        print("sellist valikut pole!")

def tevita(nimi="tundmatu",keel="ge"):
    if keel=="et":
        print(f"tere {nimi}")
    elif keel=="en":
        print(f"hi {nimi}")
    else:
        print(f"hallo {nimi}")
tevita()
tevita("Mari","en")







