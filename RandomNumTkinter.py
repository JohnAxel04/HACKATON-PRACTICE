import tkinter as rand
import random

dom = random.randint(1,11)
count = 0
def main():
    global count
    
    count += 1 
    try:
        enter1 = int(enter.get())    
        if enter1 not in range(1,11):
            title['text'] = "The input number exceed the requirment"

        elif enter1 > dom:
            title['text'] = f"{count}Try: Too high"

        elif enter1 < dom:
            title['text'] = f"{count}Try: Too low"

        else:
            
            title['text'] = f"Congratulation you guess the right number{dom} in {count} trys"
        
        
    except:
        title['text'] = "Error"

    
    
window = rand.Tk()
title = rand.Label(window,text=f"Guess a number(1-10):")
title.pack()
enter = rand.Entry(window)
enter.pack()
btn = rand.Button(window,text="Guess",command=main)
btn.pack()

window.mainloop()