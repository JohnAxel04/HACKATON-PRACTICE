def summ(inp1,inp2,inp3,inp4,inp5):
    group = inp1,inp2,inp3,inp4,inp5
    summary = sum(group)
    return summary



inp1 = int(input("Put a number"))
inp2 = int(input("Put a number"))
inp3= int(input("Put a number"))
inp4= int(input("Put a number"))
inp5= int(input("Put a number"))

print(summ(inp1,inp2,inp3,inp4,inp5))