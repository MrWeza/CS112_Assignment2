# File: CS112_A1_T2_2_20230361
# Purpose: Each player has to pick a number from 0 to 9 
#          where each number can only be picked once by one of the players. 
#          the goal is to have 3 numbers that add up to 15
#          the first player to achieve this goal wins.
#          if no player has 3 numbers that add up to 15 and there are
#          no numbers left the game ends in a draw.   
# Author: Mohamed Waleed Osama
# ID: 20230361

print('Welcome to Number Scrabble game!')
input('Press Enter to Start')
Avlbl_Num=[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] # This is the list of the numbers that you can select from
Player1=[] # This is the list which player's 1 chosen numbers will append to
Player2=[] # This is the list which player's 2 chosen numbers will append to



def Player1_input():
    while True:
        try:
            Player1_num = int(input('Player 1, Please select a number: '))  # Take input from player 1
            if 1 <= Player1_num <= 9 and Player1_num in Avlbl_Num: # The boundary of the play should be between 1 and 9 and available in the Avlbl_Num
                Avlbl_Num.remove(Player1_num) # Chosen number is removed from AVlbl_Num
                Player1.append(Player1_num) # Chosen number is appended to Player's 1 list
                break
            else:
                print('The number is not in range or not available. Please select an available number.')
        except ValueError:
            print('Invalid input. Please enter a number.')




def Player2_input():

    while True:
        try:
            Player2_num = int(input('Player 2, Please select a number: ')) # The boundary of the play should be between 1 and 9 and available in the Avlbl_Num
            if 1 <= Player2_num <= 9 and Player2_num in Avlbl_Num: # Chosen number is removed from AVlbl_Num
                Avlbl_Num.remove(Player2_num) # Chosen number is removed from AVlbl_Num
                Player2.append(Player2_num) # Chosen number is appended to Player's 2 list
                break
            else:
                print('The number is not in range or not available. Please select an available number.')
        except ValueError:
            print('Invalid input. Please enter a number.')




def check_win(player):
    from itertools import combinations
    for combo in combinations(player, 3): # Checking all the possible combinations of three numbers in the player's list
        if sum(combo) == 15:
            return True
    return False



def game():
    while len(Avlbl_Num) > 0:
        print("\nAvailable Numbers:", Avlbl_Num)
        Player1_input()
        if check_win(Player1):
            print('\n***** PLAYER 1 IS THE WINNER *****\n')
            break
        Player2_input()
        if check_win(Player2):
            print('\n***** PLAYER 2 IS THE WINNER *****\n')
            break

game()


while True :
    print()
    Play_again = input('Play Again : Press Enter \nExit : Type E \n :')    
    print ()

    if Play_again.upper() == "E" :
        print()
        print("***** THANK YOU FOR PLAYING *****")
        break
    else :
        Avlbl_Num=[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        Player1=[]
        Player2=[]
      
        game()


    









































































































































