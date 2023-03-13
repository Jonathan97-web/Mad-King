import os


# Displays starting message
def prompt():
    print("\t\t\tWelcome to the Mad King's Castle\n\n\
        You have to collect two items to defeat the Mad King.\n\n\
        Moves:\t'go {direction}' (travel north, south, east, or west)\n\
        \t'get {item}' (add nearby item to inventory)\n\n")

    input("Press ENTER to continue ...")


# Clears screen from messages
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
rooms = {
    'Clear Grounds': {'North': 'Castle Gardens', 'East': 'Mythical Armoury'},
    'Mythical Armoury': {'West': 'Clear Grounds', 'Item': 'Sword'},
    'Castle Gardens': {'North': 'Castle Gates', 'South': 'Clear Grounds'},
    'Castle Gates': {'East': 'Castle Main Hall', 'South': 'Castle Gardens'},
    'Castle Main Hall': {'South': 'Royal Chambers',
                         'West': 'Castle Gates', 'East': 'Castle Kitchens'},
    'Royal Chambers': {'North': 'Castle Main Hall', 'Madking': 'Mad King'},
    'Castle Kitchens': {'South': 'Castle Storage', 'West': 'Castle Main Hall'},
    'Castle Storage': {'North': 'Castle Kitchens', 'Item': 'Magical Armour', 'Witch': 'Kitchen Witch'}
    }

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
current_room = "Clear Grounds"

# Result of last move
msg = ""

clear()
prompt()

# Gameplay loop
while True:

    clear()

    # Display information to player
    print(f"You are in the {current_room}\n Backpack items: {inventory}\n{'-' * 27}")

    # Display message
    print(msg)

    # Item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:

            # Plural
            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")

            # Singular starts with vowel
            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")
            # Singular starts with consanant
            else:
                print(f"You see a {nearby_item}")

    # Mad King encounter
    if "Madking" in rooms[current_room].keys():

        # Lose
        if len(inventory) < 2:
            print(f"You lost a fight with {rooms[current_room]['Madking']}. Your adventure ends here and no one will remember you.")
            break

        # Win
        else:
            print(f"You beat {rooms[current_room]['Madking']}! Tales will be told about your adventure.")
            break

            # Witch encounter
    if "Witch" in rooms[current_room].keys():

        # Lose
        if len(inventory) < 1:
            print(f"You lost a fight with {rooms[current_room]['Witch']}. Your adventure ends here and no one will remember you.")
            break

        # Win
        else:
            print(f"You beat {rooms[current_room]['Witch']}! You need to find the Mad King and end his terror!")


    # Accept player's move as input
    user_input = input('Enter your move: \n')

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ' '.join(item).title()

    # Moving moving between rooms
    if action == 'Go':

        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel to {direction}."

        except:
            msg = f"You can't go that way."

    # Picking up items
    elif action == 'Get':
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[current_room]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}."

            else:
                msg = f"Can't find {item}."
        except:
            msg = f"Can't find {item}."

        # Any other commands invalid
    else:
        msg = "Invalid Command"
