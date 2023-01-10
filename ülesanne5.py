#harj04
#it22
#mirko kohava


#juubel
sp = "5.6.2002"
p,k,a = sp.split(".")
vanus = 2022-int(a)
if vanus%5 == 0:
    print("jah")
else:
    print("ei")


#matem
a,b = 10,20
tehe = input("vali tehe (+ - * /): ")
if tehe=="+":
    vastus = a + b
elif tehe=="-":
    vastus = a - b
    
else:
    vastus = "N/A"
print(f"{a} {tehe} {b} = {vastus}")

#ruut
a,b = 10,20
if a==b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} teevad kokku ristküliku")













