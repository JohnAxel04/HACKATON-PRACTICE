import tkinter as new
import random
ran = ["Rock","Paper","Scissor"]
newran = random.choice(ran)

window = new.Tk()
window.title("Rock Paper Scissor Game")

def play(person):
    ComputerLabel['text'] = f"Computer: {newran}"
    PersonLabel['text'] = f"Player: {person}"


    if newran == person:
        mainLabel['text'] = "Draw"
    elif (newran == "Rock" and person == "Paper") or (newran == "Paper" and person == "Scissor") or (newran ==  "Scissor" and person == "Rock"):
        mainLabel['text'] = "Person Win"
    else:
        mainLabel['text'] = "Lose"


mainLabel = new.Label(window,text="Rock Paper Scissor Game")
mainLabel.grid(row=0,columnspan=3)
ComputerLabel = new.Label(window,text="Computer Turn")
ComputerLabel.grid(row=1,columnspan=3)
PersonLabel = new.Label(window,text="Person Turn")
PersonLabel.grid(row=2,columnspan=3)
rockbtn = new.Button(window,text="Rock",command=lambda: play("Rock"))
rockbtn.grid(column=0,row=3)
paperbtn = new.Button(window,text="Paper",command=lambda: play("Paper"))
paperbtn.grid(column=1,row=3)
scissorbtn = new.Button(window,text="Scissor",command=lambda: play("Scissor"))
scissorbtn.grid(column=2,row=3)



window.mainloop()