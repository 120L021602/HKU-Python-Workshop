# Write a program that reads an input string, and print a list of strings following a specific pattern as shown below.
# Suppose the input string is hello, the output should be:
# hellohello
# _ellohell
# __llohel
# ___lohe
# ____oh
# Another example output for the input foobar:
# foobarfoobar
# _oobarfooba
# __obarfoob
# ___barfoo
# ____arfo
# _____rf

inputString = input()
doubleInputString = inputString + inputString
timesOfIteration = len(inputString) - 1
print(doubleInputString)
for i in range(0, timesOfIteration):
    doubleInputString = doubleInputString[1: len(doubleInputString) - 1]
    prefix = "_" * (i + 1)
    print(prefix + doubleInputString)