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
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True  # True if it's white's turn, False if black
        self.moveLog = []  # List to keep track of moves made
        self.checkmate = False
        
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"  # Remove piece from start square
        self.board[move.endRow][move.endCol] = move.pieceMoved  # Place piece on end square
        self.moveLog.append(move)  # Add move to the log if an undo is made
        self.whiteToMove = not self.whiteToMove  # Switch turns
        
class Move():
    
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3,
                   "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToRows = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToRows.items()}
    
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) +  self.getRankFile(self.endRow, self.endCol)  
    def getRankFile(self,r, c):
       return self.colsToFiles[c] + self.rowsToRanks[r]