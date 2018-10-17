from items import *
from weapons import *
enemy_hangover = {
    "id": "hangover",
    "description":"I swear to God, I will never drink again!!! My head feels like it is about to explode!!!",
    "ability_damage":{"ability1": 10, "ability2": 20, "ability3" : 30},
    "health": 100,
    "alive": True,
    "weapons":[weapon_beginners_sword],
    "items":[]
}

enemy_minion = {
    "id": "minion",
    "description":"It has seen better days. At least it has a WiFi card!",
    "ability_damage":{"ability1": 10, "ability2": 20, "ability3" : 30},
    "health": 100,
    "alive": True
}

enemy_barbian = {
    "id": "barbarian",
    "description":"This wad of cash is barely enough to pay your tuition fees.",
    "ability_damage":{"ability1": 10, "ability2": 20, "ability3" : 30},
    "health": 100,
    "alive": True
}
enemy_all = {
    "hangover": enemy_hangover,
    "minion": enemy_minion,
    "barbian": enemy_barbian
}
