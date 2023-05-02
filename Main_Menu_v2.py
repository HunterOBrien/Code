"""
Main_Menu_v2
Main menu in which the user can select the operations they want to do using easyGUI
added if and elif statements ready to call a function whe that choice is made
"""
import easygui


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


main_menu()