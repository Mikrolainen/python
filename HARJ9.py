#mirko
#harj9
#1.11.22
import locale
import datetime

aeg = datetime.datetime.now()
print(aeg.strftime("%d.%m.%Y %H:%M:%S"))

locale.setlocale(locale.LC_ALL, "et_EE")

print(aeg.strftime("%d.%B.%Y"))

ik ="50508134227"
sp = datetime.date(int("20"+ik[1:3]),int(ik[3:5]),int(ik[5:7]))
print(sp)

age = aeg.year - sp.year - ((aeg.month, aeg.day) < (aeg.month, aeg.day))
print(age)


