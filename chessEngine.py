""" 
Responsible for the chess engine logic.
Contains classes and functions to handle game rules, piece movements, and game state.
Also will keep track of the game history and allow for undo/redo functionality.
"""

class GameState:
    def __init__(self):
        # 8x8 board representation
        # Each piece is represented by a two-character string: color + type
        # Empty squares are represented by "--"
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bK", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wK", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True  # True if it's white's turn, False if black
        self.moveLog = []  # List to keep track of moves made
        self.checkmate = False  # True if the game is in checkmate
        