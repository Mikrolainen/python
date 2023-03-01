#mirko kohava
#07.02.2023
#harj5

extends Node

func _ready():
	raha(41,10)
	jahhinne([7,28,64,51,81,40,21,73,34,98,39,17,33,85,35,44])
	jah2([7,28,64,51,81,40,21,73,34,98,39,17,33,85,35,44])
	jahkesk([7,28,64,51,81,40,21,73,34,98,39,17,33,85,35,44])

func jahkesk(punktid):
	punktid.average()
	print(punktid.average)
func jah2(punktid):
	print(punktid)
	
func jahhinne(punktid):
	var kahteviisi = 25
	if punktid <= kahteviisi:
		var taun = 2
		print("su punkti summa on: ",punktid,"selle summaga sa saad hinde: ",taun)
	elif punktid >= 25:
		var norm = 3
		print("su punkti summa on: ",punktid,"selle summaga sa saad hinde: ",norm)
	elif punktid >= 50:
		var ok = 4
		print("su punkti summa on: ", punktid,"selle summaga sa saad hinde: ",ok)
	else:
		var hea = 5
		print("su punkti summa on: ", punktid,"selle summaga sa saad hinde: ",hea)
func raha(no,tunnipalk):
	print("see kuu sa tootasid: ",no," tundi")
	var rahad = 0
	if no <= 40:
		rahad = no*tunnipalk
	else:
		rahad = 40*tunnipalk+(no-40)*1.5*no
	print("Sinu kuupalga summa on: ",rahad,"€")
	
	print("----------------------------------")
	
