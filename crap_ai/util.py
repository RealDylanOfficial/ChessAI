# import requests


DEFAULT_WEBSERVER = "http://127.0.0.1:5000" # Default port for localhost 


def convert_to_fen(board): # Converts to Forsyth–Edwards Notation such that the read piece is equal to the piece name in FEN, FEN Notation: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    piece_conversion = {
        "BK": "k",
        "BQ": "q",
        "BB": "b",
        "BN": "n",
        "BR": "r",
        "BP": "p",
        "WK": "K",
        "WQ": "Q",
        "WB": "B",
        "WN": "N",
        "WR": "R",
        "WP": "P"
    } # Dictionary of values such that each piece on the server board 

    fen = ""
    for x in range(8): # Iterates through each row 
        count = 0
        for y in range(8): # Iterates through each column piece in the current row 
            if board[x][y] in ("..", "--", "??"): # If board has any of these values (not represented as pieces) it will add one to the count, which is added to the string in accordance to FEN notation
                count += 1
            elif count > 0:
                fen += str(count) # Once a represented piece is reached, add the number of empty spaces to the fen string
                fen += piece_conversion.get(board[x][y]) # Add the piece conversion representation to the string.
                count = 0 # Resets count to begin counting again
            else:
                fen += piece_conversion.get(board[x][y]) # If there are no empty spaces, places the next piece 
        if count > 0:
            fen += str(count)
        if x != 7:
            fen += "/"

    fen += " b KQkq - 0 1"
    return fen
