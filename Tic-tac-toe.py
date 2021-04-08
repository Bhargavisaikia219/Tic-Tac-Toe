board={"7":" ", "8":" ", "9":" ",
       "4":" ", "5":" ", "6":" ",
       "1":" ", "2":" ", "3":" "}

def board_print(board):
    print(board["7"] + " |" + board["8"] + " |" + board["9"])
    print("--+--+--")
    print(board["4"] + " |" + board["5"] + " |" + board["6"])
    print("--+--+--")
    print(board["1"] + " |" + board["2"] + " |" + board["3"])

def game():
    turn="X"
    count = 0

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

        if turn=="X":
            turn="O"
        else:
            turn="X"
game()

