"""
Final_v2
Final version with added comments
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
    # Welcome screen
    easygui.msgbox("Welcome to Monster Card Catalogue!")
    monster_choices = easygui.buttonbox("Please pick what you want to do with the monster cards", "Main Menu",
                                        choices=("Add Monster", "Change Monster", "Search For Card",
                                                 "Delete Monster", "Print Monsters"))

    # Gives user a choice what function they want to do
    if monster_choices == "Add Monster":
        add_monster()
    elif monster_choices == "Change Monster":
        change_monster_helper()
    elif monster_choices == "Search For Card":
        search_card()
    elif monster_choices == "Delete Monster":
        delete_monster()
    elif monster_choices == "Print Monsters":
        print_monsters()
    else:
        easygui.msgbox("sorry please enter a valid input", "Error")
        main_menu()


def add_monster():
    # Gets monster name from user, adds to dict
    new_monster = easygui.enterbox("Enter the name of the new monster", "Monster Name")
    monster_dict[new_monster] = {}
    monster_stat = 0
    counter = 0

    # Loops through counter 4 times for each different stat, error checking that the value is between 1 and 25
    # additional error checking with try, except loops that the user actually enters a number so program does not crash
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
        easygui.msgbox(f"Monster/s was successfully deleted", "Monster Deleter")
    print(monster_dict)
    main_menu()


def change_monster():
    looper = 0
    # uses index values of this list to work out what stat is being changed
    stats = ["strength", "speed", "stealth", "cunning"]
    stat_values = []

    # Creates list to add options for the monster to select changes in easygui as
    # dictionaries are difficult to work with
    monster_list = []
    for i in monster_dict:
        monster_list.append(i)

    new_name = easygui.enterbox("What is the new name of your monster?", "Monster Name")

    # Loops through counter 4 times for each different stat, error checking that the value is between 1 and 25
    # additional error checking with try, except loops that the user actually enters a number so program does not crash
    while looper != 4:
        try:
            stored_value = easygui.enterbox(f"What is the {stats[looper]} of the monster, (1 to 25)", "Testing 1")
            stored_value = int(stored_value)
            while stored_value > 25 or stored_value < 1:
                easygui.msgbox("Please enter a valid number between 1 and 25")
                stored_value = easygui.enterbox(f"What is the {stats[looper]} of the monster, (1 to 25)", "Testing")
                stored_value = int(stored_value)
            stat_values.append(stored_value)

            looper = looper + 1
        except ValueError:
            easygui.msgbox("Please enter a valid number!")

    monster_dict[new_name] = {"Strength": stat_values[0], "Speed": stat_values[1], "Stealth": stat_values[2],
                              "Cunning": stat_values[3]}
    print(monster_dict)


def change_monster_helper():
    pass_stat = 0
    # Creates list to add options for the monster to select changes in easygui
    monster_list = []
    for i in monster_dict:
        monster_list.append(i)

    # allows user to select monster to change
    monster_to_edit = easygui.choicebox("What monster would you like to edit", "Monster To Edit", monster_list)

    # If user does not select a monster, They are sent to main menu
    if monster_to_edit is None:
        main_menu()

    # Otherwise, the previous monster selected is deleted, new name of monster is asked, as well as new stats
    else:
        del monster_dict[monster_to_edit]
    change_monster()


def search_card():
    # Makes sure the user can find the card regardless of whatever capitalisation they have done
    search = easygui.enterbox("What is the name of the card you are looking for?", "Name of Card⡰").lower().capitalize()

    # Checks if card in dictionary
    if search in monster_dict:
        easygui.msgbox(f"The monster {search} is in the monster's dictionary!", "Search Results")
        easygui.msgbox(f"{search}: {monster_dict[search]}")
        edit_searched_monster = easygui.buttonbox("Would you like to edit its stats", choices=("Yes", "No"))
        # If user wants to edit, deletes old monster and allows user to pick all the stats they want
        if edit_searched_monster == "Yes":
            del monster_dict[search]
            change_monster()
        else:
            pass

    # Else says the card cannot be found
    else:
        easygui.msgbox(f"Sorry, could not find the monster ({search}), that you were looking for", "Search Results")


def print_monsters():
    # empty variable to store information
    monster_info_text = ""
    # loops through monster dictionary
    for monster_ID, monster_info in monster_dict.items():
        # adds monster name to variable, as well as key value with good formatting
        monster_info_text = monster_info_text + f"Monster Name: {monster_ID}\n"
        monster_info_text = monster_info_text + '\n'.join([f"{key}: {value}" for key, value in monster_info.items()])
        monster_info_text = monster_info_text + "\n\n"

    # prints out the variable with all the information stored into an easyGUI.msgbox
    easygui.msgbox(msg=monster_info_text, title="Print Monsters")


# Starts the program by calling the main menu function
main_menu()
