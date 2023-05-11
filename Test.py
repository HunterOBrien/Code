"""
Program to change and temporarily test if components work
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


def change_monster():
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
        new_name = easygui.enterbox("What is the new name of the monster?", "Name of Monster")

        strength = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Strength of Monster")
        while strength > 25 or strength < 1:
            easygui.msgbox("Please enter a valid number between 1 and 25")
            strength = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Strength of Monster")

        speed = easygui.enterbox("What is the speed of the monster, (1 to 25)", "Speed of Monster")
        while speed > 25 or speed < 1:
            easygui.msgbox("Please enter a valid number between 1 and 25")
            speed = easygui.enterbox("What is the speed of the monster, (1 to 25)", "Speed of Monster")

        stealth = easygui.enterbox("What is the stealth of the monster, (1 to 25)", "Stealth of Monster")
        while stealth > 25 or speed < 1:
            easygui.msgbox("Please enter a valid number between 1 and 25")
            stealth = easygui.enterbox("What is the stealth of the monster, (1 to 25)", "Stealth of Monster")

        cunning = easygui.enterbox("What is the cunning of the monster, (1 to 25)", "Cunning of Monster")
        while cunning > 25 or cunning < 1:
            easygui.msgbox("Please enter a valid number between 1 and 25")
            stealth = easygui.enterbox("What is the cunning of the monster, (1 to 25)", "Cunning of Monster")

        # Adds new monster with stats to the monster dictionary
        monster_dict[new_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}


def delete_monster():
    monster_list = []
    for i in monster_dict:
        monster_list.append(i)
    delete_option = easygui.multchoicebox("What monster would you like to delete", "Delete Monster",
                                          choices=monster_list + ["Back to main menu"])

    if "Back to main menu" in delete_option:
        main_menu()
    else:
        for monster_to_delete in delete_option:
            del monster_dict[monster_to_delete]
        easygui.msgbox(f"Monster {monster_to_delete} was successfully deleted", "Monster Deleter")

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
            except ValueError:
                easygui.msgbox("You did not enter a positive number between 1 and 25")
                counter = counter - 1
        elif counter == 1:
            try:
                monster_stat = easygui.enterbox("Enter how speedy the new monster is, (Max is 25)", "Speed of "
                                                                                                    "Monster")
                monster_stat = int(monster_stat)
                monster_dict["Speed"] = monster_stat
            except ValueError:
                easygui.msgbox("You did not enter a positive number between 1 and 25")
                counter = counter - 1
        elif counter == 2:
            try:
                monster_stat = easygui.enterbox("Enter how stealthy the new monster is, (Max is 25)", "Stealth of "
                                                                                                      "Monster")
                monster_stat = int(monster_stat)
                monster_dict["Stealth"] = monster_stat
            except ValueError:
                easygui.msgbox("You did not enter a positive number between 1 and 25")
                counter = counter - 1
        elif counter == 3:
            try:
                monster_stat = easygui.enterbox("Enter how Cunning the new monster is, (Max is 25)", "Cunning of "
                                                                                                     "Monster")
                monster_stat = int(monster_stat)
                monster_dict["Cunning"] = monster_stat
            except ValueError:
                easygui.msgbox("You did not enter a positive number between 1 and 25")
                counter = counter - 1
        counter = counter + 1


def main_menu():
    easygui.msgbox("Welcome to Monster Card Catalogue!")
    monster_choices = easygui.buttonbox("Please pick what you want to do with the monster cards", "Main Menu",
                                        choices=("Add Monster", "Change Monster", "Search For Card",
                                                 "Delete Monster", "Print Monsters"))

    if monster_choices == "Add Monster":
        add_monster()
    elif monster_choices == "Change Monster":
        pass
    elif monster_choices == "Search For Card":
        pass
    elif monster_choices == "Delete Monster":
        delete_monster()
    elif monster_choices == "Print Monsters":
        print(monster_dict)
    else:
        easygui.msgbox("sorry please enter a valid input", "Error")
        main_menu()


main_menu()
