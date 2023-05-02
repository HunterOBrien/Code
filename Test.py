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


add_monster()