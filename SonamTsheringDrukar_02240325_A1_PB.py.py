#GAME1
def guess_number_game():
    number_to_guess = 17 

    while True:
        your_guess = input("Wai charo, Guess a number between 1 and 20: ")  
        your_guess = int(your_guess) 
        if your_guess == number_to_guess:  
            print("you won!!!!!")
            break  
        else:
            print("you are stupid!")
            
guess_number_game()

#GAME2
import random
def game():
    print("Rock Paper Scissors")
    c = ["rock", "paper", "scissors"]
    while True:
        u = input("rock, paper, or scissors? ")
        if u == "quit":
            print("bye")
            break
        if u not in c:
            print("invalid, try again")
            continue
        comp = random.choice(c)
        print("computer chose", comp)
        if u == comp:
            print("Tie")
        elif (u == "rock" and comp == "scissors") or (u == "paper" and comp == "rock") or (u == "scissors" and comp == "paper"):
            print("You win")
        else:
            print("Computer wins")
game()