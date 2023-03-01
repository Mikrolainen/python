#mirko kohava
#01.03.2023



extends Node

var DMGrand = RandomNumberGenerator.new()
var reloadchance = RandomNumberGenerator.new()
var loss = RandomNumberGenerator.new()
var hitchance = RandomNumberGenerator.new()
var kuulid = 6
var koletis = 50
var skoor = 0.0
var kooku = 0.0
var succ = 0

func _process(delta):
	if koletis >= 0:
		if Input.is_action_just_pressed("piu piu piu"):
			
			kuulid -= 1
			DMGrand.randomize()
			hitchance.randomize()
			kooku += 1
			
			if kuulid > 0:
				print("pauk, mul on ",kuulid," kuuli jaanud")
				print(".")
			elif kuulid <= 0:
				print("Relva salv on otsas!!!")
				print(".")
				
			var yyy = DMGrand.randi_range(1,10)
			var hitchan = hitchance.randi_range(0,100)
			
			if hitchan < 20:
				print("Mõõda lasid!!!")
				print(".")
			else:
				print("Pihtas! Tegid ",yyy," DMG")
				print(".")
				skoor += 1
				koletis -= yyy
				print("Koletisel on ",koletis," elusid jarel")
				print(".")
				
		if Input.is_action_just_pressed("lae"):
			print("Laen relva...")
			print(".")
			
		if Input.is_action_just_released("lae"):
			
			reloadchance.randomize()
			loss.randomize()
			var aea = reloadchance.randi_range(0,100)
			var losso = loss.randi_range(1,3)
			
			if aea > 50:
				print("...Laetud")
				kuulid = 6
				print(".")
			else:
				print("Nässasid laadimise ära!!! Kaotasid ",losso," kuule salvest")
				kuulid = 6
				kuulid -= losso
				print(".")
				
		if Input.is_action_just_pressed("reloadcheck"):
			print("Sul on ",kuulid," kuuli jarel")
			print(".")
			
	else:
		get_tree().quit()
		succ = skoor/kooku*100
		print("------------------------------------Mang labi!----------------------------------")
		print("-     Punktid: ",skoor)
		print("-     laskude arv: ",kooku)
		print("-     Efektiivsus: ",succ)
		print("--------------------------------------------------------------------------------")
