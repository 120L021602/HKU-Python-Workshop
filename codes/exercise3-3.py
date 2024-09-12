# Continue with the definition of the class `Frac` in Demo 3-3. Add the following features: Allow objects of Frac
# class to be printed directly. E.g., print(Frac(1, 2)) shoud print 1/2. Define function averageWith() that takes one
# object of Frac class and return the average of the current fraction with the input. E.g., Frac(1, 4).averageWith(
# Frac(3, 4)) should gives an object of Frac class that represents \\( \frac{1}{2} \\). Using the Frac class defined,
# complete your program with the following main routine that calculates the harmonic mean of two input integers.

from math import gcd


class Frac:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def n(self):
        return self.numerator

    def d(self):
        return self.denominator

    def simplify(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // common
        self.denominator = self.denominator // common

    def averageWith(self, numerator, denominator):
        newDenominator = self.denominator * denominator
        newNumerator = self.numerator * denominator + numerator * self.denominator
        newFrac = Frac(newNumerator, newDenominator * 2)
        newFrac.simplify()
        return newFrac

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def invert(self):
        return Frac(self.denominator, self.numerator)


a = int(input())
b = int(input())
print(Frac(1, a).averageWith(1, b).invert())
