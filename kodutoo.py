#kodutoo
# mikrolainen (mirko kohava)
#it22


koik = [] 										#hoiab inimese poolt esitatud arvud meeles

kolm = 3										#selgitab arvutile mis asi on 3
for i in range(kolm):                                                                  #kusib inimeselt 3 korda tema tulemust
    vastus = int(input("Sisesta oma tulemus: "))                   #inimene annab 3 arvu
    koik.append(vastus)                                                              #lisab listile koik esitatud arvud
    
kesk = round(sum(koik)/kolm,2) 					#arvutab keskmise
print(f"Sinu keskmine tulemus on: {kesk} ") 			#annab inimesele keskmise

maks = max(koik) 								#leiab maksimum arvu
print(f"Sinu parim tulemus on: {maks} ") 			#leiab maksimum arvu esitatud arvudest
    
    
    
    