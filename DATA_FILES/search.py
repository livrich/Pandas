import json

# Monster Search
# ==============
class Monsters:
	def __init__(self):
		self.monster = '''
### {name}
cr: {cr}  
HP: {health}, AC: {ac}, {speed}  
- Passive: {passive}  
- Senses: {senses}  
- Traits: {traits}  
  
STR {st} | DEX {dex} | CON {con} | INT {inte} | WIS {wis}| CHA {cha}  
{actions}  
'''

		self.monster_action = '''
{name}  
{text}
'''
	
	# By Name
	def name(self, name):
		monsterData = {}
		with open("monsters.json", encoding="utf8") as f:
			monsterData = json.load(f)["monster"]
			pass
		
		for i in monsterData["monster"]:
			if name.lower() in i["name"].lower():
				acts = ""
				for ii in i["action"]:
					acts += self.monster_action.format(name=ii["name"], text=ii["text"])
					pass
				trat = ""
				for ii in i["trait"]:
					trat += self.monster_action.format(name=ii["name"], text=ii["text"])
					pass

				print(self.monster.format(name=i["name"], cr=i["cr"], health=i["hp"], ac=i["ac"], speed=i["speed"],
									st=i["str"], dex=i["dex"], con=i["con"], inte=i["int"], wis=i["wis"], cha=i["cha"],
									passive=i["passive"], senses=i["senses"], traits=trat, actions=acts))
				print("\n")
				pass
			pass
		pass
	
	# By CR
	def cr(self, low, high):
		monsterData = {}
		with open("monsters.json", encoding="utf8") as f:
			monsterData = json.load(f)
			pass
		for i in monsterData["monster"]:
			if low <= eval(i["cr"]) and high >= eval(i["cr"]):
				acts = ""
				for ii in i["action"]:
					acts += self.monster_action.format(name=ii["name"], text=ii["text"])
					pass
				trat = ""
				for ii in i["trait"]:
					trat += self.monster_action.format(name=ii["name"], text=ii["text"])
					pass

				print(self.monster.format(name=i["name"], cr=i["cr"], health=i["hp"], ac=i["ac"], speed=i["speed"],
                                    st=i["str"], dex=i["dex"], con=i["con"], inte=i["int"], wis=i["wis"], cha=i["cha"],
                                    passive=i["passive"], senses=i["senses"], traits=trat, actions=acts))
				print("\n")
				pass
			pass
		pass
	

# Spell Search
# ============
class spells:
	def spell(search_term):
		spellData = {}
		with open("spells-phb.json") as f:
			spellData = json.load(f)
			pass

		# TODO: Finish adding areas for information.
		spell_temp = '''
		{name} {level}
		School: {school}
		'''

		for spell in spellData["spell"]:
			if search_term in spell["name"].lower():
				print(spell)
				print("\n")
		pass
