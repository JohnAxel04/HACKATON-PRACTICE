import random
box = ["Rock","Paper","Scissor"]

def main():
    while True:
        try:
            ran = random.choice(box)
            
            print("Menu")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissor")
            inp1 = int(input("Select to play: "))
            if inp1 == 1:
                players = "Rock"
            elif inp1 == 2:
                players = "Paper"
            elif inp1 == 3:
                players = "Scissor"
            else:
                print("Error")
            print(f"Player: {players}")
            print(f"Computer: {ran}") 

            if (ran == "Rock" and players == "Rock") or (ran == "Paper" and players == "Paper") or (ran == "Scissor" and players == "Scissor"):
                print("Draw")
            elif (ran == "Rock" and players == "Paper") or (ran == "Paper" and players == "Scissor") or (ran == "Scissor" and players == "Rock"):
                print("win")    
            elif (ran == "Rock" and players == "Scissor") or (ran == "Paper" and players == "Rock") or (ran == "Scissor" and players == "Paper"):
                print("loose")   
            else:
                print("Error")
        except:
            print("Invalid Input")


main()