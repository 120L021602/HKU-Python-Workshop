# Write a program that reads a number of integers until a zero is received.
# Store the integers in a tuple by concatenation and assignment. (E.g.,: myTuple = myTuple + (newValue,))
# After reading all integers, repeatedly remove the first and last item from the tuple and print it. For example, if the input is 1 2 3 4 5 6 7 8 9 0, the output will be:
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
# (2, 3, 4, 5, 6, 7, 8)
# (3, 4, 5, 6, 7)
# (4, 5, 6)
# (5,)

myTuple = ()
x = int(input())
while x != 0:
    myTuple += (x,)
    x = int(input())
print(myTuple)
temp = myTuple[1: len(myTuple)-1]
for i in range(0, len(temp)):
    print(temp)
    if len(temp) == 1 or len(temp) == 2:
        exit()
    temp = temp[1: len(temp)-1]


