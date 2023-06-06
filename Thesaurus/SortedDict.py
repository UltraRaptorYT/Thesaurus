"""
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
"""

class SortedDict(dict):
    # overload the iteration function to create an object that can access each element each time the __next__ function is run
    def __iter__(self):
        # iterate through the dictionary and sorting the dictionary according to the key
        return iter(sorted(super(SortedDict, self).__iter__()))

    def items(self):
        return iter((k, self[k]) for k in self)

    def keys(self):
        return list(self)

    def values(self):
        return [self[k] for k in self]
    