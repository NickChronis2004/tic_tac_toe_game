import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

def start_singleplayer():
    root.destroy()
    run_singleplayer()
    
def start_multiplayer():
    root.destroy()
    run_multiplayer()

def run_singleplayer():
    # Place the singleplayer game code here
    import singleplayer_mode
    singleplayer_mode.run()

def run_multiplayer():
    # Place the multiplayer game code here
    subprocess.run([sys.executable, 'server.py'])

root = tk.Tk()
root.geometry("300x200")
root.title("Tic Tac Toe")

singleplayer_button = tk.Button(root, text="Singleplayer", command=start_singleplayer, height=2, width=20)
singleplayer_button.pack(pady=20)

multiplayer_button = tk.Button(root, text="Multiplayer", command=start_multiplayer, height=2, width=20)
multiplayer_button.pack(pady=20)

root.mainloop()