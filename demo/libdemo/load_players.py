import json

with open("players.json", "rt") as f:
    players = json.load(f)

for p in players:
    print(f"{p['name']:20}   {p['age']:2}")
