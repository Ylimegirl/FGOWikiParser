import os, json, requests
from pretty import prettyJSON
from items import itemLookup
from mobs import mobLookup
from quest import questHeader, questBody, questFooter

if not os.path.exists("inputs"):
	os.mkdir("inputs")
if not os.path.exists("outputs"):
	os.mkdir("outputs")

files = os.listdir("inputs")
verNum = "0.3.0" # Update this with new releases!!!


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
			print("> Parsing war " + str(dict["id"]) + ":")
			for spot in dict["spots"]:
				for quest in spot["quests"]:
					phases = len(quest["phases"])
					phase1 = requests.get("https://api.atlasacademy.io/nice/JP/quest/" + str(quest["id"]) + "/1").json()
					questHeader(phase1, new_file)
					if phases > 1:
						new_file.write("<tabber>\nArrow 1=\n")
						questBody(phase1, new_file)
						print(">> Parsed quest " + str(quest["id"]) + " phase 1")
						for x in range(2, phases+1):
							new_file.write("|-|\nArrow " + str(x) + "=\n")
							try:
								questBody(requests.get("https://api.atlasacademy.io/nice/JP/quest/" + str(quest["id"]) + "/" + str(x)).json(), new_file)
							except:
								new_file.write("API request for quest " + str(quest["id"]) + " phase " + str(x) + " failed\n")
							else:
								print(">> Parsed quest " + str(quest["id"]) + " phase " + str(x))
						new_file.write("</tabber>\n")
					else:
						questBody(phase1, new_file)
						print(">> Parsed quest " + str(quest["id"]) + " phase 1")
					questFooter(phase1, new_file)
					new_file.write("\n")
					
		else:
			questHeader(quest, new_file)
			questBody(quest, new_file)
			questFooter(quest, new_file)

		new_file.write("---------------------------------------------\nFGO Wiki Parser v" + verNum + " by Ylimegirl\nhttps://github.com/Ylimegirl")
		new_file.close()
		
		print("> Parsed " + item)

print("Finished parsing all files.")