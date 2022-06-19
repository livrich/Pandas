""" Questions to Answer
1. (Filter) How many spells have a range of 'touch'?
2. (Filter) What spells can a Bard use?
"""

# import numpy as np
import json
import pandas as pd

# How to read dataset
df = pd.read_json("spells.json")

with open("spells.json") as file:
    spellData = json.load(file)
    pass

# Determine how many spells have a range of touch
total_touch_spells = 0
for spell in spellData["spell"]:
    if spell["range"] == "Touch":
        total_touch_spells += 1
        print(f"Touch spell {spell}")
        print()
print(f"There are a total of {total_touch_spells} touch spells")

# Determine how many spells Bards can use
bard_spells = []
for spell in spellData["spell"]:
    if "Bard" in spell["classes"]:
        bard_spells.append(spell)
        print(f"Bard spell {spell}")
        print()
total_bard_spells = len(bard_spells)
print(f"There are a total of {total_bard_spells} Bard spells")