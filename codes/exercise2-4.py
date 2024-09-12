# Write a program that reads a number of integers until a zero is received.
# After reading all integers, repeatedly remove the first two items from the list and append the sum of the removed items to the end.
# The program should print the full process starting from the initial list until there is only one item left.
# For example, if the input is 1, 2, 3, 4, 5, 0, the output will be:
# [1, 2, 3, 4, 5]
# [3, 4, 5, 3]
# [5, 3, 7]
# [7, 8]
# [15]

myList = []
x = int(input())
while x != 0:
    myList.append(x)
    x = int(input())
lengthOfMylist = len(myList)
for i in range(lengthOfMylist):
    print(myList)
    tmpList = myList[0:2]
    myList = myList[2:]
    sumOfFirst2 = sum(tmpList)
    myList.append(sumOfFirst2)


