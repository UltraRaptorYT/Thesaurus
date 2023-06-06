"""
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
"""

import re

from SortedList.SortedList import SortedList
from SortedList.Word import Word
from Thesaurus.SortedDict import SortedDict

""""
Creates an instance of Thesaurus
"""
class Thesaurus():
    def __init__(self):
        self.thesaurus = SortedDict()
        self.filePath = None
        return

    # Check if keyword exist in the Thesaurus Dictionary
    def checkDup(self, keyword):
        return keyword in self.thesaurus.keys()

    # Add function that add new keyword
    def addKey(self):
        keyword = False
        while not keyword:
            keyword = input("\nEnter keyword (Enter 0 to return): ")
            keyword = keyword.strip().lower()
            if keyword == "0":
                keyword = True
                return
            elif any(char.isdigit() for char in keyword):
                print("Please enter keyword without numbers!")
                keyword = False
                continue
            elif any(char == " " for char in keyword):
                print("Please enter keyword without space!")
                keyword = False
                continue
            elif self.checkDup(keyword):
                print(f"Keyword \"{keyword}\" is already exist in thesaurus!")
                keyword = False
                continue
            elif keyword == "":
                print("Please enter a keyword!")
                continue
            elif not keyword.isalpha():
                print("Please enter keyword without special characters!")
                keyword = False
                continue
            synonyms, validKeyword = self.addSynonym(keyword, SortedList())
            if str(synonyms) != "":
                self.thesaurus[keyword] = synonyms
            if not validKeyword:
                continueValid = False
                while not continueValid:
                    shouldContinue = input(
                        "\nDo you want to add more keywords? y/n: ").lower()
                    if shouldContinue == "y":
                        continueValid = True
                        keyword = False
                    elif shouldContinue == "n":
                        continueValid = True
                        keyword = True
                    else:
                        print("\nInvalid input. Please enter only \"y\" or \"n\"")
        return self.thesaurus

    # Create function that adds new Synonym
    def addSynonym(self, keyword, sortedList):
        print(
            f"\nYou may enter one or more synonyms for \"{keyword}\"\n(please press \"Enter\" once done.)")
        synonym = True
        while synonym:
            synonym = input(f"Enter synonym for \"{keyword}\": ")
            synonym = synonym.strip().lower()
            if synonym == keyword:
                print("Invalid Input! Do not enter keyword again!\n")
            elif synonym == "":
                continueValid = False
                while not continueValid:
                    shouldContinue = input(
                        "\nDo you want to add more synonyms? y/n: ")
                    shouldContinue = shouldContinue.lower()
                    if shouldContinue == "y":
                        continueValid = True
                        synonym = True
                    elif shouldContinue == "n":
                        continueValid = True
                        synonym = False
                        return sortedList, synonym
                    else:
                        print("\nInvalid input. Please enter only \"y\" or \"n\"")
            elif any(char.isdigit() for char in synonym):
                print("Please enter synonym without numbers!\n")
            elif any(char == " " for char in synonym):
                print("Please enter synonym without space!\n")
            elif sortedList.checkExist(Word(synonym)):
                print("Synonym already exist! Please Try Again!\n")
            elif not synonym.isalpha():
                print("Please enter synonym without special characters!\n")
            else:
                sortedList.insert(Word(synonym))
        return sortedList, synonym

    # Create function to open file
    def openFile(self, inputFile: str):
        fileName = inputFile.split("\\")[-1]
        self.filePath = inputFile
        self.thesaurus.clear()
        with open(inputFile, 'r', encoding="utf8") as f:
            data = f.read().strip()
            if data == "":
                f.close()
                print(f"\"{fileName}\" is empty...\n")
                return False
            for row in data.split("\n"):
                if ":" not in row:
                    f.close()
                    print(
                        f"\"{fileName}\" does not follow Thesaurus format...\n")
                    return False
                keyword, synonyms = row.split(":")
                sortedList = SortedList()
                if synonyms.split(",")[0] == "":
                    f.close()
                    print(
                        f"\"{fileName}\" does not follow Thesaurus format...\n")
                    return False
                for synonym in synonyms.split(","):
                    sortedList.insert(Word(synonym))
                self.thesaurus[keyword] = sortedList
            f.close()
        print(f"""
Thesaurus \"{fileName}\" has been loaded and is printed here...""")
        return self.thesaurus

    # Overload the __str__ to print the thesaurus
    def __str__(self):
        s = ""
        for keyword, synonyms in self.thesaurus.items():
            s += f"""{keyword}: {synonyms}\n"""
        return s

    # Check if filePath exist so that we can save thesaurus
    def save(self):
        if self.filePath is None:
            print("No file detected to save in! Please use \"Save As\" function instead.")
            return False
        try:
            open(self.filePath, 'r', encoding="utf8")
        except FileNotFoundError:
            print(
                f"{self.filePath} is missing! Please use \"Save As\" function instead.")
            return False
        return self.saveAs(self.filePath) # Reuse saveAs function to save the thesaurus

    # saveAs Function to save the thesaurus
    def saveAs(self, filePath):
        fileName = filePath.split("\\")[-1]
        self.filePath = filePath
        with open(self.filePath, 'w', encoding="utf8") as f:
            s = ""
            for keyword, synonyms in self.thesaurus.items():
                s += f"""{keyword}:{",".join(str(synonyms).split(", "))}\n"""
            f.write(s)
            f.close()
        print(f"""Your file \"{fileName}\" has been saved\n""")
        return True

    # run the Sort Function to sort the thesaurus
    def sort(self, sortType):
        print(f"\nSorting Synonyms: {sortType}")
        for keyword, synonymList in self.thesaurus.items():
            self.thesaurus[keyword] = synonymList.sort(sortType)
        return self.thesaurus

    # Check what the process type is and use REGEX and keyword split to process the text
    def processText(self, text, processType):
        print(f"\nProcessing text for: {processType}")
        if processType == "Simplified Writing":
            for keyword, synonymList in self.thesaurus.items():
                for index in range(synonymList.getSize()):
                    text = re.sub(r"\b{}\b".format(
                        str(synonymList.getIndex(index))), keyword, text, flags=re.IGNORECASE)
        else:
            for keyword, synonymList in self.thesaurus.items():
                textArr = re.split(r"\b{}\b".format(keyword),text)
                for index in range(len(textArr) - 1):
                    textArr[index] += str(synonymList.getIndex(index %
                                          synonymList.length))
                text = "".join(textArr)
        return text
