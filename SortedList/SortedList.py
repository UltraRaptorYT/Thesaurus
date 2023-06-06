"""
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
"""

from SortedList.Word import Word
import random

"""
SortedList class is a LinkedList that when inserting elements it will sort by __lt__.
"""
class SortedList:
    def __init__(self):
        # Pointer towards the first Node (currently nothing)
        self.headNode = None
        self.currentNode = None
        self.length = 0  # Variable we manually keep track of number of Nodes in the list
    """
    A private function to append element to the start of the LinkedList
    """
    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
    """
    The insert function takes in a newNode variable to add it in the LinkedList.
    Raise a TypeError to make sure that the newNode variable is a Word object.
    It loops through using linearSorting algorithm to check each element to see what is __lt__
    """
    def insert(self, newNode):
        if not isinstance(newNode,Word):
            raise TypeError("Only Word Class Objects can be inserted into SortedList")
        self.length += 1
        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return

        # Check if it is going to be new head
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return

        # Check it is going to be inserted
        # between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        # Once we reach here it must be added at the tail
        # Because newNode is largest than all the other nodes.
        leftNode.nextNode = newNode

    """
    Loop through and concatenate the node values together
    """
    def __str__(self):
        # We start at the head
        output = ""
        node = self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = f"{node.__str__()}"
                firstNode = False
            else:
                output += (', ' + f"{node.__str__()}")
            node = node.nextNode
        return f"{output}"

    """
    To check if element exist in the sortedList, we will be using a linearSorting algorithm.
    The idea is just to go through the list in order and look and check if nodes values are the same as parameter passed.
    """
    def checkExist(self, word:str):
        # Check if list is empty
        if self.headNode is None:
            return False
        leftNode = self.headNode
        if leftNode == word:
            return True
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if rightNode == word:
                return True
            leftNode = rightNode
            rightNode = rightNode.nextNode
        return False

    """
    Loop through and concatenate the linkedList and appending it to an array.
    """
    def convertList(self):
        if self.headNode is None:
            return False
        linkedArr = [self.headNode]
        rightNode = self.headNode.nextNode
        while rightNode != None:
            linkedArr.append(rightNode)
            rightNode = rightNode.nextNode
        return linkedArr

    """"
    sort() function checks what kind of sorting type and what mergeSort algorithm was used.
    """
    def sort(self, sortType:str):
        # Check if list is empty
        if self.headNode is None:
            return False
        sortedList = SortedList()
        if sortType == "Alphabetically (Default)":
            sortedList.headNode = self.mergeSort(self.headNode,"alpha")
        elif sortType == "Length/Alphabetically":
            sortedList.headNode = self.mergeSort(self.headNode, "alpha")
            sortedList.headNode = self.mergeSort(sortedList.headNode, "len")
        elif sortType == "Length/Random Alphabetically":
            sortedList = self.randomSort()
            sortedList.headNode = self.mergeSort(sortedList.headNode, "len")
        else:
            sortedList = self.randomSort()
        return sortedList

    """
    To randomise the sorting, we convert the linkedList to array and then use the random.shuffle to shuffle the array.
    To reindex the nextNode values, we need to set it to none and it will append the items to the end of the SortedList.
    """
    def randomSort(self):
        sortedList = SortedList()
        linkedArr = self.convertList()
        random.shuffle(linkedArr)
        for items in linkedArr:
            items.nextNode = None
            sortedList.__appendToTail(items)
        return sortedList

    """
    Appending to the end of the LinkedList.
    To make sure newNode is a Word object, we will raise a TypeError
    """
    def __appendToTail(self, newNode):
        if not isinstance(newNode,Word):
            raise TypeError("Only Word Class Objects can be inserted into SortedList")
        self.length += 1
        if self.headNode == None:
            self.headNode = newNode
            return
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            leftNode = rightNode
            rightNode = rightNode.nextNode
        leftNode.nextNode = newNode

    """
    To delete the items, we will use the first check if the index is in the range of the sortedList [IndexError].
    """
    def delete(self, index:int):
        if index >= self.getSize():
            raise IndexError("list index out of range from sorted list")
        self.length -= 1
        if index == 0:
            self.headNode = self.headNode.nextNode
            return
        elif index == self.getSize() - 1:
            prevNode = self.getIndex(self.getSize() - 2)
            prevNode.nextNode = None
            return
        else:
            prevNode = self.getIndex(index - 1)
            deleteNode = self.getIndex(index)
            nextNode = deleteNode.nextNode
            prevNode.nextNode = nextNode
            return

    """
    To merge the sorted arrays together, we will use the sortedMerge function.
    This function takes in 2 linked lists and a sorting type.
    It will compare the 2 linked lists data points recursively based on the sorting type.
    This sorting of the 2 linked lists are concatenated together using a temp list
    It will return a temp list
    """
    def sortedMerge(self, left, right, sortType:str):
        # Create a temp list NULL
        result = None

        # If left is empty then return right
        if left == None:
            return right
        # If right is empty then return left
        if right == None:
            return left
        if sortType == "alpha":
            # If left value is smaller or equal to right value
            if left.name <= right.name:
                # assign temp to left value
                result = left
                # Recursively check left next value is smaller or equal to right value
                result.nextNode = self.sortedMerge(left.nextNode, right, sortType)
            else:
                # assign temp to right value
                result = right
                # Recursively check right next value is smaller or equal to left value
                result.nextNode = self.sortedMerge(left, right.nextNode, sortType)
        elif sortType == "len":
            # If left length is smaller or equal to right length
            if left.size() <= right.size():
                # assign temp to left value
                result = left
                # Recursively check left next value is smaller or equal to right value
                result.nextNode = self.sortedMerge(left.nextNode, right, sortType)
            else:
                # assign temp to right value
                result = right
                # Recursively check right next value is smaller or equal to left value
                result.nextNode = self.sortedMerge(left, right.nextNode, sortType)
        # return temp list
        return result
    
    """
    We will implement a mergeSort algorithm with the current linked list.
    Merge Sort Algorithm takes the array and split it into half. 
    It will continue splitting the array into individual nodes [Recursively]
    After splitting the nodes into individual nodes, we will use a temp nodes to 
    """
    def mergeSort(self,headNode, sortType:str = "alpha"):
        if headNode == None or headNode.nextNode == None:
            return headNode
        # Get middle of the link list
        middle = self.getMiddle(headNode)
        nextToMid = middle.nextNode

        # Set the next to middle node to None
        middle.nextNode = None

        # Apply mergeSort on left list
        left = self.mergeSort(headNode,sortType)
        # print(left)
        # Apply mergeSort on right list
        right = self.mergeSort(nextToMid,sortType)
        # print(right)

        # Merge the left and right lists
        sortedList = self.sortedMerge(left, right, sortType)
        return sortedList

        

    """
    Using a One-Pass method, we will create two points, slow_pace and fast_pace.
    We will make fast_pace transverse the list twice as fast_pace as slow_pace.
    When fast_pace reach the end of the list, the slow_pace will be at the middle.
    """
    def getMiddle(self, headNode):
        if (headNode == None):
            return headNode
        slow_pace = headNode
        fast_pace = headNode
        while (fast_pace.nextNode != None and
               fast_pace.nextNode.nextNode != None):
            slow_pace = slow_pace.nextNode
            fast_pace = fast_pace.nextNode.nextNode
        return slow_pace

    # Use a Zero Index based system to get index
    def getIndex(self, index:int):
        length = 0
        # Check if index is more than length
        if index > self.length:
            raise IndexError(
                "list index out of range from sorted list")
        # Check if list is empty
        if self.headNode is None:
            return None
        leftNode = self.headNode
        if index == length:
            self.currentNode = leftNode
            return self.currentNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            length += 1
            if index == length:
                self.currentNode = rightNode
                return self.currentNode
            leftNode = rightNode
            rightNode = rightNode.nextNode
        return None

    # Get the length of the SortedList by looping through the LinkedList and increment the length if necessary
    def getSize(self):
        length = 0
        # Check if list is empty
        if self.headNode is None:
            self.length = length
            return self.length
        length = 1
        rightNode = self.headNode.nextNode
        while rightNode != None:
            length += 1
            rightNode = rightNode.nextNode
        self.length = length
        return self.length
