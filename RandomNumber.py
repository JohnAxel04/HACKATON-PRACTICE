import random


randomNum = random.randint(1,10)

counter = 0
while True:

        inp = int(input("Guess the Number(1-1): "))
        if inp not in range(1,11):
            print("exceed to the limit")
        elif inp > randomNum:
            print("You guess too high")
        elif inp < randomNum:
            print("You guess too low")
        elif inp == randomNum:
            print(f"Congratulations, Taken {counter} trys")
            break
        
        counter += 1
