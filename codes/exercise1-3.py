# Write a program that reads any number of integers until a zero is reached, then output the average value of the
# input integers. The output should be an integer, which is the floor of the calculated average. You can refer to the
# notes for example inputs/outputs.


x = int(input())
i = 1
total = 0
average = 0
while x != 0:
    total += x
    x = int(input())
    i += 1
average = total // (i - 1)
print(average)