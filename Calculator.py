print("basic calculator")

while True:
    num1 = eval(input("Input1: "))
    num2 = eval(input("Input2: "))
    sele = input("+,-,*,/: ")

    if sele == "+":
        result = num1 + num2
    elif sele == "-":
        result =num1 - num2
    elif sele == "*":
        result =num1 * num2
    elif sele == "/":
        result =num1 / num2
    else:
        print("Please select input")
    
    print(f"The Result is {result}")
    ques = input("want to continue(yes,no): ")
    if ques == "yes":
        continue
    else:
        break