"""
Add_Monster_v5
Allows the user to add a new monster card to the existing monster_dict
Changed the add_monster function to loop through one singular stat modifier four times, each time for a different stat
Added try except loops to check for a value error, if so, the counter is decreased by one so the same stat
will be asked for again until valid input
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
    monster_stat = 0
    counter = 0

    while counter < 4:
        if counter == 0:
            try:
                monster_stat = easygui.enterbox("Enter how strong the new monster is, (Max is 25)", "Strength of "
                                                                                                    "Monster")
                monster_stat = int(monster_stat)
                monster_dict["Strength"] = monster_stat
                while monster_stat > 25 or monster_stat < 1:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    monster_stat = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Testing")
                    monster_stat = int(monster_stat)
            except ValueError:
                easygui.msgbox("You did not enter a positive number between 1 and 25")
                counter = counter - 1
        elif counter == 1:
            try:
                monster_stat = easygui.enterbox("Enter how speedy the new monster is, (Max is 25)", "Speed of "
                                                                                                    "Monster")
                monster_stat = int(monster_stat)
                monster_dict["Speed"] = monster_stat
                while monster_stat > 25 or monster_stat < 1:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    monster_stat = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Testing")
                    monster_stat = int(monster_stat)
            except ValueError:
                easygui.msgbox("You did not enter a positive number between 1 and 25")
                counter = counter - 1
        elif counter == 2:
            try:
                monster_stat = easygui.enterbox("Enter how stealthy the new monster is, (Max is 25)", "Stealth of "
                                                                                                      "Monster")
                monster_stat = int(monster_stat)
                monster_dict["Stealth"] = monster_stat
                while monster_stat > 25 or monster_stat < 1:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    monster_stat = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Testing")
                    monster_stat = int(monster_stat)
            except ValueError:
                easygui.msgbox("You did not enter a positive number between 1 and 25")
                counter = counter - 1
        elif counter == 3:
            try:
                monster_stat = easygui.enterbox("Enter how Cunning the new monster is, (Max is 25)", "Cunning of "
                                                                                                     "Monster")
                monster_stat = int(monster_stat)
                monster_dict["Cunning"] = monster_stat
                while monster_stat > 25 or monster_stat < 1:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    monster_stat = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Testing")
                    monster_stat = int(monster_stat)
            except ValueError:
                easygui.msgbox("You did not enter a positive number between 1 and 25")
                counter = counter - 1
        counter = counter + 1


add_monster()
print(monster_dict)
