import tkinter as tk
import tkinter.messagebox as mb

player1_score = 0
player2_score = 0

def check_win(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def check_tie(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True

def button_click(row, col):
    global current_player, player1_score, player2_score
    if board[row][col] == "":
        board[row][col] = current_player
        button[row][col].config(text=current_player)

        winner = check_win(board)
        if winner:
            if winner == "X":
                player1_score += 1
            else:
                player2_score += 1
            mb.showinfo("Game Over", f"Player {winner} wins!")
            disable_buttons()
            reset_game()
        elif check_tie(board):
            mb.showinfo("Game Over", "It's a tie!")
            disable_buttons()
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def disable_buttons():
    for row in range(3):
        for col in range(3):
            button[row][col].config(state=tk.DISABLED)

def reset_game():
    global board, current_player
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            button[row][col].config(text="", state=tk.NORMAL)

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [["", "", ""], ["", "", ""], ["", "", ""]]
current_player = "X"
button = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        button[row][col] = tk.Button(root, text="", width=6, height=2, command=lambda r=row, c=col: button_click(r, c))
        button[row][col].grid(row=row, column=col)

score_label = tk.Label(root, text=f"Player X: {player1_score} - Player O: {player2_score}")
score_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
