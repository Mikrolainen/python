#mirko kohava
#it22
#harj3


a1,a2 = "8:30","14:15"
h1,m1 = a1.split(":")
minut1 = int(h1)*60+int(m1)
print(minut1)
h2,m2 = a2.split(":")
minut2 = int(h2)*60+int(m2)
ajavahe = minut2-minut1
vanaisa = 30/56+2
hh = ajavahe//60
mm = ajavahe%60
print(f"Ajavahe on {hh}:{mm}")

print(ajavahe)


email = "sobsfbspbdf@sdgj.rer"
print("@" in email)


tekst = input("ütle kurat küll!:")
print(tekst.lower().replace("kurat","***"))

