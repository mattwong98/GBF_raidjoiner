import random,pyautogui, time
from methods import clickInRange, clickInRangeFast

def main():
    print("I am testing the code function:")
    #calls the methods defined below
    HelloWorld()
    PrintNumber()
    AddAndPrint()
    HighFive()
    SubName()


def HelloWorld():
    print ("Hello World")
    return

def PrintNumber():
    x = int(input("Enter a number"))
    print ("The number is", x)
    return

def AddAndPrint():
    Add1 = int(input("First number to add:"))
    Add2 = int(input("Second number to add:"))
    print(Add1 + Add2)
    return

def HighFive():
    number = 5
    print (number)
    return

def SubName():
    Sub1 = int(input("First number to subtract:"))
    Sub2 = int(input("Second number to subtract:"))
    print (Sub2 - Sub1)
    return

if __name__ == "__main__":
    main()