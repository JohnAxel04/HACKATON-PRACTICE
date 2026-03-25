import tkinter as do
def submit():
    varr = entry1.get()

    if len(varr) == 0:
        last['text'] = "The Task must have a name"
    else:
        newVar = entry1.get()
        listBox1.insert("end",newVar)
        entry1.delete(0,"end")
        last['text'] = "Task successfully added"

def dell():
    try:
        delist = listBox1.curselection()
        if len(delist) == 0:
            last['text'] = "Select to Delete"
        else:
            listBox1.delete(delist)
            last['text'] = "succesfully deleted"
    except:
        do.Label(window,text="Error").pack()
window = do.Tk()
titlle = do.Label(window,text="To Do List")
titlle.pack()
entry1 = do.Entry(window)
entry1.pack()
def in1(event):
    btn['bg'] = "blue"
def ot1(event):
    btn['bg'] = "lightblue"
btn = do.Button(window,text="Submit",command=submit,bg="lightblue",activebackground="darkblue")
btn.bind("<Enter>",in1)
btn.bind("<Leave>",ot1)
btn.pack()
listBox1 = do.Listbox(window)
listBox1.pack()
def inn(event):
    delBTn['bg'] = "green"
def outt(event):
    delBTn['bg'] = "lightgreen"
delBTn = do.Button(window,text="Delete",command=dell,bg="lightgreen",activebackground="darkgreen")
delBTn.bind("<Enter>",inn)
delBTn.bind("<Leave>",outt)
delBTn.pack()

last = do.Label(window,text="")
last.pack()
window.mainloop()