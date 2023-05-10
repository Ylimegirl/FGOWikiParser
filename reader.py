import os, json
from pretty import prettyJSON
from items import itemLookup
from mobs import mobLookup

if not os.path.exists("inputs"):
	os.mkdir("inputs")
if not os.path.exists("outputs"):
	os.mkdir("outputs")

files = os.listdir("inputs")
verNum = "0.1.0" # Update this with new releases!!!


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
		
		new_file.write("{{Questheader\n|ap = " + str(dict["consume"]) + "\n")
		new_file.write("|bond = " + str(dict["bond"]) + "\n")
		new_file.write("|qp = {{subst:formatnum:" + str(dict["qp"]) + "}}\n")
		new_file.write("|exp = {{subst:formatnum:" + str(dict["exp"]) + "}}\n")
		new_file.write("|image = " + "\n")
		new_file.write("|jpnodename = " + "\n")
		new_file.write("|ennodename = " + "\n")
		new_file.write("|jpname = " + "\n")
		new_file.write("|enname = " + dict["name"] + "\n")
		new_file.write("|type = {{Battlefield Type|" + dict["individuality"][0]["name"][5:].lower() + "}}\n")
		new_file.write("}}\n")
		
		new_file.write("{{Questbody\n")
		for wave in dict["stages"]:
			currWave = str(wave["wave"])
			new_file.write("|battle" + currWave + " = Battle " + currWave + "/" + str(len(dict["stages"])) + "\n")
			for enemy in wave["enemies"]:
				new_file.write("|en" + currWave + str(enemy["deckId"]) + " = [[" +mobLookup(enemy["svt"]["name"], enemy["svt"]["collectionNo"]) + "|" + enemy["name"] + "]];")
				new_file.write(" Lvl " + str(enemy["lv"]) + " {{" + enemy["svt"]["className"].capitalize())
				if(enemy["svt"]["rarity"] == 1 or enemy["svt"]["rarity"] == 2):
					new_file.write("Bronze")
				elif(enemy["svt"]["rarity"] == 3):
					new_file.write("Silver")
				new_file.write("}} {{subst:formatnum:" + str(enemy["hp"]) + "}} HP\n")
		
		new_file.write("|dropicons =")
		for group in dict["drops"]:
			new_file.write(" " + itemLookup(group["objectId"], group["type"], group["num"]))
		new_file.write("\n")
		new_file.write("}}\n")
		
		new_file.write("{{Questfooter\n")
		new_file.write("|reward =")
		for group in dict["gifts"]:
			new_file.write(" " + itemLookup(group["objectId"], group["type"], group["num"]))
		new_file.write("\n")
		new_file.write("}}\n")

		new_file.write("---------------------------------------------\nFGO Wiki Parser v" + verNum + " by Ylimegirl\nhttps://github.com/Ylimegirl")
		new_file.close()
		
		print("> Parsed " + item)

print("Finished parsing all files.")