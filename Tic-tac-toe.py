'''The board is made using dictionary in which keys are
   the location and initially their values are empty and after every move
   the program changes the values according to user's choice of move.'''

board={"7":" ", "8":" ", "9":" ",
       "4":" ", "5":" ", "6":" ",
       "1":" ", "2":" ", "3":" "}

'''To print the updated board after every move in the game and thus making
    a function, board_print so that we can easily print the board 
    everytime by calling this function. '''

def board_print(board):
    print(board["7"] + " |" + board["8"] + " |" + board["9"])
    print("--+--+--")
    print(board["4"] + " |" + board["5"] + " |" + board["6"])
    print("--+--+--")
    print(board["1"] + " |" + board["2"] + " |" + board["3"])

#Main function which has all the gameplay functionality.
def game():

    turn="X"
    count = 0

    '''After taking input from the user, check if the input is a valid move or not.
       If the block that user requests to move to is valid,
       fill that block else ask the user to choose another block.'''

    for i in range(9):
        board_print(board)
        print(f"\nNow it is your turn {turn}. Tell me which place you want to move.")
        move=input( )

        if board[move]==" ":
            board[move]= turn
            count +=1
        else:
            print("This place is already filled!!\nPlease choose a different place.")
            continue

        #To check if player X or O has won,for every move after 5 moves.
        if count>=5:
            if board['7'] == board['8'] == board['9'] != ' ':   #across the top
                board_print(board)
                print("\nGame Over.\n")
                print(f"Hurray!! {turn} won.")
                break
            elif board['4'] == board['5'] == board['6'] != ' ': #across the middle
                board_print(board)
                print("\nGame Over.\n")
                print(f"Hurray!! {turn} won.")
                break
            elif board['1'] == board['2'] == board['3'] != ' ': #across the bottom
                board_print(board)
                print("\nGame Over.\n")
                print(f"Hurray!! {turn} won.")
                break
            elif board['1'] == board['4'] == board['7'] != ' ': #down the left side
                board_print(board)
                print("\nGame Over.\n")
                print(f"Hurray!! {turn} won.")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': #down the middle
                board_print(board)
                print("\nGame Over.\n")
                print(f"Hurray!! {turn} won.")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': #down the right side
                board_print(board)
                print("\nGame Over.\n")
                print(f"Hurray!! {turn} won.")
                break
            elif board['7'] == board['5'] == board['3'] != ' ': #diagonal
                board_print(board)
                print("\nGame Over.\n")
                print(f"Hurray!! {turn} won.")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': #diagonal
                board_print(board)
                print("\nGame Over.\n")
                print(f"Hurray!! {turn} won.")
                break

        #If neither X nor O wins and the board is full, the result will be 'tie'.
        if count==9:
            print("\nGame Over.\n")
            print("It\'s a tie!!!")

        #To change the player after every move.
        if turn=="X":
            turn="O"
        else:
            turn="X"


    board_keys = []

    for key in board:
        board_keys.append(key)

    #To ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
           board[key] = " "     #clean the grid for new match

        game()

game()

