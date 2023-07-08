from items import itemLookup
from mobs import mobLookup
def questHeader(quest, new_file):
	new_file.write("{{Questheader\n|ap = " + str(quest["consume"]) + "\n")
	new_file.write("|bond = ")
	if "bond" in quest.keys():
		new_file.write('{:,}'.format(quest["bond"]))
	else:
		new_file.write("0")
	new_file.write("\n|qp = ")
	if "qp" in quest.keys():
		new_file.write('{:,}'.format(quest["qp"]))
	else:
		new_file.write("0")
	new_file.write("\n|exp = ")
	if "exp" in quest.keys():
		new_file.write('{:,}'.format(quest["exp"]))
	else:
		new_file.write("0")
	new_file.write("\n|image = " + "\n")
	new_file.write("|jpnodename = " + quest["spotName"] + "\n")
	new_file.write("|ennodename = " + "\n")
	new_file.write("|jpname = " + quest["name"] + "\n")
	new_file.write("|enname = " + "\n")
	new_file.write("|type =")
	if "individuality" in quest.keys():
		for indiv in quest["individuality"]:
			if(indiv["name"] != "unknown"):
				new_file.write(" {{Battlefield Type|" + indiv["name"][5:].lower() + "}}")
	else:
		new_file.write(" ")
	new_file.write("\n}}\n")

def questBody(quest, new_file):
	if "phasesWithEnemies" in quest.keys() and not "stages" in quest.keys():
		new_file.write("<center>'''MISSING QUEST DATA'''<br />(Parse the [https://api.atlasacademy.io/nice/JP/quest/" + str(quest["id"]) + " quest's JSON file] for this information!)</center>\n")
	elif "noBattle" in quest["flags"]:
		new_file.write("<center>'''NO BATTLE'''</center>\n")
	elif "stages" in quest.keys():
		new_file.write("{{Questbody\n")
		for wave in quest["stages"]:
			currWave = str(wave["wave"])
			new_file.write("|battle" + currWave + " = Battle " + currWave + "/" + str(len(quest["stages"])) + "\n")
			for enemy in wave["enemies"]:
				new_file.write("|en" + currWave + str(enemy["deckId"]) + " = ")
				if enemy["svt"]["collectionNo"] != 0:
					new_file.write("[[" + mobLookup(enemy["svt"]["name"], enemy["svt"]["collectionNo"]) + "|" + enemy["name"] + "]];")
				else:
					new_file.write("[https://apps.atlasacademy.io/db/JP/enemy/" + str(enemy["svt"]["id"]) + " " + enemy["name"] + "]")
				new_file.write(" Lvl " + str(enemy["lv"]) + " {{")
				if enemy["svt"]["className"] == "alterego":
					new_file.write("Alter Ego")
				elif enemy["sv"]["className"] == "mooncancer":
					new_file.write("Moon Cancer")
				else:
					new_file.write(enemy["svt"]["className"].capitalize())
				if(enemy["svt"]["rarity"] == 1 or enemy["svt"]["rarity"] == 2):
					new_file.write("Bronze")
				elif(enemy["svt"]["rarity"] == 3):
					new_file.write("Silver")
				new_file.write("}} " + '{:,}'.format(enemy["hp"]) + " HP\n")
		
		new_file.write("|dropicons =")
		for group in quest["drops"]:
			new_file.write(itemLookup(group["objectId"], group["type"], group["num"], False))
		new_file.write("\n")
		new_file.write("}}\n")
	else:
		new_file.write("<center>'''NO BATTLE'''</center>\n")

def questFooter(quest, new_file):
	new_file.write("{{Questfooter\n")
	new_file.write("|reward =")
	for group in quest["gifts"]:
		new_file.write(itemLookup(group["objectId"], group["type"], group["num"], True))
	new_file.write("\n")
	new_file.write("}}\n")