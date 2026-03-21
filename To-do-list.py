lagayan_ko = []

def add():
    addtask = input("Add Task: ")
    if addtask != "":
        lagayan_ko.append(addtask)  
        print("task is added")
    else:
        print("Input must not be blank")
def show():
    if len(lagayan_ko) == 0:
        print("You have zero task")
    else:
        print("This is your list of task")
        for i, lagay in enumerate(lagayan_ko):
            
            print(f"{i+1} {lagay}")
def delete():
    show()
    try:
        del1 = int(input("Choose: "))
        lagayan_ko.pop(del1 - 1)
        print("Delete successfully")
    except:
        print("Invalid Input")

def main():
    while True:
        print("Menu")   
        print("1. Add Task")   
        print("2. Show Task")   
        print("3. Delete Task")   
        print("4. Exit")   
        tanong = int(input("Select: "))
        if tanong == 1:
            add()
        elif tanong == 2:
            show()
        elif tanong == 3:
            delete()
        elif tanong == 4:
            break
        else:
            print("Invalid Output")
main()