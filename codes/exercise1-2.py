# Write a program that reads three integers, each representing one side of a triangle. Determine the type of the
# triangle and produce an output "E" if the triangle is equilateral, "I" if isosceles, "R" if right, "S" if scalene,
# and "N" if it is not a triangle. You can refer to the notes for examples.

a = int(input())
b = int(input())
c = int(input())
if a + b <= c or b + a <= c or a + c <= b:
    print("N")
    exit()
if a == b and b == c and a == c:
    print("E")
if (a == b and a != c) or (b == c and a != b) or (a == c and a != b):
    print("I")
if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("R")
elif a != b and b != c and a != c:
    print("S")