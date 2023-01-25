#mirko kohava
#25.01.2023
#harjutus2


extends Node

var rand = RandomNumberGenerator.new()
var prand = RandomNumberGenerator.new()

func _ready():
	var raha = 50
	var toode = 55
	if raha >= toode:
		print("sa saad osta seda toodet!")
	else:
		print("sul pole piisavalt raha!")
	print("-----------------------------------------")
	rand.randomize()
	var no = rand.randi_range(1,10)
	prand.randomize()
	var yes = prand.randi_range(1,10)
	print("kulg1: ",yes," kulg2: ",no)
	if no == yes:
		print("see on ruut")
		print("ruudu pindala on: ",no*yes)
	else: 
		print("see on ristkulik")
		print("ristkuliku pindala on: ",no*yes)
	print("-------------------------------------------")
	
	
