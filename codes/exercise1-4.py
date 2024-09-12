# Write a program that reads one integer as n, then print the first n Fibonacci numbers.
# First two Fibonacci numbers are 0 and 1, and the third onwards equal to the sum of the two previous numbers.
# Refer to the notes for example inputs/outputs.

n = int(input())
a = 0
b = 1
if n == 1:
    print(0)
elif n == 2:
    print(0, 1, end=" ")
if n >= 3:
    print(0, 1, end=" ")
    for i in range(n - 2):
        tmp = b
        b = a + b
        a = tmp
        print(b, end=" ")
