# Tic-Tac-Toe Game

**Simple Tic-Tac-Toe project** with a graphical interface and both single-player (with AI) and two-player modes.

---

##  Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Running](#installation--running)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Game Modes](#game-modes)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License & Credits](#license--credits)

---

## About
This is a basic Tic-Tac-Toe game written in Python, featuring a user-friendly GUI made with `tkinter`, AI-driven single-player mode using the Minimax algorithm, and a networked two-player mode via sockets for local multiplayer.

---

## Features
- **Single-player mode** with three difficulty levels: *easy*, *medium*, *hard*
- AI that uses the **Minimax algorithm** for optimal moves in hard mode
- **Hints** option to suggest ideal moves to the player
- **Restart game** functionality
- **Multiplayer mode**: play with another user over a local network
- Simple graphical interface using **tkinter**

---

## Tech Stack
- **Python 3**
- **tkinter** for GUI
- Standard **socket** and **threading** libraries for multiplayer

---

## Getting Started

### Prerequisites
- Install **Python 3.x**
- (Optional) For virtual environments:
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # or `venv\Scripts\activate` on Windows


Installation & Running

Clone the repo:

git clone https://github.com/NickChronis2004/tic_tac_toe_game.git
cd tic_tac_toe_game


Run the main script and choose mode:

python main.py


For multiplayer:

Start the server:

python server.py


In two separate terminals or devices (connected to same Wi‑Fi):

python client.py



Usage

In single-player mode:

Select difficulty, play against AI.

Use Hint for best move suggestion.

Restart anytime.

In multiplayer mode:

One instance runs the server.

Other(s) connect via client script.

Game progresses turn by turn with score tracking.

Project Structure
.
├── main.py               # Entry point with GUI selector
├── singleplayer_mode.py  # Game logic & AI for single-player
├── server.py             # Networking logic for multiplayer server
└── client.py             # Networking and GUI for client

Highlights

singleplayer_mode.py: difficulty toggles, board updates, win/draw detection, Minimax AI, hint function

server.py: handles client communication, turn management, win tracking

client.py: GUI interaction, messaging, score updates, game reset, cleanup on exit

Future Enhancements

Add AI with variable strategies (e.g. Monte Carlo, Q‑learning)

Enable online multiplayer over internet

Improve GUI appearance and add animations or sound effects

Include logging and automated tests

Contributing

Contributions are welcome. For example:

Report issues or suggest enhancements

Tidy code or add new features

Submit pull requests with clear change descriptions

License & Credits

Written by Nikolaos Chronis, June 2024.

No external libraries beyond Python standard library.
