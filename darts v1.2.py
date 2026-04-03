#--------------------------
#name: Nootguin
#date: 28.01.26
#title: Darts v1.2
#--------------------------

import time # Import time to make closing the program via quit more user friendly

def game():
    p1total = 501
    p2total = 501
    player = "Player 1" # sets player to player 1
    while p1total > 0 or p2total > 0: # 
        if player == "Player 1": # if the player is player 1 then
            p1total = turn(p1total,player) # passes the function and sets the returned value
            print("This is the current score left for Player 1 = ",p1total) # prints total player 1 score left
            if p1total == 0: # player 1 win condition
                print("Player 1 Wins!")
                playagain()
                break # breaks the while loop
            player = "Player 2" # changes turn
        elif player == "Player 2": # if the player is player 2 then
            p2total = turn(p2total,player) # passes the function and sets the returned value
            print("This is the current score left for Player 2 = ",p2total) # prints total player 2 score left
            if p2total == 0: # player 2 win condition
                print("Player 2 Wins!")
                playagain()
                break # breaks the while loop
            player = "Player 1" # changes turn
    
def menu(): 
    print("""
    1. Start Game
    2. How to Play - Rules
    3. Quit
    """)
    menu_select = (input("Enter: ")).strip(" ") # asks the user to enter a number to select an option
    if menu_select == "3": # closes program if 3 was selected
        print("Closing the game...")
        quit(time.sleep(3)) # takes 3 seconds before closing program
    elif menu_select == "2": # prints rules of game if 2 was selected
        print("""
    1. Each player takes a turn in, throwing 3 darts.
    2. Each player starts at 501 score and each turn the tally of their three darts is taken away from their total.
    3. Scores that are less than 2 or add up below total score left are not counted.
    4. If any dart that misses or sticks into another dart it counts as a throw and gets no score.
    5. Whichever player reaches exactly zero first wins the game.
        """)
        game() # runs game procedure once rules have been outputed
    elif menu_select == "1":
        game() # runs game procedure if start game is chosen
    else: # if the user does not input 2 or 3 the menu outputs an error and reprompts the user
        print("ERROR - Ivalid input, please try again")
        menu()

def turn(x,y):
    try: # trys to set score as integar of input
        score = int(input(f"{y}. Please enter your score for this turn: "))
    except ValueError: # if value is not an integar it prints an error and asks again
        print("ERROR - Ivalid input, please try again")
        turn(x,y)
    if x < score: # if the player total is less than what they scored the score is not counted and the turn ends
        print("BUST, No Score!")
        return(x) # ends function and returns total
    elif score <= 2 or score > 180:
        print("Score not possible, No Score!")
        return(x)
    else:
        x = x-score # the score is taken away from the players current total
        return(x) # ends function and returns total

def playagain():
    again = input("Do you want to play again? y/n: ").lower().strip(" ") # makes the input lower case and strips any spaces
    if again == "y":
        print("Starting New game!")
        menu()
    elif again == "n":
        print("Closing the game...")
        quit(time.sleep(3)) # closes program if 3 was selected
    else:
        print("ERROR - Please input y or n.") # if input was not y or n then the program asks the question again
        playagain() 

print("Welcome to the Game!") # welcomes user to game
menu() # starts the menu












