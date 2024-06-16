import socket
import threading
import tkinter as tk
from tkinter import messagebox

play_count = 0

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text']
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']
    return None

def receive_messages():
    global my_turn
    global x_wins
    global o_wins
    global play_count
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.startswith('MOVE'):
                symbol, row, col = message[4], int(message[5]), int(message[6])
                buttons[row][col].config(text=symbol)
                winner = check_winner()
                if winner:
                    if winner == 'X':
                        x_wins += 1
                    else:
                        o_wins += 1
                    update_score()
                    messagebox.showinfo("Info", f"Player {winner} wins!")
                    play_count = 0  # Reset play count when a game ends
                elif all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
                    messagebox.showinfo("Info", "It's a draw!")
                    play_count = 0  # Reset play count when a game ends
                my_turn = not my_turn
            elif message == 'RESET':
                play_count += 1
                if play_count == 2:
                    clear_board()
                    play_count = 0
            elif message.startswith('SCORE'):
                _, x_wins, o_wins = message.split(':')
                x_wins = int(x_wins)
                o_wins = int(o_wins)
                update_score()
            else:
                messagebox.showinfo("Info", message)
        except:
            break

def send_move(row, col):
    global my_turn
    if my_turn:
        move = f"MOVE{symbol}{row}{col}"
        buttons[row][col].config(text=symbol)
        client_socket.send(move.encode('utf-8'))
        my_turn = False

def on_button_click(row, col):
    if buttons[row][col].cget("text") == "" and my_turn:
        send_move(row, col)

def reset_game():
    client_socket.send(b'RESET')

def clear_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

def create_play_button():
    play_button = tk.Button(root, text="Play", font='Arial 20', width=10, height=2, command=reset_game)
    play_button.grid(row=4, column=0, columnspan=3)

def update_score():
    score_label.config(text=f"Player X Wins: {x_wins} | Player O Wins: {o_wins}")

def on_closing():
    client_socket.close()
    root.destroy()

# Setup the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9999))
symbol = client_socket.recv(1024).decode('utf-8')[-1]
my_turn = (symbol == 'X')
x_wins = 0
o_wins = 0

# Setup the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font='Arial 20', width=5, height=2,
        command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

score_label = tk.Label(root, text="Player X Wins: 0 | Player O Wins: 0", font='Arial 15')
score_label.grid(row=3, column=0, columnspan=3)

create_play_button()

root.protocol("WM_DELETE_WINDOW", on_closing)

threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()
client_socket.close()
