"""
Change_Monster_v4
Allows the user to modify an existing monster
Sends user back to main menu if no monster is selected
fixes the criteria of stats being between 1 and 25 to work properly
adds additional error checking that the user enters an integer for the monsters stats
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
    pass_stat = 0
    # Creates list to add options for the monster to select changes in easygui
    monster_list = []
    for i in monster_dict:
        monster_list.append(i)

    new_name = easygui.enterbox("What is the new name of your monster?", "Monster Name")
    while pass_stat != 4:

        if pass_stat == 0:
            try:
                strength = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Testing 1")
                strength = int(strength)
                while strength > 25 or strength < 1:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    strength = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Testing")
                    strength = int(strength)
                pass_stat = 1
            except ValueError:
                easygui.msgbox("Please enter a valid number!")

        elif pass_stat == 1:
            try:
                speed = easygui.enterbox("What is the speed of the monster, (1 to 25)", "Testing 2")
                speed = int(speed)
                while speed > 25 or speed < 1:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    speed = easygui.enterbox("What is the speed of the monster, (1 to 25)", "Testing")
                    speed = int(speed)
                pass_stat = 2
            except ValueError:
                easygui.msgbox("Please enter a valid number!")

        elif pass_stat == 2:
            try:
                stealth = easygui.enterbox("What is the stealth of the monster, (1 to 25)", "Testing 2")
                stealth = int(stealth)
                while stealth > 25 or stealth < 1:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    stealth = easygui.enterbox("What is the speed of the monster, (1 to 25)", "Testing")
                    stealth = int(stealth)
                pass_stat = 3
            except ValueError:
                easygui.msgbox("Please enter a valid number!")

        elif pass_stat == 3:
            try:
                cunning = easygui.enterbox("What is the speed of the monster, (1 to 25)", "Testing 2")
                cunning = int(cunning)
                while cunning > 25 or cunning < 1:
                    easygui.msgbox("Please enter a valid number between 1 and 25")
                    cunning = easygui.enterbox("What is the cunning of the monster, (1 to 25)", "Testing")
                    cunning = int(cunning)
                pass_stat = 4
            except ValueError:
                easygui.msgbox("Please enter a valid number!")

    if pass_stat == 4:
        # Adds new monster with stats to the monster dictionary
        monster_dict[new_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}
        print(monster_dict)


def change_monster_helper():
    pass_stat = 0
    # Creates list to add options for the monster to select changes in easygui
    monster_list = []
    for i in monster_dict:
        monster_list.append(i)

    monster_to_edit = easygui.choicebox("What monster would you like to edit", "Monster To Edit", monster_list)

    # If user does not select a monster, They are sent to main menu
    if monster_to_edit is None:
        main_menu()

    # Otherwise, the previous monster selected is deleted, new name of monster is asked, as well as new stats
    else:
        del monster_dict[monster_to_edit]
    change_monster()


change_monster_helper()
