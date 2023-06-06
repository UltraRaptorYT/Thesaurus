"""
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
"""


class Menu:
    """
    Menu class takes in 3 parameters:
    1. prompt: The question to be asked to the user
    2. order: Boolean value to determine whether the menu should be ordered or not
    3. options: Array of possible input values for question
    4. callback: The function to be called when the user enters a valid input

    Functions Available:
    1. insert(items): Inserts items into the menu
    2. show(): Prints out the menu
    3. showBanner(): Prints out the banner
    """

    def __init__(self, prompt, order, options=None):
        self.prompt = prompt
        self.order = order
        self.items = []
        self.length = 0
        self.options = options
        return

    def insert(self, items: list):
        for item in items:
            self.length += 1
            self.items.append(item)

    def show(self):
        print(f"\n{self.prompt}")
        if self.order:
            for i in range(self.length):
                print(f"\t{i+1}. {self.items[i]}")
        else:
            for item in self.items:
                print(f"\t- {item}")
        return ""
    
    def showBanner(self):
        print("")
        print("*" * 60)
        print("*" + f"{' ST1507 DSAA: Welcome to:':<58}" + "*")
        print("*" + f"{' ':<58}" + "*")
        print(
            "*" + f"{'  ~ Thesaurus Based Text Processing Application ~':<58}" + "*")
        print("*" + f"{'':-<58}" + "*")
        print("*" + f"{' ':<58}" + "*")
        print("*" + f"{' - Done by: Soh Hong Yu (2100775)':<58}" + "*")
        print("*" + f"{' - Class DAAA/2B/01':<58}" + "*")
        print("*" * 60)
        print("\n" * 1)
        return
