def calculation(no1,no2,opt):
    if opt == "+":
        return no1 + no2
    if opt == "-":
        return no1 - no2
    if opt == "*":
        return no1 * no2
    if opt == "/":
        if no2 == "0":
            return("Error")
        return no1 / no2
    else:
        return("Invalid Operator")

def main():
    print("Basic Calculation: ")

    while True:
        try:
            no1 = eval(input("Slot1: "))
            no2 = eval(input("Slot2: "))
            opt = input("+,-,*,/: ")

            result = calculation(no1,no2,opt)
            print(f"Result: {result}")
        except:
            print("Please enter a valid number")
        else:
            last = input("want to continue(yes/no)? ").lower()
            if last == "yes":
                continue
            elif last == "no":
                break
            else:
                print("Invalid Input Try again")
                continue
main()