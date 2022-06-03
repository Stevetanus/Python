def validate_board(board_dict):
    # check for one black and one white king
    if 'bking' not in board_dict.values() or 'wking' not in board_dict.values():
        return False
    bking = 0
    wking = 0
    for king in board_dict.values():
        if king == 'bking':
            bking += 1
        if king == 'wking':
            wking += 1
    if bking > 1 or wking > 1:
        return False

    # check for a maximum of 16 pieces per player
    white_player = 0
    black_player = 0
    for item in board_dict.values():
        if item[0] == 'w':
            white_player += 1
        elif item[0] == 'b':
            black_player += 1
    if black_player >= 17 or white_player >= 17:
        return False

    # check for at most 8 pawns per player
    white_pawn = 0
    black_pawn = 0
    for p in board_dict.values():
        if p == 'bpawn':
            black_pawn += 1
        elif p == 'wpawn':
            white_pawn += 1
    if white_pawn > 8 or black_pawn > 8:
        return False
    # check for a valid location
    board_keys = {'a1': '', 'a2': '', 'a3': '', 'a4': '', 'a5': '', 'a6': '', 'a7': '', 'a8': '',
                  'b1': '', 'b2': '', 'b3': '', 'b4': '', 'b5': '', 'b6': '', 'b7': '', 'b8': '',
                  'c1': '', 'c2': '', 'c3': '', 'c4': '', 'c5': '', 'c6': '', 'c7': '', 'c8': '',
                  'd1': '', 'd2': '', 'd3': '', 'd4': '', 'd5': '', 'd6': '', 'd7': '', 'd8': '',
                  'e1': '', 'e2': '', 'e3': '', 'e4': '', 'e5': '', 'e6': '', 'e7': '', 'e8': '',
                  'f1': '', 'f2': '', 'f3': '', 'f4': '', 'f5': '', 'f6': '', 'f7': '', 'f8': '',
                  'g1': '', 'g2': '', 'g3': '', 'g4': '', 'g5': '', 'g6': '', 'g7': '', 'g8': '',
                  'h1': '', 'h2': '', 'h3': '', 'h4': '', 'h5': '', 'h6': '', 'h7': '', 'h8': ''}
    for v in board_dict.keys():
        if v not in board_keys.keys():
            return False

    # check if the name starts with a "w" or "b"
    for pieces in board_dict.values():
        if pieces[0] != "b" and pieces[0] != "w":
            return False

    # check if the piece name is valid
    piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for names in board_dict.values():
        if names[1:] not in piece_names:
            return False
    return True  # If the chess was valid its print True otherwise it will print None


print(validate_board({"h1": "bking", "c6": "wqueen",
                      "g2": "bbishop", "h5": "bqueen", "e3": "wking"}))  # True
print(validate_board({"a1": "bpawn", "a2": "wking"}))  # False: no bking
# False: cannot have 2 white kings, no bking
print(validate_board({"a1": "wking", "a2": "wking", "c3": "bbishop"}))
# False: z9 is an invalid position
print(validate_board({"a1": "bking", "z9": "wking"}))
print(validate_board({'a1': 'bking', 'a2': 'wking', 'h1': 'bpawn', 'h2': 'bpawn', 'h3': 'bpawn', 'h4': 'bpawn', 'h5': 'bpawn',
                      'h6': 'bpawn', 'h7': 'bpawn', 'h8': 'bpawn', 'g7': 'bpawn', 'g8': 'bpawn'}))  # False theres more than 8 pawns
# False: cannot have 2 white kings and 1 black king
print(validate_board(
    {"a1": "wking", "a2": "wking", "c3": "bbishop", "c4": "bking"}))
