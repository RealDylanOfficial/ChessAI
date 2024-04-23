import chess
import time
import requests
import json

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
    "..": "",
}

def getMove(ai, depth, board, move_label, time_label):
    # Generate move
    start_time = time.time()
    ai_move = ai.get_move(board, depth)
    move_label.config(text="Move: "+str(ai_move))
    time_label.config(text="Time: "+str(time.time()-start_time))
    # Send move to arm
    

def updateBoard(chess_tiles):
    # Get new board state
    SERVER = "http://10.205.38.238:5000/update_chessboard"
    
    response = requests.get(SERVER)

    if response.status_code == 200:
        chess_board = response.json()
    else:
        print("Board request failed. Status code: " + response.status_code)
        return
    
    PIECE_DICT = {"P_B":"BP", "P_W":"WP", "B_W":"WB", "B_B":"BB", "N_W":"WN", "N_B":"BN", "K_W":"WK", "K_B":"BK", "Q_B":"BQ", "Q_W":"WQ", "R_W":"WR", "R_B":"BR", "":"..", None:".."}
    ROWS = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g", 7:"h"}
    # chess_board = json.loads('{"a1": {"x": 40.0, "y": 30.0, "piece": ""}, "b1": {"x": 120.0, "y": 30.0, "piece": ""}, "c1": {"x": 200.0, "y": 30.0, "piece": ""}, "d1": {"x": 280.0, "y": 30.0, "piece": ""}, "e1": {"x": 360.0, "y": 30.0, "piece": ""}, "f1": {"x": 440.0, "y": 30.0, "piece": ""}, "g1": {"x": 520.0, "y": 30.0, "piece": ""}, "h1": {"x": 600.0, "y": 30.0, "piece": ""}, "a2": {"x": 40.0, "y": 90.0, "piece": ""}, "b2": {"x": 120.0, "y": 90.0, "piece": ""}, "c2": {"x": 40.0, "y": 30.0, "piece": "P_W"}, "d2": {"x": 280.0, "y": 90.0, "piece": ""}, "e2": {"x": 360.0, "y": 90.0, "piece": ""}, "f2": {"x": 40.0, "y": 30.0, "piece": "B_W"}, "g2": {"x": 520.0, "y": 90.0, "piece": ""}, "h2": {"x": 600.0, "y": 90.0, "piece": ""}, "a3": {"x": 40.0, "y": 30.0, "piece": "P_B"}, "b3": {"x": 120.0, "y": 150.0, "piece": ""}, "c3": {"x": 200.0, "y": 150.0, "piece": ""}, "d3": {"x": 280.0, "y": 150.0, "piece": ""}, "e3": {"x": 360.0, "y": 150.0, "piece": ""}, "f3": {"x": 440.0, "y": 150.0, "piece": ""}, "g3": {"x": 520.0, "y": 150.0, "piece": ""}, "h3": {"x": 600.0, "y": 150.0, "piece": ""}, "a4": {"x": 40.0, "y": 210.0, "piece": ""}, "b4": {"x": 40.0, "y": 30.0, "piece": "P_W"}, "c4": {"x": 200.0, "y": 210.0, "piece": ""}, "d4": {"x": 280.0, "y": 210.0, "piece": ""}, "e4": {"x": 40.0, "y": 30.0, "piece": "P_B"}, "f4": {"x": 440.0, "y": 210.0, "piece": ""}, "g4": {"x": 520.0, "y": 210.0, "piece": ""}, "h4": {"x": 600.0, "y": 210.0, "piece": ""}, "a5": {"x": 40.0, "y": 270.0, "piece": ""}, "b5": {"x": 120.0, "y": 270.0, "piece": ""}, "c5": {"x": 200.0, "y": 270.0, "piece": ""}, "d5": {"x": 280.0, "y": 270.0, "piece": ""}, "e5": {"x": 360.0, "y": 270.0, "piece": ""}, "f5": {"x": 440.0, "y": 270.0, "piece": ""}, "g5": {"x": 520.0, "y": 270.0, "piece": ""}, "h5": {"x": 600.0, "y": 270.0, "piece": ""}, "a6": {"x": 40.0, "y": 30.0, "piece": "K_W"}, "b6": {"x": 120.0, "y": 330.0, "piece": ""}, "c6": {"x": 40.0, "y": 30.0, "piece": "R_W"}, "d6": {"x": 280.0, "y": 330.0, "piece": ""}, "e6": {"x": 360.0, "y": 330.0, "piece": ""}, "f6": {"x": 440.0, "y": 330.0, "piece": ""}, "g6": {"x": 520.0, "y": 330.0, "piece": ""}, "h6": {"x": 600.0, "y": 330.0, "piece": ""}, "a7": {"x": 40.0, "y": 390.0, "piece": ""}, "b7": {"x": 40.0, "y": 30.0, "piece": "K_B"}, "c7": {"x": 200.0, "y": 390.0, "piece": ""}, "d7": {"x": 40.0, "y": 30.0, "piece": "N_B"}, "e7": {"x": 360.0, "y": 390.0, "piece": ""}, "f7": {"x": 40.0, "y": 30.0, "piece": "P_B"}, "g7": {"x": 520.0, "y": 390.0, "piece": ""}, "h7": {"x": 600.0, "y": 390.0, "piece": ""}, "a8": {"x": 40.0, "y": 450.0, "piece": ""}, "b8": {"x": 120.0, "y": 450.0, "piece": ""}, "c8": {"x": 200.0, "y": 450.0, "piece": ""}, "d8": {"x": 280.0, "y": 450.0, "piece": ""}, "e8": {"x": 360.0, "y": 450.0, "piece": ""}, "f8": {"x": 440.0, "y": 450.0, "piece": ""}, "g8": {"x": 520.0, "y": 450.0, "piece": ""}, "h8": {"x": 600.0, "y": 450.0, "piece": ""}}')
    new_board = [[],[],[],[],[],[],[],[]]
    
    for i in range(0, 8):
        for j in range(0, 8):
            row = ROWS[j]
            coords = (chess_board[row+str(i+1)]["x"], chess_board[row+str(i+1)]["y"])
            piece = chess_board[row+str(i+1)]["piece"]
            new_board[j].append(PIECE_DICT[piece])
        
    global board
    board = chess.Board(convert_to_fen(new_board))
    # new_board = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    # ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    # ["..", "..", "..", "..", "..", "..", "..", ".."],
    # ["..", "..", "..", "..", "..", "..", "..", ".."],
    # ["..", "..", "..", "..", "..", "..", "..", ".."],
    # ["..", "..", "..", "..", "..", "..", "..", ".."],
    # ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    # ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]
    
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

move_label = Label(tk, text="Move:")
move_label.pack(side="top")

time_label = Label(tk, text="Time:")
time_label.pack(side="top")

update_button = Button(tk, text="Update board", height="1", width="20", font=FONT, command=lambda: updateBoard(chess_tiles))
get_move_button = Button(tk, text="Generate move", height="1", width="20", font=FONT, command=lambda: getMove(alphabeta_ai, DEPTH, board, move_label, time_label))
update_button.pack(side="top")  # Placed the buttons on top
get_move_button.pack(side="top")



chess_tiles[(4, 3)].config(text="X")
tk.mainloop()