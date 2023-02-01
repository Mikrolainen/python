#mirko kohava
#01.02.2023
#H3
extends Node


var rand = RandomNumberGenerator.new()
var prand = RandomNumberGenerator.new()

func _ready():
	var p1 = 100
	var p2 = 100
	while p1 > 0 and p2 > 0:
		rand.randomize()
		var no = rand.randi_range(1,20)
		rand.randomize()
		var yes = prand.randi_range(8,15)
		p1 -= no
		print("P2 DMG:",no,", P1 Life:",p1)
		p2 -= yes
		print("P1 DMG:",yes,", P1 Life:",p2)
	if p1 < 0:
		print("p1 voitis!")
	else:
		print("p2 voitis!")
