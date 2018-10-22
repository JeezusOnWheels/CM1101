from items import *

dialogue_start = {
    "name": "Bedroom",
    "description":
    """You wake up and a long night of heavy drinking is catching up on you. Have you just dreamt about Kirill? Confused, you look for something to hold on to. Your stomach is rambling, and a massive headache has made its appearance. Wait, are you even alive? More confused, you look through the window and you are kind of proud that you woke up early for once. It must be Kirill. 
""",
    "numbers": {"1": dialogue_stretch, "2": "Tutor", "3": "Parking"}
}

dialogue = {
    "1": dialogue_start,
    "2": dialogue_stretch,
    "3": room_tutor,
    "4": room_parking,
    "5": room_office
}
