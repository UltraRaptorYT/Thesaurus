"""
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
"""
from SortedList.Node import Node

# Use the Node parent class as a inherited class.
class Word(Node):
    def __init__(self, name):
        self.name = name.lower().strip() # Make keyword lowercased and remove any random spaces
        super().__init__()

    # get the length of the keyword
    def size(self):
        return len(self.name)

    # check if keyword are the same
    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.name == otherNode.name

    # check if keyword is less than other keyword
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'<' not supported between instances of 'Word' and 'NoneType'")
        return self.name < otherNode.name

    # overloading the __str__ function to change how the Word is printed
    def __str__(self):
        s = f'{self.name}'
        return s
