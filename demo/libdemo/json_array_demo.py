
import json

players = [ { 'name' : 'Ronaldo', 'age': 40},
            { 'name' : 'Carlos', 'age' : 35}
          ]

with open("players.json", "wt") as f:
     json.dump(players, f)  # write list[dict] to json array


