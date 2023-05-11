"""
Change_Monster_v1
Allows the user to modify an existing monster
Sends user back to main menu if no monster is selected
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


def main_menu():
    easygui.msgbox("Welcome to Monster Card Catalogue!")
    monster_choices = easygui.buttonbox("Please pick what you want to do with the monster cards", "Main Menu",
                                        choices=("Add Monster", "Change Monster", "Search For Card",
                                                 "Delete Monster", "Print Monsters"))

    if monster_choices == "Add Monster":
        pass
    elif monster_choices == "Change Monster":
        pass
    elif monster_choices == "Search For Card":
        pass
    elif monster_choices == "Delete Monster":
        pass
    elif monster_choices == "Print Monsters":
        pass


def change_monster():
    # Creates list to add options for the monster to select changes in easygui
    monster_list = []
    for i in monster_dict:
        monster_list.append(i)
    monster_to_edit = easygui.choicebox("What monster would you like to edit", "Monster To Edit", monster_list)
    counter = 0

    # If user does not select a monster, They are sent to main menu
    if monster_to_edit is None:
        main_menu()

    # Otherwise, the previous monster selected is deleted, new name of monster is asked, as well as new stats
    else:
        del monster_dict[monster_to_edit]
        new_name = easygui.enterbox("What is the new name of the monster?", "Name of Monster")

        while counter < 4:
            if counter == 0:
                try:
                    strength = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Strength of Monster")
                except ValueError:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    counter = counter - 1

            elif counter == 1:
                try:
                    speed = easygui.enterbox("What is the speed of the monster, (1 to 25)", "Speed of Monster")
                except ValueError:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    counter = counter - 1

            elif counter == 2:
                try:
                    stealth = easygui.enterbox("What is the stealth of the monster, (1 to 25)", "Stealth of Monster")
                except ValueError:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    counter = counter - 1

            elif counter == 3:
                try:
                    cunning = easygui.enterbox("What is the cunning of the monster, (1 to 25)", "Cunning of Monster")
                except ValueError:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    counter = counter - 1

            counter = counter + 1
        # Adds new monster with stats to the monster dictionary
        monster_dict[new_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}


change_monster()
print(monster_dict)
