inp1 = int(input("Put a number"))
inp2 = int(input("Put a number"))
inp3= int(input("Put a number"))
if inp1 > 2 and inp1 > inp3:
    print(f"This is the highest Number {inp1}")
elif inp2 > inp1 and inp2 > inp3:
    print(f"This is the highest Number {inp2}")
else:
    print(f"This is the highest Number {inp3}")