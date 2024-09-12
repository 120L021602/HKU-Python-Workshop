# Given the following code as the main program, complete two functions readList() and findNo() as explained below.
#
# The program
# myList = readList()
# number = int(input())
# print(findNo(myList, number))
# Explanation
# readList(): Read numbers from user until zero is received. Return the list of numbers.
# findNo(myList, number): return True if the number in the list; else False.

"""
Complete this function
readList(): Read numbers from user until zero is received, return the list of numbers.
"""


def readList():
    myList = []
    x = int(input())
    while x != 0:
        myList.append(x)
        x = int(input())
    return myList


'''
Complete this function
findNo(myList, number): Return 'True' if the number in the List; else return 'False'
'''


def findNo(myList, number):
    if number in myList:
        return True
    else:
        return False



#Given main routine
myList = readList()
number = int(input())
print(findNo(myList, number))
