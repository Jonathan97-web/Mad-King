import os
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def prompt():
    ''' Displays starting message '''
    print("\t\t\tWelcome to the Mad King's Castle\n\n\
        You have to collect two items to defeat the Mad King.\n\n\
        Moves:\t'go {direction}' (travel north, south, east, or west)\n\
        \t'get {item}' (add nearby item to inventory)\n\n")

    input("Press ENTER to continue ...")


def clear():
    ''' Clears screen from messages '''
    os.system('cls' if os.name == 'nt' else 'clear')


def restart_game():
    ''' Restarts the application '''
    python = sys.executable
    os.execl(python, python, * sys.argv)
    if __name__ == "__main__":
        answer = raw_input("Do you want to restart the game?")
    if answer.lower().strip in "y yes".split():
        restart_program()


# Map
rooms = {
    'Clear Grounds': {'North': 'Castle Gardens', 'East': 'Mythical Armoury'},
    'Mythical Armoury': {'West': 'Clear Grounds', 'Item': 'Sword'},
    'Castle Gardens': {'North': 'Castle Gates', 'South': 'Clear Grounds'},
    'Castle Gates': {'East': 'Castle Main Hall', 'South': 'Castle Gardens'},
    'Castle Main Hall': {'South': 'Royal Chambers',
                         'West': 'Castle Gates', 'East': 'Castle Kitchens'},
    'Royal Chambers': {'North': 'Castle Main Hall', 'Madking': 'The Mad King'},
    'Castle Kitchens': {'South': 'Castle Storage', 'West': 'Castle Main Hall'},
    'Castle Storage': {
        'North': 'Castle Kitchens',
        'Item': 'Magical Armour', 'Witch': 'The Kitchen Witch'
    }
    }


# List of directions
directions = "North, South, West or East"

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
    print(
        f"You are in the {current_room}\n"
    )
    print(f"You can go {directions}")
    print(f"To pickup items write 'Get (Item)'")
    print(
        f"Backpack items: {Fore.RED}{inventory}"
        f"\n{'-' * 27}"
    )

    # Display message
    print(msg)

    # Zone messages

    if current_room == "Clear Grounds":
        print(
            "You arrive at Clear Grounds,\n"
            "North of you, you see a castle fitting a King. \n "
            "East of you you see an empty barracks "
            "which looks it could contain something useful."
            )

    if current_room == "Mythical Armoury":
        print(
            "You arrive at the Mythical armoury, \n"
            "East of you is the Clear Grounds \n"
            "In one of the weapon racks you see a Sword hanging there.\n"
            "Will you pick it up?"
        )

    if current_room == "Castle Gardens":
        print(
            "You arrive at Castle Gardens. \n"
            "The garden seems well tended \n"
            "But there are no signs of any groundkeepers.\n"
            "To the South you can see Clear Grounds. \n"
            "To the North you can see the Castle Gates. \n"
        )

    if current_room == "Castle Gates":
        print(
            "You arrive at the Castle Gates \n"
            "You see no sign of life in this area either \n"
            "You start to wonder if it's a good idea to enter the castle. \n"
            "You feel pulled towards the castle \n"
            "To the East you can see the Castle Main Hall \n"
            "To the South you can see the Castle Gardens"
        )

    if current_room == "Castle Main Hall":
        print(
            "You arrive at the Castle Main Hall \n"
            "You see a big table in the center of the room \n"
            "The table is dined as if someone had dinner here recently \n"
            "Will you venture further? \n"
            "To the East you can see a door what seems to be "
            "the Castle Kitchens \n"
            "To the South you can see a huge door to the Royal Chambers"
        )

    if current_room == "Royal Chambers":
        print(
            "You arrive at the Royal Chambers. \n"
            "In the room you can see what looks \n"
            "like to be the king of the castle. \n"
            "You try to converse with the king \n"
            "But the king is obviously mad and doesn't listen \n"
            "He screams traitor and goes on the offense."
        )
        input('Press ENTER to attack')
        clear()

    if current_room == "Castle Kitchens":
        print(
            "You arrive at the Castle Kitchens. \n"
            "You can see a pot and food that has been prepared. \n"
            "You can feel a foul stench coming towards the South. \n"
            "To the West you see a door that leads "
            "you to the Castle Main Hall \n"
            "To the South you can see a door that seems "
            "to be the Castle Storage"
        )

    if current_room == "Castle Storage":
        print(
            "You arrive at the Castle Storage \n"
            "You see a figure in front of you. \n"
            "The figure approaches you \n"
            "It's a witch! She takes a swing at you \n"
        )
        input('Press ENTER to attack')
        clear()

    # Item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:

            # Plural
            if nearby_item[-1] == 's':
                print(
                    f"You see {Fore.RED}{nearby_item}"
                    )

            # Singular item starts with vowel
            elif nearby_item[0] in vowels:
                print(f"You see an {Fore.RED}{nearby_item}")
            # Singular item starts with consanant
            else:
                print(f"You see a {Fore.RED}{nearby_item}")

    # Mad King encounter
    if "Madking" in rooms[current_room].keys():

        # Lose
        if len(inventory) < 2:
            print(
                "You lost a fight against \n"
                f"{Fore.BLUE}{rooms[current_room]['Madking']}. \n"
                "Your adventure ends here and no one will remember you."
            )

            input("Press ENTER to reset the game...")
            restart_game()

        # Win
        else:
            print(
                f"You beat {Fore.BLUE}{rooms[current_room]['Madking']}! \n"
                "As you killed the Mad King the castle disappeared. \n"
                "You're standing in the middle of nowhere. \n"
                "Perhaps it's you who should question your sanity? \n"
                "Congratulations on beating the game! \n"
                "if you would like to play again press ENTER"
            )

            input("Press ENTER to restart the game...")
            restart_game()

            # Witch encounter
    if "Witch" in rooms[current_room].keys():

        # Lose
        if len(inventory) < 1:
            print(
                "You lost a fight with "
                f"{Fore.BLUE}{rooms[current_room]['Witch']}. \n"
                "Your adventure ends here and no one will remember you."
                "Perhaps you forgot an item along the way? \n"
            )

            input("Press ENTER to restart the game...")
            restart_game()

        # Win
        else:
            print(
                f"You beat {Fore.BLUE}{rooms[current_room]['Witch']}!\n"
                "Since you picked up the Sword you were able to block \n"
                "the witches attack and counter-attack. \n"
                "As you killed the witch she disappeared, \n"
                "as she was never there in the first place. \n"
                "You need to find the Mad King and end his terror!"
            )


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

        except Exception:
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
        except Exception:
            msg = f"Can't find {item}."

        # Any other commands invalid
    else:
        msg = "Invalid Command"
