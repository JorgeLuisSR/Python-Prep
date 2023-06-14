
import sys
if not sys.path.__contains__(r"C:/xampp/htdocs/Python-Prep"):
    sys.path.append(r"C:/xampp/htdocs/Python-Prep")
    print(sys.path)


import M07_funciones.Prep_Course_Homework_07 as m7

class Calc:
    def __init__(self, lista):
        print("WeirdCalculator has begun its program :)")
        self.li = lista
    def isPrime(self, n):
        return m7.isPrime(n)
    def factorial(self, n):
        return m7.factorial(n)
    def unitChange(self, n, uo, ud):
        return m7.unitChange(n, uo, ud)
    def mostRepeated(self, isMax=False):
        return m7.mostRepeated(self.li, isMax)
    def keepPrime(self):
        return m7.keepPrimes(self.li)