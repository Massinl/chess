""" 
Main driver for the chess game.
This file initializes the game, sets up the board, and starts the main loop.
"""


import pygame as p
import chessEngine

WIDTH = HEIGHT = 512  # 512x512 pixels
DIMENSION = 8  # Chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION  # Size of each square
MAX_FPS = 15  # For animations
IMAGES = {}  # Dictionary to hold images of pieces

"""
Initialize a global dictionary to hold images of pieces.
This function loads images from the 'images' directory and scales them to fit the square size
"""
def loadImages():
    """Load images for the chess pieces."""
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bP", "wR", "wN", "wB", "wQ", "wK", "wP"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))
        # Remember we can access images by IMAGES["bR"] same for all pieces

""" 
 Main function to run the chess game. 
"""

def main():
    p.init()  # Initialize Pygame
    screen = p.display.set_mode((WIDTH, HEIGHT))  # Set the window size
    clock = p.time.Clock()  # Create a clock to control the frame rate
    screen.fill(p.Color("white"))  # Fill the screen with white color
    gs = chessEngine.GameState()  # Create a new game state
    loadImages()  # Load images of chess pieces
    running = True  # Game loop control variable
    sqSelected = ()  # Keep track of last click of the user
    playerClicks = []  # List to keep track of player clicks (two tuples)
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # Get the mouse click position
                column = location[0] // SQ_SIZE  
                row = location[1] // SQ_SIZE  
                if sqSelected == (row, column): # If the same square is clicked again
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, column)  
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:  # If two squares are selected
                   move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)  # Create a move object
                   print(move.getChessNotation()) 
                   gs.makeMove(move)  
                   sqSelected = ()
                   playerClicks = []  
                
        drawGameState(screen, gs)  # Draw the current game state
        clock.tick(MAX_FPS)  # Control the frame rate
        p.display.flip()  # Update the display
        
def drawGameState(screen, gs):
        drawBoard(screen)  # Draw the chess board
        drawPieces(screen, gs.board)  # Draw the pieces on the board

"""
Draw the chess board on the screen.
"""
def drawBoard(screen):
    colors = [p.Color("grey"), p.Color("navy")]  # Define colors for the squares
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE , SQ_SIZE, SQ_SIZE))  # Draw each square

""" 
Draw the pieces on the board.
"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]  # Get the piece at the current square
            if piece != "--":  # If there is a piece
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))  # Draw the piece on the square
                
if __name__ == "__main__":
    main()  # Call the main function to start the game
    
