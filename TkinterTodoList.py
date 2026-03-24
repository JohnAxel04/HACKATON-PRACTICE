import tkinter as all

def addTask():
    newTasks = entry1.get()
    if len(newTasks) == "":
        firstLabel['text'] = "Name must not be Zero"
    else:
        newEntry = entry1.get()
        listb.insert(all.END, newEntry)
        entry1.delete(0,all.END)
        firstLabel['text'] = "Successfully Task is Added"
# def showTask():
#     top = all.Toplevel(window)
#     top.title("Tasks List")
#     try:
#         if len(task) == 0:
#             all.Label(top,text="You have no Task").pack()
#         else:
#             all.Label(top,text="Task List").pack()
            
#             for i, lagay in enumerate(task):
                
                
#     except:
#         all.Label(top,text="Error").pack()

def deleteBtn():
    try:
        selected = listb.curselection()
        listb.delete(selected)
        firstLabel["text"] = "Successfully deleted"
    except:
        firstLabel["text"] = "Error"
window = all.Tk()
window.title()

firstLabel = all.Label(window,text="To do List")
firstLabel.pack()
entry1 = all.Entry(window)
entry1.pack()
btn = all.Button(window,text="Enter",command=addTask).pack()

listb = all.Listbox(window,selectmode="single")
listb.pack()
deleteBtn = all.Button(window,text="Enter",command=deleteBtn)
deleteBtn.pack()
window.mainloop()