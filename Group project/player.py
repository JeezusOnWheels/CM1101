from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
stats = {"health": 500}
spells = {"spell1": 50, "spell2" : 20}
# Start game at the reception
current_room = rooms["Reception"]
player_in_battle = False
