"""
Delete_Monster_v1
deletes a monster selected by the user and using msgbox to say what has been deleted
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


def delete_monster():
    monster_list = list(monster_dict.keys())
    delete_option = easygui.multchoicebox("What monster would you like to delete", "Monster Deleter",
                                          choices=["Back to main menu"] + monster_list)
    # Deletes monster selected by user
    monster_to_delete = delete_option[0]
    del monster_dict[monster_to_delete]
    easygui.msgbox(f"the monster {monster_to_delete} was deleted")


delete_monster()

