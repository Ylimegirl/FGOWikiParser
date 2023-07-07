item_ref = [[1, "QP"], [2, "Saint Quartz"], [3, "Mana Prism"], [13, "Friend Point"], [18, "Rare Prism"], [48, "Evocation Leaf"], [100, "Golden Apple"], [101, "Silver Apple"], [102, "Copper Apple"], [103, "Bronze Sapling"], [104, "Bronze Apple"], [6001, "Shining Gem of Swords"], [6002, "Shining Gem of Bows"], [6003, "Shining Gem of Lances"], [6004, "Shining Gem of Riding"], [6005, "Shining Gem of Spells"], [6006, "Shining Gem of Killing"], [6007, "Shining Gem of Madness"], [6101, "Magic Gem of Swords"], [6102, "Magic Gem of Bows"], [6103, "Magic Gem of Lances"], [6104, "Magic Gem of Rider"], [6105, "Magic Gem of Spells"], [6106, "Magic Gem of Killing"], [6107, "Magic Gem of Madness"], [6201, "Secret Gem of Swords"], [6202, "Secret Gem of Bows"], [6203, "Secret Gem of Lances"], [6204, "Secret Gem of Rider"], [6205, "Secret Gem of Spells"], [6206, "Secret Gem of Killing"], [6207, "Secret Gem of Madness"], [7001, "Saber Piece"], [7002, "Archer Piece"], [7003, "Lancer Piece"], [7004, "Rider Piece"], [7005, "Caster Piece"], [7006, "Assassin Piece"], [7007, "Berserker Piece"], [7101, "Saber Monument"], [7102, "Archer Monument"], [7103, "Lancer Monument"], [7104, "Lancer Monument"], [7105, "Rider Monument"], [7106, "Assassin Monument"], [7107, "Berserker Monument"], [6503, "Hero's Proof"], [6516, "Unlucky Bone"], [6512, "Dragon Fang"], [6505, "Void's Refuse"], [6522, "Chains of the Fool"], [6527, "Stinger of Certain Death"], [6530, "Magical Cerebrospinal Fluid"], [6533, "Night-Weeping Iron Stake"], [6534, "Stimulus Gunpowder"], [6549, "Tiny Bell of Amnesty"], [6551, "Twilight Ceremonial Blade"], [6552, "Unforgettable Ashes"], [6554, "Obsidian Edge"], [6502, "Yggdrasil Seed"], [6508, "Ghost Lantern"], [6515, "Octuplet Crystals"], [6509, "Snake Jewel"], [6501, "Phoenix Plume"], [6510, "Infinity Gear"], [6511, "Forbidden Page"], [6514, "Homunculus Baby"], [6513, "Meteoric Horseshoe"], [6524, "Medal of Great Knight"], [6526, "Seashell of Reminiscence"], [6532, "Kotan Magatama"], [6535, "Permafrost Ice Crystal"], [6537, "Giant's Ring"], [6536, "Aurora Steel"], [6538, "Ancient Bell of Tranquility"], [6541, "Arrowhead of Maledictions"], [6543, "Crown of Radiant Silver"], [6545, "Divine Leyline Spiritron"], [6547, "Rainbow Yarn"], [6550, "Scales of Fantasies"], [6553, "Sunscale"], [6507, "Talon of Chaos"], [6517, "Heart of a Foreign God"], [6506, "Dragon's Reverse Scale"], [6518, "Spirit Root"], [6519, "Warhorse's Immature Horn"], [6520, "Bloodstone Tear"], [6521, "Black Tallow"], [6523, "Lamp of Demon Sealing"], [6525, "Scarab of Wisdom"], [6528, "Primordial Lanugo"], [6529, "Cursed Beast Cholecyst"], [6531, "Bizarre Godly Wine"], [6539, "Dawnlight Reactor Core"], [6540, "Tsukumo Mirror"], [6542, "Genesis Egg"], [6544, "Comet Shard"], [6546, "Fruit of Longevity"], [6548, "Demonic Flame Hōzuki"], [6999, "Crystallized Lore"]]

def itemLookup(id, type, count):
	if(type == "item"):
		for item in item_ref:
			if(id == item[0]):
				if(count == 1):
					return "{{" + item[1] + "}}"
				else:
					return "{{" + item[1] + "|" + '{:,}'.format(count) + "}}"
		return " [https://apps.atlasacademy.io/db/JP/item/" + str(id) + " Item #" + str(id) + " ×" + '{:,}'.format(count) + "]"
	elif(type == "servant"):
		return " [https://apps.atlasacademy.io/db/JP/enemy/" + str(id) + " EXP Card " + str(id) + " ×" + '{:,}'.format(count) + "]"
	elif(type == "questRewardIcon"):
		if(id == 8):
			return "NP Upgrade"
		if(id == 9):
			return "Skill Upgrade"
	else:
		return "Unknown Item " + str(id)