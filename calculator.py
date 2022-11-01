import math
from time import sleep


print("========================================")
print("Welcome to the calculator!")
print("========================================")
sleep(1)


def root(num1):
    return math.sqrt(num1)


def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def exponentiation(num1, num2):
    return num1 ** num2


def percentage(num1, num2):
    return (num1 / num2) * 100


num1 = input("Enter a number: ")
print("Accepted operation symbols: +, -, /, *, √, **, %")
operator = input("Enter a operator: ")
if operator == "√" and num1.isnumeric():
    num1 = float(num1)
    root(num1)
    print(f"square fot of {num1} = {root(num1)}")
elif operator == "√" and not num1.isnumeric():
    print(f"{num1} is not a numeric value! please try again!")

else:
    num2 = input("Enter a second number ")
    if num1.isnumeric and num2.isnumeric():
        num1 = float(num1)
        num2 = float(num2)
        if operator == '+':
            plus(num1, num2)
            print(f" {num1} + {num2} = {plus(num1, num2)}")
        elif operator == '-':
            divide(num1, num2)
            print(f" {num1} - {num2} = {minus(num1, num2)}")
        elif operator == '*':
            multiply(num1, num2)
            print(f" {num1} + {num2} = {multiply(num1, num2)}")
        elif operator == '/':
            if num2 != 0:
                divide(num1, num2)
                print(f" {num1} / {num2} = {divide(num1, num2)}")
        elif operator == "**":
            exponentiation(num1, num2)
            print(f" {num1} ** {num2} = {exponentiation(num1, num2)}")
        elif operator == "%":
            if num2 != 0:
                percentage(num1, num2)
            print(f"{num1} is {percentage(num1, num2)} of {num2}")
        else:
            print("wrong operator, please enter correct one")
    else:
        print("Please enter only numeric values")
        print(f"{num1} is not a numeric value")
        print(f"{num2} is not a numeric value")

