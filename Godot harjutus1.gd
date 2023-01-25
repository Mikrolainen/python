#mirko kohava
#25,01,2023
#harjutus1


extends Node

var rng = RandomNumberGenerator.new()

func _ready():
	var player = "mikrolainen"
	var life = 5
	
	print(player)
	print("elud: ",life)
	print("pikkus: ",len(player))
	rng.randomize()
	var random = rng.randi_range(0,19)
	print("arv: ",random)
	
