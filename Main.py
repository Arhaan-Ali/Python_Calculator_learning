from pickle import FLOAT

Response1 = input("Would like to use the calculator ? ")
if Response1 == "yes" :
    print("go ahead and chose what you want to do : Add, Subtract, Divide, Multiply two numbers")
    Response2 = input("A for Addition, S for Subtraction, D for Division, M for Multiplication ")
    if Response2 == "A" :
        N1 = float(input("please tell the first number "))
        N2 = float(input("please tell the second number to add with first "))
        result = round(N1 + N2, 2)
        print(f"your answer is: {result}")
    if Response2 == "S" :
        N1 = float(input("please tell the first number "))
        N2 = float(input("please tell the second number to Subtract with first "))
        result = round(N1 - N2, 2)
        print(f"your answer is: {result}")
    if Response2 == "D" :
        N1 = float(input("please tell the first number "))
        N2 = float(input("please tell the second number to divide with first "))
        result = round(N1 / N2, 2)
        print(f"your answer is: {result}")
    if Response2 == "M" :
        N1 = float(input("please tell the first number "))
        N2 = float(input("please tell the second number to Multiply with first "))
        result = round(N1 * N2, 2)
        print(f"your answer is: {result}")
    else:
        print("Wrong Input!")
elif Response1 == "no":
    print("please comeback later when you want to use the calculator.")
else:
    print("please enter either yes or no.")