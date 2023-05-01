"""
Main_Menu_v1
Main menu in which the user can select the operations they want to do using easyGUI
"""
import easygui


def main_menu():
    easygui.msgbox("Welcome to Monster Card Catalogue!")
    monster_choices = easygui.buttonbox("Please pick what you want to do with the monster cards", "Main Menu",
                                        choices=("Add Monster", "Change Monster", "Search For Card",
                                                 "Delete Monster", "Print Monsters"))


main_menu()