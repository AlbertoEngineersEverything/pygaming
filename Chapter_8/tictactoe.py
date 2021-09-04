#!C:\Users\Alberto\AppData\Local\Programs\Python\Python38\python

# Program:  Tic-Tac-Toe game
# Author:   Sloan Kelly (Originally)

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

current_token = 'X'
winning_token = ''
slots_filled = 0

print('Tic-Tac-Toe by Sloan Kelly')
print("Match three lines vertically, horizontally or diagonally.")
print("X goes first, then O goes second.")

while (winning_token == '') and (slots_filled < 9):
    print("\n")
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print('====='*15)

    pos = -1
    while pos == -1:
        pos = int(input(f"{current_token}'s turn. Where to? : "))
        if pos < 1 or pos > 9:
            pos = -1
            print("Invalid choice!  1-9 only.")

        pos = pos - 1

        if board[pos] == 'X' or board[pos] == 'O':
            print(f"That spot has already been taken by {board[pos]}===> TRY AGAIN")
            pos = -1

    board[pos] = current_token
    slots_filled += 1

    row1 = board[0] == current_token and board[1] == current_token and board[2] == current_token
    row2 = board[3] == current_token and board[4] == current_token and board[5] == current_token
    row3 = board[6] == current_token and board[7] == current_token and board[8] == current_token

    col1 = board[0] == current_token and board[3] == current_token and board[6] == current_token
    col2 = board[1] == current_token and board[4] == current_token and board[7] == current_token
    col3 = board[2] == current_token and board[5] == current_token and board[8] == current_token

    dia1 = board[0] == current_token and board[4] == current_token and board[8] == current_token
    dia2 = board[2] == current_token and board[4] == current_token and board[6] == current_token

    row = row1 or row2 or row3
    col = col1 or col2 or col3
    dia = dia1 or dia2

    if row or col or dia:
        print("\n")
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print("-+-+-")
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print("-+-+-")
        print(f"{board[6]}|{board[7]}|{board[8]}")

        print("\n")
        print(f"Congratulations {current_token}!  You WON!!")
        winning_token = current_token

    if current_token == 'X':
        current_token = 'O'
    else:
        current_token = 'X'

    if slots_filled == 9 and winning_token == '':
        print("Nobody won.  Better luck next time.")

