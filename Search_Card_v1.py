"""
Search_Card_v1
allows user to search to see if a card exists
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


def search_card():
    search = easygui.enterbox("What is the name of the card you are looking for?", "Name of Card").lower().capitalize()
    if search in monster_dict:
        easygui.msgbox(f"The monster {search} is in the monster's dictionary!", "Search Results")
    else:
        easygui.msgbox(f"Sorry, could not find the monster ({search}), that you were looking for", "Search Results")


search_card()