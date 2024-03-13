import chess
import time
import requests

from crap_ai.ai import AI_AlphaBeta
from crap_ai.util import convert_to_fen

from tkinter import Canvas, Frame, Tk, Label, Button

# black is lowercase
board = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]

UNICODE_CHARS = {
    "BK": "♚",
    "BQ": "♛",
    "BB": "♝",
    "BN": "♞",
    "BR": "♜",
    "BP": "♟",
    "WK": "♔",
    "WQ": "♕",
    "WB": "♗",
    "WN": "♘",
    "WR": "♖",
    "WP": "♙",
    "..": ""
}

def getMove(ai, depth, board):
    # Generate move
    start_time = time.time()
    ai_move = ai.get_move(board, depth)
    
    # Send move to arm
    

def updateBoard(chess_tiles):
    # Get new board state
    url = "http://localhost:4576/chessboard"
    response = requests.get(url)

    if response.status_code == 200:
        chess_board = response.json()
    else:
        pass
    
    new_board = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]
    
    # Update UI
    for row in range(0, len(new_board)):
        for piece in range(0, len(new_board[0])):
            chess_tiles[(row, piece)].config(text=UNICODE_CHARS[new_board[row][piece]])

board = chess.Board(convert_to_fen(board))

alphabeta_ai = AI_AlphaBeta()


tk = Tk()
FONT = ("Comic Sans MS", tk.winfo_screenheight() // 30)
DEPTH = 4
canvas = Canvas(tk, width=tk.winfo_screenwidth()/2, height=tk.winfo_screenheight()/2)
canvas.pack(side="left")  # Adjusted the placement of canvas to the left

chess_tiles = {}

for y in range(8):
    for x in range(8):
        lab = Label(canvas, borderwidth="2", relief="groove", width=2, height=1, font=FONT)
        lab.grid(row=x, column=y)
        chess_tiles[(x, y)] = lab

board_stat = Label(canvas, text="Board State")

update_button = Button(tk, text="Update board", height="1", width="20", font=FONT, command=lambda: updateBoard(chess_tiles))
get_move_button = Button(tk, text="Generate move", height="1", width="20", font=FONT, command=lambda: getMove(alphabeta_ai, DEPTH, board))
update_button.pack(side="top")  # Placed the buttons on top
get_move_button.pack(side="top")



chess_tiles[(4, 3)].config(text="X")
tk.mainloop()