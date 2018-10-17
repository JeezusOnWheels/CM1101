#!/usr/bin/python3 LOL

from map import rooms
from player import *
from items import *
from gameparser import *
from weapons import *
from enemies import *
from game_ascii_art import *
import random
def is_winning():
    i = 0
    for a in rooms["Start"]["items"]:
        i = i+1
    if i==6:
        return True
    else:
        return False
def print_introduction_to_game():
    print(game_title_in_ascii)
    print("\n")
    print("WELCOME TO DORK!!!")
    print("Dork is a text-based adventure game with turn based combat and is not in any way related to Zork")
    print("You must battle monsters and NPCs to earn loot so eventually you can defeat the final boss 'Kirril' who is not in any way related to Kirill")
    print("You start off with skillpoints which can be invested to make a unique build. Different builds may be appropriate for different enemies. You can retrain to reallocate them")
    print("Extra challange is to try to find a way to break the game (this will only be a challange when the game is finnished because currently there are many bugs")
    print("GOOD LUCK!")
def display_information(enemy_id, turn):
    print ("This is turn " + str(turn))
    print ("The enemy health is: " + str(enemy_all[enemy_id]["health"]))
    print ("My health is: " + str(stats["health"]))
    print ("You can:")
    for spell in spells:
        print ("CAST " + spell + " to do " + str(spells[spell]) + " damage!")
    for weapon in player_weapons:
        print("ATTACK " + weapon["id"] + " to attack with " + weapon["id"] + " to deal " + str(weapon["damage"]) + " damage!")
def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    if (items == []):
    	return ""
    string = ""
    for item in items:
    	string = string + item["name"] + ", "
    try:
    	string = string[0:len(string)-2]
    except:
    	return ""
    return string

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if room["items"] == []:
    	return 
    print ("There is " + list_of_items(room["items"]) + " here.\n")
def print_room_weapons(room):
    if room["weapons"] == []:
    	return 
    print ("There is " + list_of_items(room["weapons"]) + " here.\n")

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    print ("You have " + list_of_items(items) + ".\n")

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print("")
    print(room["name"].upper())
    print("")
    # Display room description
    print(room["description"])
    print("")
    print_room_items(room)
    #
    # COMPLETE ME!
    #

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items, room_weapons, player_weapons, room_enemies):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
    	print("TAKE " + item["id"] + " to take " + item["name"])
    for item in inv_items:
    	print("DROP " + item["id"] + " to drop " + item["name"])
    for weapon in room_weapons:
        print("EQUIP " + weapon["id"] + " to equip " + weapon["id"])
    for weapon in player_weapons:
        print("UNEQUIP " + weapon["id"] + " to drop " + weapon["id"])
    for enemy in room_enemies:
        print("BATTLE " + enemy["id"] + " to battle " + enemy["id"])
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    #print (current_room)
    global current_room
    current_room = move(current_room["exits"], direction)


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    #Try to loop through the items in the current room
    #try:
    i = 0
    total_sum_of_items = 0
    actual_item = items_all[item_id]
    for element in current_room["items"]:
        if actual_item == element:
            for myinvitem in inventory:
                total_sum_of_items = total_sum_of_items + myinvitem["mass"]
            if (total_sum_of_items + element["mass"] > 3.0):
                print ("You cannot take that")
                print ("It is too heavy :/")
                return
            current_room["items"].pop(i)
            inventory.append(element)
            print("you picked up "+ element["name"])
            return
        i = i + 1
    print ("You cannot take that")
    return

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    i = 0
    actual_item = items_all[item_id]
    for element in inventory:
        if actual_item == element:
            current_room["items"].append(element)
            inventory.pop(i)
        i = i + 1
def execute_unequip(weapon_id):
    """This function takes a weapon id as an argument and moves the item from player's inventory to the room weapons
    """
    i = 0
    actual_item = weapon_all[weapon_id]
    for element in player_weapons:
        if actual_item == element:
            current_room["weapons"].append(element)
            player_weapons.pop(i)
        i = i + 1
def execute_monster_drop(item, monster_id): #This function drops an item that a monster has
    i = 0
    for element in enemy_all[monster_id]["weapons"]:
        if item == element:
            current_room["weapons"].append(element)
            enemy_all[monster_id]["weapons"].pop(i)
        i = i + 1
def execute_equip(item_id):
    i = 0
    total_sum_of_items = 0
    actual_item = weapon_all[item_id]
    for element in current_room["weapons"]:
        if actual_item == element:
            current_room["weapons"].pop(i)
            player_weapons.append(element)
            print("you equipped up "+ element["id"])
            return
        i = i + 1
    print ("You cannot equip that")
    return
def execute_battle(enemy_id):
    """This function puts a player in battle. And takes enemy ID as an argument (E.g. troll)"
    """
    global player_in_battle
    player_in_battle = True
    turn = 1
    print(enemy_all[enemy_id]["description"])
    while (stats["health"] > 0) and (enemy_all[enemy_id]["health"] > 0): #checks if both players still have positive hp
        display_information(enemy_id, turn)
        user_input = input("> ")
        user_input = normalise_input(user_input)#get nice input from user
        damage_player = execute_command(user_input) #calculate the damage the spell or attack will do
        print (damage_player)
        enemy_all[enemy_id]["health"] = enemy_all[enemy_id]["health"] - damage_player #Take damage away from the monster
        
        #get enemy to do a move!
        enemy_attack = random.randint(1,len(enemy_all[enemy_id]["ability_damage"]) - 1) #enemy chooses randomly which spell to use!
        stats["health"] = stats["health"] - enemy_all[enemy_id]["ability_damage"]["ability"+str(enemy_attack)]
        turn = turn + 1
    if (stats["health"] > 0):#if player has won
        print("You have defeated the " + enemy_all[enemy_id]["id"])
        print("He has dropped the following loot: ")
        for item in enemy_all[enemy_id]["weapons"]:
            print(item["id"])
            execute_monster_drop(item, enemy_id)
        player_in_battle = False
def calculate_damage(spell_name):#E.g. spell1
    return spells[spell_name]
def calculate_attack_damage(weapon_id):
    return weapon_all[weapon_id]["damage"]
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    global player_in_battle
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            
    elif command[0] == "battle":
        if len(command) > 1:
            execute_battle(command[1])
        else:
            print("Battle who?")
            
    elif command[0] == "equip":
        if len(command) > 1:
            execute_equip(command[1])
        else:
            print("equip what")
            
    elif command[0] == "unequip":
        if len(command) > 1:
            execute_unequip(command[1])
        else:
            print("unequip what")
            
    elif (player_in_battle): #PROCESS ALL COMMANDS AVAIVABLE IN BATTLE
        if(command[0] == "cast"):
            if len(command) > 1:
                return calculate_damage(command[1])
            else:
                print("which spell do you want to cast?")
        
        elif(command[0] == "attack"):
            if len(command) > 1:
                return calculate_attack_damage(command[1])
            else:
                print("which weapon do you want to use for attacking?")
            
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items, room_weapons, player_weapons, room_enemies):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items, room_weapons, player_weapons, room_enemies)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    print_introduction_to_game()
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        if is_winning() == True:
            print ("you win!!!")
            exit()
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory, current_room["weapons"], player_weapons, current_room["enemies"])

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

