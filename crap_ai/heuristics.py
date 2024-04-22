# MIT License

# Copyright (c) 2016 James Lim

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

import chess

def material(board_state: chess.Board, weight):
    black_points = 0
    # board_state = board_state.split()[0]
    piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 0}
    pieces = board_state.piece_map()
    symbols = []
    
    for x in pieces.values():
        symbols.append(x.symbol())
    for piece in symbols:
        piece: chess.Piece
        if piece.islower():
            black_points += piece_values[piece]
        elif piece.isupper():
            black_points -= piece_values[piece.lower()]
    return black_points * weight

def piece_moves(game: chess.Board, weight):
    black_points = 0
    turn = game.turn
    square_values = {"e4": 1, "e5": 1, "d4": 1, "d5": 1, "c6": 0.5, "d6": 0.5, "e6": 0.5, "f6": 0.5,
                    "c3": 0.5, "d3": 0.5, "e3": 0.5, "f3": 0.5, "c4": 0.5, "c5": 0.5, "f4": 0.5, "f5": 0.5}
    possible_moves = game.legal_moves
    for move in possible_moves:
        if turn == chess.BLACK:
            if move.uci()[2:4] in square_values:
                black_points += square_values[move.uci()[2:4]]
        else:
            if move.uci()[2:4] in square_values:
                black_points -= square_values[move.uci()[2:4]]

    return black_points * weight

def pawn_structure(board_state: chess.Board, weight):
    black_points = 0
    board_state = str(board_state)

    # convert fen into matrix:
    board_state_arr = []
    for row in board_state:
        row_arr = []
        for char in row:
            if char.isdigit():
                for i in range(int(char)):
                    row_arr.append(" ")
            else:
                row_arr.append(char)
        board_state_arr.append(row_arr)

    # determine pawn to search for based on whose turn it is
    for i, row in enumerate(board_state_arr):
        for j in range(len(row)):
            if board_state_arr[i][j] == "p":
                tl = i-1, j-1
                tr = i-1, j+1
                if tl[0] >= 0 and tl[0] <= 7 and tl[1] >= 0 and tl[1] <= 7:
                    if board_state_arr[tl[0]][tl[1]] == "p":
                        black_points += 1
                if tr[0] >= 0 and tr[0] <= 7 and tr[1] >= 0 and tr[1] <= 7:
                    if board_state_arr[tr[0]][tr[1]] == "p":
                        black_points += 1
    return black_points * weight

def in_check(game: chess.Board, weight):
    black_points = 0
    # Turn should be 'w' or 'b'
    if game.turn == chess.WHITE: turn = "w"
    else: turn = "b"
    # Check or Checkmate situations
    if turn == "w":
        if game.is_checkmate():
            black_points += float("inf")
        elif game.is_check():
            black_points += 1 * weight
    else:
        if game.is_checkmate():
            black_points += float("-inf")
        elif game.is_check():
            black_points -= 1 * weight
            
    return black_points

# def center_squares(game, weight):
#     black_points = 0
#     # inner center squares - e4, e5, d4, d5
#     inner = [game.board.get_piece(game.xy2i("e4")),
#             game.board.get_piece(game.xy2i("e5")),
#             game.board.get_piece(game.xy2i("d4")),
#             game.board.get_piece(game.xy2i("d5"))]
#     for square in inner:
#         if square.islower():
#             black_points += 3
#     # outer center squares - c3, d3, e3, f3, c6, d6, e6, f6, f4, f5, c4, c5
#     outer = [game.board.get_piece(game.xy2i("c3")),
#             game.board.get_piece(game.xy2i("d3")),
#             game.board.get_piece(game.xy2i("e3")),
#             game.board.get_piece(game.xy2i("f3")),
#             game.board.get_piece(game.xy2i("c6")),
#             game.board.get_piece(game.xy2i("d6")),
#             game.board.get_piece(game.xy2i("e6")),
#             game.board.get_piece(game.xy2i("f6")),
#             game.board.get_piece(game.xy2i("f4")),
#             game.board.get_piece(game.xy2i("f5")),
#             game.board.get_piece(game.xy2i("c4")),
#             game.board.get_piece(game.xy2i("c5"))]
#     for square in outer:
#         if square.islower():
#             black_points += 1
#     return black_points * weight
