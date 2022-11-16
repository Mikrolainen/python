#mirko kohava
#it22
#harj4


j=1
for i in range (5):
    print("* " * j)
    j+=1
    
    
J=1
for i in range (5):
    print("* " * j)
    j-=1
    
#loto
import random
for i in range(5):
    print(random.randint(0,9),end="")
    
#paaris/paaritu
    
for i in range(10):
    if i%2==0:
        print(f"{i} paaris")
    else:
        print(f"{i} paaritu")
    
#korrustustabel

arv = 5
for i in range(1,11):
    print(f"{arv}*{i}={arv*i}")
        
        
#viisikud
    
for i in range(1,101):
    if i%5==0:
        print(i)
    
    
#arvamismang
    
loop = 1

while loop==1:
    arv = random.randint(1,10)
    print(arv)
    for i in range(3):
        pakkumine = int(input("arva arv 1-10: "))
        if pakkumine==arv:
            print("tubli")
            break
        else:
            print("proovi jälle")
    loop = int(input("jätka 1/0: "))
print("game over")
    
