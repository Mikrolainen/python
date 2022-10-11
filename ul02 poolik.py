#mirko kohava
#11.okt 2022
#ul02
import math


#pitsa
kogus = 1
hind = 12.90
jootraha = 1.29
summa = round(((hind+jootraha)*kogus))
print(kogus,"toote hind on",summa,"€")

#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round(hind+(hind*ale)*kogus,2)
print(kogus,"toote hind on",summa,"€")

#rulluisitajad



#hupotenuus
a,b = 16,9
c = round(math.sqrt(pow(a,2)+pow(b,2)),2)
print("hupotenuus on",c)

#ajateisendus
minutid = int(input("sisesta minutid:"))
h = minutid//60
m = minutid%60
print("vastus on",h,";",m)


a,b,c= 30,30,30

p=a+b+c
print("kolmnurga ümbermõõt on:",p)