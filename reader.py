import os, json, requests
from pretty import prettyJSON
from items import itemLookup
from mobs import mobLookup

def parseQuest(quest):
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
				new_file.write("|en" + currWave + str(enemy["deckId"]) + " = [[" + mobLookup(enemy["svt"]["name"], enemy["svt"]["collectionNo"]) + "|" + enemy["name"] + "]];")
				new_file.write(" Lvl " + str(enemy["lv"]) + " {{" + enemy["svt"]["className"].capitalize())
				if(enemy["svt"]["rarity"] == 1 or enemy["svt"]["rarity"] == 2):
					new_file.write("Bronze")
				elif(enemy["svt"]["rarity"] == 3):
					new_file.write("Silver")
				new_file.write("}} " + '{:,}'.format(enemy["hp"]) + " HP\n")
		
		new_file.write("|dropicons =")
		for group in quest["drops"]:
			new_file.write(" " + itemLookup(group["objectId"], group["type"], group["num"]))
		new_file.write("\n")
		new_file.write("}}\n")
	else:
		new_file.write("<center>'''NO BATTLE'''</center>\n")
	
	new_file.write("{{Questfooter\n")
	new_file.write("|reward =")
	for group in quest["gifts"]:
		new_file.write(" " + itemLookup(group["objectId"], group["type"], group["num"]))
	new_file.write("\n")
	new_file.write("}}\n")

if not os.path.exists("inputs"):
	os.mkdir("inputs")
if not os.path.exists("outputs"):
	os.mkdir("outputs")

files = os.listdir("inputs")
verNum = "0.2.0" # Update this with new releases!!!


print("Parsing files...")


for item in files:
	#grab original text
	ref = open("inputs/" + item, encoding="utf-8")
	parsed = ref.read()
	ref.close()
	
	#prettified output (for debugging/reference)
	#prettyJSON(parsed, item)
	
	try:
		dict = json.loads(parsed)#converts json to dict format
	except json.decoder.JSONDecodeError:
		print("> Didn't parse " + item + " (file not in JSON format)")
	except:
		print("> Didn't parse " + item + " (failed to read JSON file)")
	else: 
		newname = "outputs/" + item[0:item.find(".")] + "_parsed.txt"
		if os.path.exists(newname):#deletes _parsed file if it already exists
			os.remove(newname)
		new_file = open(newname, "a", encoding="utf-8")
		
		if "spots" in dict.keys():
			for spot in dict["spots"]:
				for quest in spot["quests"]:
					questJSON = requests.get("https://api.atlasacademy.io/nice/JP/quest/" + str(quest["id"]))
					if(questJSON.status_code == 200):
						print(">> API request for quest " + str(quest["id"]) + " successful")
						phases = questJSON.json()["phases"][0]
						for x in range(1, phases+1):
							parseQuest(requests.get("https://api.atlasacademy.io/nice/JP/quest/" + str(quest["id"]) + "/" + str(x)).json())
							print(">>> Parsed quest " + str(quest["id"]) + " phase " + str(x))
					else:
						parseQuest(quest)
					new_file.write("\n")
					
		else:
			parseQuest(dict)

		new_file.write("---------------------------------------------\nFGO Wiki Parser v" + verNum + " by Ylimegirl\nhttps://github.com/Ylimegirl")
		new_file.close()
		
		print("> Parsed " + item)

print("Finished parsing all files.")