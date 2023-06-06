"""
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
"""
# Writing program

import os
from Thesaurus.Thesaurus import Thesaurus
from SortedList.SortedList import SortedList
from SortedList.Word import Word
from Menu.Menu import Menu
from Online.Online import getSimilarWords


# main program

def main():
    """
    Use the Menu class to create a menu object
    """
    mainMenu = Menu(
        f"Please select your choice: ({','.join([str(x+1) for x in range(10)])})", True)
    mainMenu.showBanner()
    mainMenu.insert(["New",
                     "Open",
                     "Sort",
                     "Process Text",
                     "Additional Functions",
                     "Spell Checker",
                     "Print",
                     "Save",
                     "Save As",
                     "Exit", ])
    os.system("pause") # Get "Press any key to continue"
    exitApp = False
    while not exitApp:
        choice = False
        while not choice:
            mainMenu.show() # Show main menu
            choice = input("Enter choice: ")
            # Main menu validation
            if choice == '1':
                thesaurus = Thesaurus() # Create a new thesaurus object
                print("""
We will be starting a new Thesaurus.
You may now enter a series of keywords and their synonyms.""")
                thesaurus.addKey() # Add synonym
                if str(thesaurus): # Check if thesaurus exist
                    print(f"""
Your new Thesaurus is ready and printed here....
{thesaurus}
""")
                else:
                    print(f"\nYour new Thesaurus is empty...\n")
                os.system("pause") # Get "Press any key to continue"
            elif choice == '2':
                thesaurus = Thesaurus() # Create a new thesaurus object
                print("""
We will be opening an existing Thesaurus.""")
                validFile = False
                while not validFile:
                    # Input file validation
                    inputFile = input(
                        "Please enter input file (Enter 0 to return): ")
                    if inputFile == "0":
                        validFile = True
                        continue
                    elif ".txt" != inputFile[-4:]:
                        print("Invalid File Type! Please try again!\n")
                        validFile = False
                        continue
                    if ":\\" not in inputFile:
                        inputFile = os.path.abspath(
                            os.getcwd()) + "\\" + inputFile
                    try:
                        open(inputFile, 'r', encoding="utf8")
                    except FileNotFoundError:
                        print("File does not exist! Please try again!\n")
                        validFile = False
                        continue
                    validFile = True
                if inputFile != "0":
                    if thesaurus.openFile(inputFile):
                        print(thesaurus)
                else:
                    print(f"\nYour new Thesaurus is empty...\n")
                os.system("pause") # Get "Press any key to continue"
            elif choice == '3':
                # Check if thesaurus exist
                try:
                    if not str(thesaurus):
                        print(
                            f"\nYour Thesaurus is empty...\nPlease create/open a thesaurus.\n")
                        continue
                except UnboundLocalError:
                    print(f"\nNo Thesaurus found! Please create/open a thesaurus.")
                    continue
                # Sorting Menu
                sortMenu = Menu(
                    f"Please select your choice: ({','.join([str(x+1) for x in range(5)])})", True)
                sortOptions = ["Alphabetically (Default)",
                               "Length/Alphabetically",
                               "Length/Random Alphabetically",
                               "Randomly",
                               "Back to Main Menu", ]
                sortMenu.insert(sortOptions)
                sortValid = False
                # Sorting validation
                while not sortValid:
                    sortMenu.show()
                    sortChoice = input("Enter choice: ")
                    if sortChoice == "5":
                        sortValid = True
                        continue
                    elif sortChoice.isnumeric() and sortChoice not in ["1", "2", "3", "4"]:
                        print(
                            "\nOnly options between 1 to 5 are available. Please try again!")
                        sortValid = False
                        continue
                    elif sortChoice not in ["1", "2", "3", "4"]:
                        print("\nYou must enter a number. Please try again!")
                        sortValid = False
                        continue
                    sortValid = False
                    thesaurus.sort(sortOptions[int(sortChoice) - 1]) # use sort class to sort
                    print(f"{thesaurus}\n")
                    os.system("pause") # Get "Press any key to continue"
            elif choice == '4':
                # Check if thesaurus exist
                try:
                    if not str(thesaurus):
                        print(
                            f"\nYour Thesaurus is empty...\nPlease create/open a thesaurus.\n")
                        continue
                except UnboundLocalError:
                    print(f"\nNo Thesaurus found! Please create/open a thesaurus.")
                    continue
                # File validation
                validFile = False
                while not validFile:
                    print("\nSelect the file you want to process")
                    inputFile = input(
                        "Please enter input file (Enter 0 to return): ")
                    if inputFile == "0":
                        validFile = True
                        continue
                    elif ".txt" != inputFile[-4:]:
                        print("Invalid File Type! Please try again!")
                        validFile = False
                        continue
                    if ":\\" not in inputFile:
                        inputFile = os.path.abspath(
                            os.getcwd()) + "\\" + inputFile
                    try:
                        open(inputFile, 'r', encoding="utf8")
                    except FileNotFoundError:
                        print("File does not exist! Please try again!")
                        validFile = False
                        continue
                    validFile = True
                if inputFile == "0":
                    os.system("pause") # Get "Press any key to continue"
                    break
                text = open(inputFile, 'r', encoding="utf8").read()
                print("\nThe text before processing")
                print(f"{text}\n")
                os.system("pause") # Get "Press any key to continue"
                print("\nNext choose a Text Processing option.")
                processMenu = Menu(
                    f"Please select your choice: ({','.join([str(x+1) for x in range(3)])})", True)
                processOptions = ["Simplified Writing",
                                  "Elegant Writing", "Back to Main Menu"]
                processMenu.insert(processOptions)
                processValid = False
                while not processValid:
                    processMenu.show()
                    processChoice = input("Enter choice: ")
                    # Choice validation
                    if processChoice == "3":
                        processValid = True
                        continue
                    elif processChoice.isnumeric() and processChoice not in ["1", "2"]:
                        print(
                            "\nOnly options between 1 to 3 are available. Please try again!")
                        processValid = False
                        continue
                    elif processChoice not in ["1", "2"]:
                        print("\nYou must enter a number. Please try again!")
                        processValid = False
                        continue
                    processValid = False
                    newText = thesaurus.processText(
                        text, processOptions[int(processChoice) - 1])
                    print("\nThe text after processing:")
                    print(newText + "\n")
                    os.system("pause") # Get "Press any key to continue"
                    continueValid = False
                    # y/n validation
                    while not continueValid:
                        shouldContinue = input(
                            "\nDo you want to save the text to a file? y/n: ")
                        shouldContinue = shouldContinue.lower()
                        if shouldContinue == "y":
                            continueValid = True
                            validFile = False
                            # File path validation
                            while not validFile:
                                filePath = input(
                                    "Please enter new filename (Enter 0 to return): ")
                                if filePath == "0":
                                    validFile = True
                                    continue
                                elif ".txt" != filePath[-4:]:
                                    print(
                                        "Invalid File Type! Please try again!\n")
                                    validFile = False
                                    continue
                                if ":\\" not in filePath:
                                    filePath = os.path.abspath(
                                        os.getcwd()) + "\\" + filePath
                                validFile = True
                            if filePath == "0":
                                continueValid = False
                                continue
                            fileExist = os.path.isfile(
                                filePath) and os.path.exists(filePath)
                            saveFile = True
                            fileName = filePath.split("\\")[-1]
                            # Check if file exists
                            if fileExist:
                                fileValid = False
                                while not fileValid:
                                    shouldContinue = input(
                                        f"Do you want to overwrite {fileName}'s content? y/n: ")
                                    shouldContinue = shouldContinue.lower()
                                    if shouldContinue == "n":
                                        fileValid = True
                                        validFile = False
                                        saveFile = False
                                        continue
                                    elif shouldContinue != "y":
                                        fileValid = False
                                        print(
                                            "\nInvalid input. Please enter only \"y\" or \"n\"")
                                        continue
                                    fileValid = True
                            # Write and replace file
                            if saveFile:
                                with open(filePath, "w", encoding="utf8") as f:
                                    f.write(newText)
                                    f.close()
                                    print(
                                        f"The text has been saved in \"{fileName}\"")
                        elif shouldContinue == "n":
                            continueValid = True
                            continue
                        else:
                            print(
                                "\nInvalid input. Please enter only \"y\" or \"n\"")
                    print("\n")
                    os.system("pause") # Get "Press any key to continue"
            elif choice == '5':
                # Advance Menu
                advanceMenu = Menu(
                    f"Please select your choice: ({','.join([str(x+1) for x in range(8)])})", True)
                advanceList = ["Add NEW keyword(s)", "Add NEW synonym(s)", "Edit keyword(s)", "Edit synonym(s)",
                               "Delete keyword(s)", "Delete synonym(s)", "Delete Thesaurus", "Back to Main Menu"]
                advanceMenu.insert(advanceList)
                advanceValid = False
                while not advanceValid:
                    advanceMenu.show()
                    advanceChoice = input("Enter choice: ")
                    # input validation
                    if advanceChoice == "8":
                        advanceValid = True
                        continue
                    elif advanceChoice.isnumeric() and advanceChoice not in ["1", "2", "3", "4", "5", "6", "7"]:
                        print(
                            "\nOnly options between 1 to 8 are available. Please try again!")
                        advanceValid = False
                        continue
                    elif advanceChoice not in ["1", "2", "3", "4", "5", "6", "7"]:
                        print("\nYou must enter a number. Please try again!")
                        advanceValid = False
                        continue
                    advanceValid = True
                    # Check if thesaurus exist
                    try:
                        if not str(thesaurus):
                            print(
                                f"\nYour Thesaurus is empty...\nPlease create/open a thesaurus.\n")
                            continue
                    except UnboundLocalError:
                        print(
                            f"\nNo Thesaurus found! Please create/open a thesaurus.")
                        continue
                    # Add keywords
                    if advanceChoice == "1":
                        thesaurus.addKey()
                        if str(thesaurus):
                            print(
                                f"""\nYour edited Thesaurus is ready and printed here....\n{thesaurus}\n""")
                        else:
                            print(f"\nYour new Thesaurus is empty...\n")
                    # Add synonyms
                    elif advanceChoice == "2":
                        print(
                            f"""\nPrinting existing Thesaurus....\n{thesaurus}""")
                        keyword = False
                        while not keyword:
                            keyword = input(
                                "\nEnter keyword to add synonyms (Enter 0 to return): ")
                            keyword = keyword.strip().lower()
                            if keyword == "0":
                                keyword = True
                                continue
                            elif any(char.isdigit() for char in keyword):
                                print("Please enter keyword without numbers!")
                                keyword = False
                                continue
                            elif any(char == " " for char in keyword):
                                print("Please enter keyword without space!")
                                keyword = False
                                continue
                            elif keyword == "":
                                print("Please enter a keyword!")
                                continue
                            elif not keyword.isalpha():
                                print(
                                    "Please enter keyword without special characters!")
                                keyword = False
                                continue
                            elif thesaurus.checkDup(keyword):
                                synonyms, _ = thesaurus.addSynonym(
                                    keyword, thesaurus.thesaurus[keyword])
                                if str(synonyms) != "":
                                    thesaurus.thesaurus[keyword] = synonyms
                                print(
                                    f"""\nYour edited Thesaurus is ready and printed here....\n{thesaurus}\n""")
                            else:
                                print(
                                    f"Keyword {keyword} not in existing Thesaurus")
                                keyword = False
                                continue
                    # Edit keywords
                    elif advanceChoice == "3":
                        editKeyword = False
                        while not editKeyword:
                            print(
                                f"""\nPrinting existing Thesaurus....\n{thesaurus}""")
                            keyword = False
                            while not keyword:
                                keyword = input(
                                    "\nEnter keyword to edit (Enter 0 to return): ")
                                keyword = keyword.strip().lower()
                                if keyword == "0":
                                    keyword = True
                                    editKeyword = True
                                    continue
                                elif any(char.isdigit() for char in keyword):
                                    print("Please enter keyword without numbers!")
                                    keyword = False
                                    continue
                                elif any(char == " " for char in keyword):
                                    print("Please enter keyword without space!")
                                    keyword = False
                                    continue
                                elif keyword == "":
                                    print("Please enter a keyword!")
                                    continue
                                elif not keyword.isalpha():
                                    print(
                                        "Please enter keyword without special characters!")
                                    keyword = False
                                    continue
                                elif thesaurus.checkDup(keyword):
                                    newKeyword = False
                                    # keyword validation
                                    while not newKeyword:
                                        newKeyword = input(
                                            f"\nEnter new keyword to replace \"{keyword}\" (Enter 0 to return): ")
                                        newKeyword = newKeyword.strip().lower()
                                        if newKeyword == "0":
                                            newKeyword = True
                                            continue
                                        elif any(char.isdigit() for char in newKeyword):
                                            print(
                                                "Please enter keyword without numbers!")
                                            newKeyword = False
                                            continue
                                        elif any(char == " " for char in newKeyword):
                                            print(
                                                "Please enter keyword without space!")
                                            newKeyword = False
                                            continue
                                        elif newKeyword == "":
                                            print("Please enter a keyword!")
                                            continue
                                        elif not newKeyword.isalpha():
                                            print(
                                                "Please enter keyword without special characters!")
                                            newKeyword = False
                                            continue
                                        elif thesaurus.checkDup(newKeyword):
                                            print(
                                                f"Keyword \"{newKeyword}\" is already exist in thesaurus!")
                                            newKeyword = False
                                            continue
                                        elif thesaurus.thesaurus[keyword].checkExist(Word(newKeyword)):
                                            print(
                                                f"Keyword \"{newKeyword}\" is a synonym in thesaurus!")
                                            newKeyword = False
                                            continue
                                        else:
                                            thesaurus.thesaurus[newKeyword] = thesaurus.thesaurus[keyword]
                                            del thesaurus.thesaurus[keyword]
                                            if str(thesaurus):
                                                print(
                                                    f"""\nYour edited Thesaurus is ready and printed here....\n{thesaurus}\n""")
                                            else:
                                                print(f"\nYour new Thesaurus is empty...\n")
                                    newKeywordValid = False
                                    # check if more keyword should be added
                                    while not newKeywordValid:
                                        shouldContinue = input(
                                            f"Do you want to edit more keywords? y/n: ")
                                        shouldContinue = shouldContinue.lower()
                                        if shouldContinue == "n":
                                            newKeywordValid = True
                                            editKeyword = True
                                            continue
                                        elif shouldContinue != "y":
                                            newKeywordValid = False
                                            print(
                                                "\nInvalid input. Please enter only \"y\" or \"n\"")
                                            continue
                                        newKeywordValid = True
                                        editKeyword = False
                                else:
                                    print(
                                        f"Keyword {keyword} not in existing Thesaurus")
                                    keyword = False
                                    continue
                    # Edit synonyms
                    elif advanceChoice == "4":
                        editSynonym = False
                        while not editSynonym:
                            keyword = False
                            # keyword validation
                            while not keyword:
                                print(
                                f"""\nPrinting existing Thesaurus....\n{thesaurus}""")
                                keyword = input(
                                    "\nEnter keyword to edit synonyms (Enter 0 to return): ")
                                keyword = keyword.strip().lower()
                                if keyword == "0":
                                    keyword = True
                                    editSynonym = True
                                    continue
                                elif any(char.isdigit() for char in keyword):
                                    print("Please enter keyword without numbers!")
                                    keyword = False
                                    continue
                                elif any(char == " " for char in keyword):
                                    print("Please enter keyword without space!")
                                    keyword = False
                                    continue
                                elif keyword == "":
                                    print("Please enter a keyword!")
                                    keyword = False
                                    continue
                                elif not keyword.isalpha():
                                    print(
                                        "Please enter keyword without special characters!")
                                    keyword = False
                                    continue
                                elif thesaurus.checkDup(keyword):
                                    synonymValid = False
                                    selectMenu = Menu(
                                        f"Which of the following synonym do you want to edit? (Enter 0 to return)", True)
                                    synonymArr = thesaurus.thesaurus[keyword].convertList(
                                    )
                                    selectMenu.insert(synonymArr)
                                    selectValid = False
                                    while not selectValid:
                                        selectMenu.show()
                                        selectChoice = input("Enter choice: ")
                                        if selectChoice == "0":
                                            selectValid = True
                                        elif selectChoice.isnumeric():
                                            if int(selectChoice) >= 1 and int(selectChoice) <= len(synonymArr):
                                                selectChoice = int(
                                                    selectChoice) - 1
                                                synonym = True
                                                while synonym:
                                                    synonym = input(
                                                        f"Enter new synonym for \"{keyword}\" to replace \"{synonymArr[selectChoice]}\" (Enter 0 to return): ")
                                                    synonym = synonym.strip().lower()
                                                    if synonym == "0":
                                                        editSynonym = True
                                                        synonym = False
                                                    elif synonym == keyword:
                                                        print(
                                                            "Invalid Input! Do not enter keyword again!\n")
                                                    elif any(char.isdigit() for char in synonym):
                                                        print(
                                                            "Please enter synonym without numbers!\n")
                                                    elif any(char == " " for char in synonym):
                                                        print(
                                                            "Please enter synonym without space!\n")
                                                    elif thesaurus.thesaurus[keyword].checkExist(Word(synonym)):
                                                        print(
                                                            "Synonym already exist! Please Try Again!\n")
                                                    elif not synonym.isalpha():
                                                        print(
                                                            "Please enter synonym without special characters!\n")
                                                    elif synonym == "":
                                                        print("Please enter a synonym!\n")
                                                    else:
                                                        thesaurus.thesaurus[keyword].delete(
                                                            selectChoice)
                                                        thesaurus.thesaurus[keyword].insert(
                                                            Word(synonym))
                                                        synonym = False
                                                selectValid = True
                                                if str(thesaurus):
                                                    print(
                                                        f"""\nYour edited Thesaurus is ready and printed here....\n{thesaurus}\n""")
                                                else:
                                                    print(f"\nYour new Thesaurus is empty...\n")
                                            else:
                                                print(
                                                    f"\nOnly options between 0 to {len(synonymArr)} are available. Please try again!")
                                        else:
                                            print(
                                                "\nYou must enter a number. Please try again!")
                                else:
                                    print(
                                        f"Keyword {keyword} not in existing Thesaurus")
                                    keyword = False
                                    continue
                            editSynonymValid = False
                            while not editSynonymValid:
                                shouldContinue = input(
                                    f"Do you want to edit more synonyms? y/n: ")
                                shouldContinue = shouldContinue.lower()
                                if shouldContinue == "n":
                                    editSynonymValid = True
                                    editSynonym = True
                                    continue
                                elif shouldContinue != "y":
                                    editSynonymValid = False
                                    print(
                                        "\nInvalid input. Please enter only \"y\" or \"n\"")
                                    continue
                                editSynonymValid = True
                                editSynonym = False
                    # Delete keyword
                    elif advanceChoice == "5":
                        delKeyword = False
                        thesaurusDel = False
                        while not delKeyword:
                            print(
                                f"""\nPrinting existing Thesaurus....\n{thesaurus}""")
                            keyword = False
                            while not keyword:
                                keyword = input(
                                    "\nEnter keyword to delete (Enter 0 to return): ")
                                keyword = keyword.strip().lower()
                                if keyword == "0":
                                    keyword = True
                                    delKeyword = True
                                    continue
                                elif any(char.isdigit() for char in keyword):
                                    print("Please enter keyword without numbers!")
                                    keyword = False
                                    continue
                                elif any(char == " " for char in keyword):
                                    print("Please enter keyword without space!")
                                    keyword = False
                                    continue
                                elif keyword == "":
                                    print("Please enter a keyword!")
                                    continue
                                elif not keyword.isalpha():
                                    print(
                                        "Please enter keyword without special characters!")
                                    keyword = False
                                    continue
                                elif thesaurus.checkDup(keyword):
                                    delKeywordValid = False
                                    while not delKeywordValid:
                                        shouldContinue = input(
                                            f"\nAre you should you want to delete \"{keyword}\"? y/n: ")
                                        shouldContinue = shouldContinue.lower()
                                        if shouldContinue == "n":
                                            delKeywordValid = True
                                            delKeyword = False
                                            continue
                                        elif shouldContinue != "y":
                                            delKeywordValid = False
                                            print(
                                                "\nInvalid input. Please enter only \"y\" or \"n\"")
                                            continue
                                        delKeywordValid = True
                                        delKeyword = False
                                        del thesaurus.thesaurus[keyword]
                                        if str(thesaurus):
                                            print(
                                                f"""\nYour edited Thesaurus is ready and printed here....\n{thesaurus}""")
                                        else:
                                            print(f"\nYour new Thesaurus is empty...\n")
                                            delKeyword = True
                                            del thesaurus
                                            thesaurusDel = True
                                else:
                                    print(
                                        f"Keyword {keyword} not in existing Thesaurus")
                                    keyword = False
                                    continue
                            delKeywordValid = False
                            while not delKeywordValid and not thesaurusDel:
                                shouldContinue = input(
                                    f"\nDo you want to delete more keywords? y/n: ")
                                shouldContinue = shouldContinue.lower()
                                if shouldContinue == "n":
                                    delKeywordValid = True
                                    delKeyword = True
                                    continue
                                elif shouldContinue != "y":
                                    delKeywordValid = False
                                    print(
                                        "\nInvalid input. Please enter only \"y\" or \"n\"")
                                    continue
                                delKeywordValid = True
                                delKeyword = False
                    # Delete synonym
                    elif advanceChoice == "6":
                        delSynonym = False
                        thesaurusDel = False
                        while not delSynonym:
                            print(
                                f"""\nPrinting existing Thesaurus....\n{thesaurus}""")
                            keyword = False
                            while not keyword:
                                keyword = input(
                                    "\nEnter keyword to delete synonyms (Enter 0 to return): ")
                                keyword = keyword.strip().lower()
                                if keyword == "0":
                                    keyword = True
                                    delSynonym = True
                                    continue
                                elif any(char.isdigit() for char in keyword):
                                    print("Please enter keyword without numbers!")
                                    keyword = False
                                    continue
                                elif any(char == " " for char in keyword):
                                    print("Please enter keyword without space!")
                                    keyword = False
                                    continue
                                elif keyword == "":
                                    print("Please enter a keyword!")
                                    continue
                                elif not keyword.isalpha():
                                    print(
                                        "Please enter keyword without special characters!")
                                    keyword = False
                                    continue
                                elif thesaurus.checkDup(keyword):
                                    synonymValid = False
                                    selectMenu = Menu(
                                        f"Which of the following synonym do you want to delete? (Enter 0 to return)", True)
                                    synonymArr = thesaurus.thesaurus[keyword].convertList(
                                    )
                                    selectMenu.insert(synonymArr)
                                    selectValid = False
                                    while not selectValid:
                                        selectMenu.show()
                                        selectChoice = input("Enter choice: ")
                                        if selectChoice == "0":
                                            selectValid = True
                                        elif selectChoice.isnumeric():
                                            if int(selectChoice) >= 1 and int(selectChoice) <= len(synonymArr):
                                                selectChoice = int(
                                                    selectChoice) - 1
                                                delSynonymCheckValid = False
                                                while not delSynonymCheckValid:
                                                    shouldContinue = input(
                                                        f"\nAre you should you want to delete \"{synonymArr[selectChoice]}\"? y/n: ")
                                                    shouldContinue = shouldContinue.lower()
                                                    if shouldContinue == "n":
                                                        delSynonymCheckValid = True
                                                        delSynonymCheck = False
                                                        continue
                                                    elif shouldContinue != "y":
                                                        delSynonymCheckValid = False
                                                        print(
                                                            "\nInvalid input. Please enter only \"y\" or \"n\"")
                                                        continue
                                                    delSynonymCheckValid = True
                                                    delSynonymCheck = False
                                                    thesaurus.thesaurus[keyword].delete(
                                                        selectChoice)
                                                    if thesaurus.thesaurus[keyword].getSize() == 0:
                                                        del thesaurus.thesaurus[keyword]
                                                    if str(thesaurus):
                                                        print(
                                                            f"""\nYour edited Thesaurus is ready and printed here....\n{thesaurus}""")
                                                    else:
                                                        print(f"\nYour new Thesaurus is empty...\n")
                                                        delSynonymCheck = True
                                                        del thesaurus
                                                        thesaurusDel = True
                                                        delSynonym = True
                                                selectValid = True
                                            else:
                                                print(
                                                    f"\nOnly options between 0 to {len(synonymArr)} are available. Please try again!")
                                        else:
                                            print(
                                                "\nYou must enter a number. Please try again!")
                                else:
                                    print(
                                        f"Keyword {keyword} not in existing Thesaurus")
                                    keyword = False
                                    continue
                            delSynonymValid = False
                            while not delSynonymValid and not thesaurusDel:
                                shouldContinue = input(
                                    f"\nDo you want to delete more synonyms? y/n: ")
                                shouldContinue = shouldContinue.lower()
                                if shouldContinue == "n":
                                    delSynonymValid = True
                                    delSynonym = True
                                    continue
                                elif shouldContinue != "y":
                                    delSynonymValid = False
                                    print(
                                        "Invalid input. Please enter only \"y\" or \"n\"")
                                    continue
                                delSynonymValid = True
                                delSynonym = False
                    # Delete Thesaurus
                    else:
                        del thesaurus
                        print("\nYou have successfully deleted your thesaurus!\n")
                    os.system("pause") # Get "Press any key to continue"
            # New Features
            elif choice == '6':
                print("\nWelcome to Spell Checker!\nDon\'t know how to spell? Enter keyword here!")
                keyword = False
                while not keyword:
                    keyword = input(
                        "\nEnter keyword (Enter 0 to return): ")
                    keyword = keyword.strip().lower()
                    if keyword == "0":
                        continue
                    elif any(char.isdigit() for char in keyword):
                        print("Please enter keyword without numbers!")
                        keyword = False
                        continue
                    elif any(char == " " for char in keyword):
                        print("Please enter keyword without space!")
                        keyword = False
                        continue
                    elif keyword == "":
                        print("Please enter a keyword!")
                        continue
                    elif not keyword.isalpha():
                        print("Please enter keyword without special characters!")
                        keyword = False
                        continue
                if keyword != "0":
                    similarArr = getSimilarWords(keyword)
                    if len(similarArr) != 0:
                        print(", ".join(similarArr))
                    else:
                        print(f"No similar words to {keyword}")
                    print("")
                    os.system("pause") # Get "Press any key to continue"
            elif choice == '7':
                # Check if thesaurus exist
                try:
                    if not str(thesaurus):
                        print(
                            f"\nYour Thesaurus is empty...\nPlease create/open a thesaurus.\n")
                        continue
                except UnboundLocalError:
                    print(f"\nNo Thesaurus found! Please create/open a thesaurus.")
                    continue
                if thesaurus.filePath:
                    print(f"""
The Thesaurus \"{thesaurus.filePath.split(chr(92))[-1]}\" is printed here....""")
                else:
                    print("""
The Thesaurus created is printed here....""")
                print(f"{thesaurus}\n")
                os.system("pause") # Get "Press any key to continue"
            elif choice == '8':
                # Check if thesaurus exist
                try:
                    if not str(thesaurus):
                        print(
                            f"\nYour Thesaurus is empty...\nPlease create/open a thesaurus.\n")
                        continue
                except UnboundLocalError:
                    print(f"\nNo Thesaurus found! Please create/open a thesaurus.")
                    continue
                print("\nSave")
                thesaurus.save()
                os.system("pause") # Get "Press any key to continue"
            elif choice == '9':
                # Check if thesaurus exist
                try:
                    if not str(thesaurus):
                        print(
                            f"\nYour Thesaurus is empty...\nPlease create/open a thesaurus.\n")
                        continue
                except UnboundLocalError:
                    print(f"\nNo Thesaurus found! Please create/open a thesaurus.")
                    continue
                print("\nSave As")
                validFile = False
                while not validFile:
                    filePath = input(
                        "Please enter new filename (Enter 0 to return): ")
                    if filePath == "0":
                        validFile = True
                        continue
                    if ".txt" != filePath[-4:]:
                        print("Invalid File Type! Please try again!\n")
                        validFile = False
                        continue
                    if ":\\" not in filePath:
                        filePath = os.path.abspath(
                            os.getcwd()) + "\\" + filePath
                    validFile = True
                if filePath != "0":
                    fileExist = os.path.isfile(
                                filePath) and os.path.exists(filePath)
                    fileName = filePath.split("\\")[-1]
                    saveFile = True
                    if fileExist:
                        fileValid = False
                        while not fileValid:
                            shouldContinue = input(
                                f"\nDo you want to overwrite {fileName}'s content? y/n: ")
                            shouldContinue = shouldContinue.lower()
                            if shouldContinue == "n":
                                fileValid = True
                                validFile = False
                                saveFile = False
                                continue
                            elif shouldContinue != "y":
                                fileValid = False
                                print(
                                    "\nInvalid input. Please enter only \"y\" or \"n\"")
                                continue
                            fileValid = True
                    if saveFile:
                        thesaurus.saveAs(filePath)
                os.system("pause") # Get "Press any key to continue"
            elif choice == '10':
                print(
                    '\nBye, thanks for using ST1507 DSAA: Thesaurus Based Text Processor\n')
                exit()
            elif choice.isnumeric():
                print("\nOnly options between 1 to 10 are available. Please try again!")
                choice = False
            else:
                print("\nYou must enter a number. Please try again!")
                choice = False


if __name__ == "__main__":
    main()
