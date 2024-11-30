import pygame
import sys
from tictactoe.env.tictactoe_env import TicTacToeEnv

# Constants
WINDOW_SIZE = 600
GRID_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
LINE_WIDTH = 5
CIRCLE_COLOR = (242, 85, 96)
CROSS_COLOR = (28, 170, 156)
MARKER_WIDTH = 15

class TicTacToeGUI:
    def __init__(self):
        """
        Initialize the Pygame GUI for Tic Tac Toe and the environment.
        """
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        self.window.fill(BACKGROUND_COLOR)
        self.running = True
        self.env = TicTacToeEnv()
        self.cell_size = WINDOW_SIZE // 3
        self.font = pygame.font.Font(None, 74)

    def draw_grid(self):
        """
        Draw the Tic Tac Toe grid.
        """
        for x in range(1, 3):
            pygame.draw.line(self.window, GRID_COLOR, 
                             (x * self.cell_size, 0), 
                             (x * self.cell_size, WINDOW_SIZE), 
                             LINE_WIDTH)
        for y in range(1, 3):
            pygame.draw.line(self.window, GRID_COLOR, 
                             (0, y * self.cell_size), 
                             (WINDOW_SIZE, y * self.cell_size), 
                             LINE_WIDTH)

    def draw_markers(self):
        """
        Draw X's and O's on the board based on the environment state.
        """
        for i, cell in enumerate(self.env.state):
            x = (i % 3) * self.cell_size
            y = (i // 3) * self.cell_size
            if cell == 1:  # Player 1 (X)
                pygame.draw.line(self.window, CROSS_COLOR, 
                                 (x + 50, y + 50), 
                                 (x + self.cell_size - 50, y + self.cell_size - 50), 
                                 MARKER_WIDTH)
                pygame.draw.line(self.window, CROSS_COLOR, 
                                 (x + self.cell_size - 50, y + 50), 
                                 (x + 50, y + self.cell_size - 50), 
                                 MARKER_WIDTH)
            elif cell == -1:  # Player 2 (O)
                pygame.draw.circle(self.window, CIRCLE_COLOR, 
                                   (x + self.cell_size // 2, y + self.cell_size // 2), 
                                   self.cell_size // 3, 
                                   MARKER_WIDTH)

    def get_cell_index(self, pos):
        """
        Convert mouse position to board index.
        :param pos: (x, y) position of the mouse.
        :return: Index of the cell (0-8) or None if invalid.
        """
        x, y = pos
        row = y // self.cell_size
        col = x // self.cell_size
        return row * 3 + col

    def display_result(self, message):
        """
        Display the game result on the screen.
        """
        # Draw the final state before showing the message
        self.window.fill(BACKGROUND_COLOR)
        self.draw_grid()
        self.draw_markers()
        pygame.display.flip()  # Update the screen to show the last move

        # Display the result message
        text = self.font.render(message, True, (0, 0, 0))
        rect = text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
        self.window.blit(text, rect)
        pygame.display.flip()  # Update the screen to show the message

        # Add a delay to let the player see the final state
        pygame.time.wait(2000)

    def run(self):
        """
        Main loop for running the GUI.
        """
        self.env.reset()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.env.done:
                    cell_index = self.get_cell_index(event.pos)
                    if cell_index is not None:
                        _, reward, done = self.env.step(cell_index)
                        if done:
                            if reward == 1:
                                message = "Player X wins!" if self.env.current_player == 1 else "Player O wins!"
                            elif reward == 0:
                                message = "It's a draw!"
                            else:
                                message = ""  # No message for invalid moves
                            if message:
                                self.display_result(message)
                                self.env.reset()

            self.window.fill(BACKGROUND_COLOR)  # Clear the screen
            self.draw_grid()  # Draw the grid
            self.draw_markers()  # Draw X's and O's
            pygame.display.flip()  # Update the display



if __name__ == "__main__":
    gui = TicTacToeGUI()
    gui.run()
