# Steps for program
# * Make a list of every different key in all entries.
# * Check and add missing keys from master list into every entry.

import json

def test():
	with open("items.json", encoding="utf8") as f:
		data = json.load(f)["item"]
		for i in data:
			for key in keyList:
				if key not in i.keys():
					print(i["name"] + " :: " + key)
	pass


def fix():
	newData = {"item":[]}
	with open("items.json", encoding="utf8") as f:
		data = json.load(f)["item"]
		for i in data:
			for key in keyList:
				if key not in i.keys():
					i[key] = []
			newData["item"].append(i)
		pass

	with open("items.json", "w", encoding="utf8") as f:
		json.dump(newData, f, indent=4)
		pass
	pass


keyList = []
with open("items.json", encoding="utf8") as f:
	data = json.load(f)["item"]
	for i in data:
		for key in i.keys():
			if key not in keyList:
				keyList.append(key)
	pass

fix()
test()