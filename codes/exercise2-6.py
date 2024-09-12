# Write a program that reads integers into a list until 0 is read.
# The list must be kept sorted all the time.
# When a `0` is read, the program should print a history of the list built.
# For example, if the input is 1 4 2 3 0, the output should be:
# [1]
# [1, 4]
# [1, 2, 4]
# [1, 2, 3, 4]

myList = []
x = int(input())
while x != 0:
    myList.append(x)
    x = int(input())
for i in range(0, len(myList)):
    tempList = myList[0: i + 1]
    sortedList = sorted(tempList)
    print(sortedList)
