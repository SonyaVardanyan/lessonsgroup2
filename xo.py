#!/usr/bin/python3
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                moves.append((row, col))
    return moves

def get_computer_move(board):
    return random.choice(get_available_moves(board))

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to XO Game!")
    print_board(board)
    
    while True:
        row = int(input(f"Player {current_player}, choose row (0-2): "))
        col = int(input(f"Player {current_player}, choose column (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_full(board):
                print("It's a draw!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Try again.")

def main():
    print("Welcome to XO Game!")
    player_choice = input("Do you want to play against the computer or another person? (computer/person): ").lower()
    
    if player_choice == "computer":
        play_game_with_computer()
    elif player_choice == "person":
        play_game()
    else:
        print("Invalid choice. Please enter 'computer' or 'person'.")

def play_game_with_computer():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to XO Game against the computer!")
    print_board(board)
    
    while True:
        if current_player == "X":
            row = int(input("Player X, choose row (0-2): "))
            col = int(input("Player X, choose column (0-2): "))
        else:
            row, col = get_computer_move(board)
        
        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            
            if check_winner(board, current_player):
                if current_player == "X":
                    print("Player X wins!")
                else:
                    print("Computer wins!")
                break
            elif is_full(board):
                print("It's a draw!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    main()
