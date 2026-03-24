import tkinter as world
import json


root = world.Tk()

def popup():
    popp = world.Toplevel(root)
    popp.geometry("250x250")
    popp.title("Profile Card")
    text_tile = world.Label(popp,text="Profile Card")
    text_tile.pack()
    popFrame = world.Frame(popp,bg="grey")
    popFrame.pack()
    imgq = world.PhotoImage(file="pic.png")
    imgq = imgq.subsample(7,7)
    imglabel = world.Label(popFrame, image=imgq, anchor="n",bg="grey",width=200)
    imglabel.image = imgq
    imglabel.grid(column=0,row=0,columnspan=2)
    namePop = world.Label(popFrame,text="Name:",bg="grey",fg="white")
    namePop.grid(column=0,row=1)
    namePop2 = world.Label(popFrame,text="werqwerwer: ",bg="grey",fg="white")
    namePop2.grid(column=1,row=1)
    agePop = world.Label(popFrame,text="age:",bg="grey",fg="white")
    agePop.grid(column=0,row=2)
    agePop2 = world.Label(popFrame,text="20",bg="grey",fg="white")
    agePop2.grid(column=1,row=2)
    genderPop = world.Label(popFrame,text="Gender: ",bg="grey",fg="white")
    genderPop.grid(column=0,row=3)
    genderPop2 = world.Label(popFrame,text="",bg="grey",fg="white")
    genderPop2.grid(column=1,row=3)
    newvar = varr.get()
    if newvar == 0:
        genderPop2["text"] = "male"
    else:
        genderPop2["text"] = "Female"
    try:
        newEntry = int(entry4.get())
        age = 2026 - newEntry
        name4["text"] = f"Your are {age} Years Old"
        agePop2["text"] = age
    except:
        age = "Invalid"
        name4["text"] = "Must not be 0"
        agePop2["text"] = "Must not be 0"
    
    firstname = entry1.get()
    midname = entry2.get()
    lastname = entry3.get()
    namePop2['text'] = f"{firstname} {midname} {lastname}"

    Fold = {
        "First" : entry1.get(),
        "midd" : entry2.get(),
        "last" : entry3.get(),
        "birth" : entry4.get(),
        "age" : age,
        "gender" : genderPop2["text"]
        }
    try:
        with open("Profile.json","r") as file:
            data = json.load(file)
    except:
        data = []
    
    data.append(Fold)

    with open("Profile.json", "w") as file:
        json.dump(data,file,indent=4)

def maleBg():
    root['bg'] = "lightblue"
def femaleBg():
    root['bg'] = "pink"

def showList():
    showTop = world.Toplevel(root)

    try:
        with open("Profile.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        world.Label(showTop,text="No File is found").pack()
        return
    
    for i,profile in enumerate(data):
        text = f"{i+1} First Name: {profile['First']} Middle Name: {profile['midd']} Last Name: {profile['last']} Age: {profile['age']} Gender:{profile['gender']}"
        world.Label(showTop,text=text).pack()


root.title("Profile Card Generator")
root.config(bg="lightblue")

titl = world.Label(root,text="Profile Builder")
titl.pack()
frm = world.Frame(root)
frm.pack(padx=20,pady=5)

entry1 = world.Entry(frm)
entry1.grid(padx=5,pady=5)
entry2 = world.Entry(frm)
entry2.grid(column=1,row=0,padx=5,pady=5)
entry3 = world.Entry(frm)
entry3.grid(column=2,row=0,padx=5,pady=5)
nam1 = world.Label(frm,text="First Name")
nam1.grid(column=0,row=1)
nam2 = world.Label(frm,text="Middle Name")
nam2.grid(column=1,row=1)
nam3 = world.Label(frm,text="Last Name")
nam3.grid(column=2,row=1)

entry4 = world.Entry(frm)
entry4.grid(column=0,row=2)



name4 = world.Label(frm,text="Computing")
name4.grid(column=1,row=2,columnspan=2,rowspan=2)
nam5 = world.Label(frm,text="Birth Year")
nam5.grid(column=0,row=3)
nam6 = world.Label(frm,text="Gender")
nam6.grid(column=0,row=4)
varr = world.IntVar()
rad = world.Radiobutton(frm,text="male",variable=varr,value=0,command=maleBg)
rad.grid(column=1,row=4)
rad1 = world.Radiobutton(frm,text="female",variable=varr,value=1,command=femaleBg)
rad1.grid(column=2,row=4)

def hover(event):
    btn["bg"] = "darkgrey"
def hoverOut(event):
    btn["bg"] = "grey"
btn = world.Button(root,text="Generate",command=popup,bg="grey")
btn.bind("<Enter>", hover)
btn.bind("<Leave>", hoverOut)
def inn(event):
    btn["bg"] = "darkgreen"
def outt(event):
    btn["bg"] = "darkgreen"
btn.pack(pady=10)
showw = world.Button(root,text="Show Profiles" ,command=showList,bg="green")
showw.bind("<Enter>", inn)
showw.bind("<Leave>", outt)
showw.pack(pady=10)

root.mainloop()