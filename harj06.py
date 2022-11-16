#mirko.kohava
#27.10.22
#harj06

failike=open("s6pru_l6ustaraamatus.txt","r")

reformikad = 0
kesikud = 0
erakonnad = []



for i in failike.readlines():
    ee,pe,er,kyl = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        kesikud+=1
    if er not in erakonnad:
        erakonnad.append(er)
    with open("yes.txt","a") as yes:
        yes.write(ee+" "+pe+"\n")

print(f"reformikaid kokku {reformikad}")
print(f"kesikud kokku {kesikud}")
print(f"erakondi kokku {erakonnad}")

failike.close()







