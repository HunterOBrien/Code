"""
Change_Monster_v1
Allows the user to modify an existing monster
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
    monster_list = []
    for i in monster_dict:
        monster_list.append(i)

    monster_to_edit = easygui.choicebox("What monster would you like to edit", "Monster To Edit", monster_list)

    if monster_to_edit is None:
        quit("TEST")

    else:
        del monster_dict[monster_to_edit]
        new_name = easygui.enterbox("What is the new name of the monster?", "Name The Monster")
        strength = easygui.enterbox("What is the strength of the monster, (1 to 25)", "Strength of Monster")
        speed = easygui.enterbox("What is the speed of the monster, (1 to 25)", "Strength of Monster")
        stealth = easygui.enterbox("What is the stealth of the monster, (1 to 25)", "Strength of Monster")
        cunning = easygui.enterbox("What is the cunning of the monster, (1 to 25)", "Strength of Monster")

        monster_dict[new_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}


change_monster()
print(monster_dict)
