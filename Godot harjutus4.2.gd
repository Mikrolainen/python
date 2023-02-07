#mirko kohava
#07.02.2023
#harj 4.2

extends Node

func _ready():
	var player = {"name":"Mirko", "health":78, "items":["sword","bread","shield"], "gold":3}
	for i in range(5): 
		player.gold += 7
	print("Mirko kulla arv on: ",player.gold)
	print("--------------------------------------------------")

