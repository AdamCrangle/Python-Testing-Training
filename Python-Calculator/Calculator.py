import Calculator_Logic
UserInput = ""

print("Hello Welcome To Calculator")
print("=============================")
print("To Access The Calculator Please Enter The Type")
while UserInput != "D":

    print("=============================")
    print(" (A) Addition ")
    print(" (B) Subtraction")
    print(" (C) Multiplication")
    print(" (D) Exit")
    print("=============================")

    UserInput = input("Enter Your Choice: ").upper()
    if UserInput == "A":
        print("Addition has been selected")
        print("=============================")
        Input1 = input("Please Enter 1st Number ")
        Input2 = input("Please Enter 2nd Number ")
        if Input1.isdigit() and Input2.isdigit():
            Answer = Calculator_Logic.add(Input1, Input2)
            print("Multiplication Result ", Input1, ' + ', Input2, ' = ', Answer)
        else:
            print("Invalid Input")


    elif UserInput == "B":
        print("Subtraction has been selected")
        print("=============================")
        Input1 = input("Please Enter 1st Number ")
        Input2 = input("Please Enter 2nd Number ")
        if Input1.isdigit() and Input2.isdigit():
            Answer = Calculator_Logic.sub(Input1, Input2)
            print("Subtraction Result ", Input1, ' - ', Input2, ' = ', Answer)
        else:
            print("Invalid Input")

    elif UserInput == "C":
        print("Multiplication has been selected")
        print("=============================")
        Input1 = input("Please Enter 1st Number ")
        Input2 = input("Please Enter 2nd Number ")
        if Input1.isdigit() and Input2.isdigit():
            Answer = Calculator_Logic.mul(Input1, Input2)
            print("Multiplication Result ", Input1, ' * ', Input2, ' = ', Answer)
        else:
            print("Invalid Input")
    elif UserInput == "D":
        print("Exiting")
        break

    else:
        print("Invalid Input")
