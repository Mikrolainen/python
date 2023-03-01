extends Node
#mirko kohava
#01.02.2023
#H4

func _ready():
	print("--------------------------------------------------------------------")
	var players = ["Feake","Bradwell","Dreger","Bloggett","Lambole","Daish","Lippiett","Blackie","Stollenbeck","Houseago","Dugall","Sprowson","Kitley","Mcenamin","Allchin","Doghartie","Brierly","Pirrone","Fairnie","Seal","Scoffins","Galer","Matevosian","DeBlase","Cubbin","Izzett","Ebi","Clohisey","Prater","Probart","Samwaye","Concannon","MacLure","Eliet","Kundt","Reyes"]
	var size = players.size()
	var suurim = players.max()
	players.sort()
	players.erase("reyes")
	players.append("Mirko")
	for player in players:
		print(player)
	print("suurim vaartus on: ",suurim)
	print("mangijate arv on: ",size)
	print(players[0])
