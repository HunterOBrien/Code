"""
Add_Monster_v3
Allows the user to add a new monster card to the existing monster_dict
Uses while loops to test if the values for strength, speed, etc. are within the allowed values
Added try except loops to check for a value error, if so, the while loop is run again
"""

import easygui

# Nested dictionary containing all the existing monster cards
monster_dict = {
    'Stoneling': {
        'Strength': 7,
        'Speed': 1,
        'Stealth': 25,
        'Cunning': 15
    },
    'Vexscream': {
        'Strength': 1,
        'Speed': 6,
        'Stealth': 21,
        'Cunning': 19

    },
    'Dawnmirage': {
        'Strength': 5,
        'Speed': 15,
        'Stealth': 18,
        'Cunning': 22
    },
    'Blazegolem': {
        'Strength': 15,
        'Speed': 20,
        'Stealth': 23,
        'Cunning': 6
    },
    'Websnake': {
        'Strength': 7,
        'Speed': 15,
        'Stealth': 10,
        'Cunning': 5
    },
    'Moldvine': {
        'Strength': 21,
        'Speed': 18,
        'Stealth': 14,
        'Cunning': 5
    },
    'Vortexwing': {
        'Strength': 19,
        'Speed': 13,
        'Stealth': 19,
        'Cunning': 2
    },
    'Rotthing': {
        'Strength': 16,
        'Speed': 7,
        'Stealth': 4,
        'Cunning': 12
    },
    'Froststep': {
        'Strength': 14,
        'Speed': 14,
        'Stealth': 17,
        'Cunning': 4
    },
    'Wispghoul': {
        'Strength': 17,
        'Speed': 19,
        'Stealth': 3,
        'Cunning': 2
    },
}


def add_monster():
    # Gets monster name from user, adds to dict
    new_monster = easygui.enterbox("Enter the name of the new monster", "Monster Name")
    monster_dict[new_monster] = {}
    monster_strength = 0
    monster_speed = 0
    monster_stealth = 0
    monster_cunning = 0

    # Adds Strength value to monster
    # Runs while loop until a number between 1 and 25 is entered
    while (monster_strength > 25) or (monster_strength < 1):
        try:
            monster_strength = easygui.enterbox("Enter how strong the new monster is, (Max is 25)", "Strength of "
                                                                                                    "Monster")
            monster_strength = int(monster_strength)
        except ValueError:
            easygui.msgbox("You did not enter a positive number between 1 and 25")
            monster_strength = 0
        monster_dict["Strength"] = monster_strength

    # Adds Speed value to monster
    # Runs while loop until a number between 1 and 25 is entered
    while (monster_speed > 25) or (monster_speed < 1):
        try:
            monster_speed = easygui.enterbox("Enter how Speedy the new monster is, (Max is 25)", "Speed of "
                                                                                                 "Monster")
            monster_speed = int(monster_speed)
        except ValueError:
            easygui.msgbox("You did not enter a positive number between 1 and 25")
            monster_speed = 0
        monster_dict["Speed"] = monster_speed

    # Adds Strength value to monster
    # Runs while loop until a number between 1 and 25 is entered
    while (monster_stealth > 25) or (monster_stealth < 1):
        try:
            monster_stealth = easygui.enterbox("Enter how Stealthy the new monster is, (Max is 25)", "Stealth of "
                                                                                                     "Monster")
            monster_stealth = int(monster_stealth)
        except ValueError:
            easygui.msgbox("You did not enter a positive number between 1 and 25")
            monster_stealth = 0
        monster_dict["Stealth"] = monster_stealth

    # Adds Cunning value to monster
    # Runs while loop until a number between 1 and 25 is entered
    while (monster_cunning > 25) or (monster_cunning < 1):
        try:
            monster_cunning = easygui.enterbox("Enter how cunning the new monster is, (Max is 25)", "Cunning of "
                                                                                                    "Monster")
            monster_cunning = int(monster_cunning)
        except ValueError:
            easygui.msgbox("You did not enter a positive number between 1 and 25")
            monster_cunning = 0
        monster_dict["Cunning"] = monster_cunning


add_monster()
print(monster_dict)
