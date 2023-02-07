#mirko kohava
#07.02.2023
#harj5

extends Node

var rand = RandomNumberGenerator.new()

func _ready():
	var tunnid = rand.randomize()
	var no = rand.randi_range(1,10)
	print(tunnid)
	print("----------------------------------")
