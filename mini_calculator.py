print("---mini-calculator----")
num1 = float(input("enter the first number here: "))
num2 = float(input("enter the secound number here: "))

print("pres 1 for addition\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division")

choise = int (input("enter the choice between1-4: "))

if choise ==1:
    print("the addition oftwo numbers:",num1+num2)
elif choise ==2:
    print("the subtraction of two numbers are:",num1-num2)
elif choise ==3:
    print("the multiplication of two numbers:",num1*num2)
elif choise ==4:
    print("the division of two numbers:",num1/num2)
else:
    print("input is unvalid")