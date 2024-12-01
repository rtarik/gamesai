import pygame
from tictactoe.env.tictactoe_env import TicTacToeEnv

class TicTacToeGUI:
    def __init__(self):
        pygame.init()
        self.env = TicTacToeEnv()
        self.screen_size = 300
        self.cell_size = self.screen_size // 3
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption("Tic Tac Toe")
        self.font = pygame.font.Font(None, 100)
        self.running = True

    def draw_board(self):
        """
        Draw the game board and current state.
        """
        self.screen.fill((255, 255, 255))
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.cell_size, 0), (i * self.cell_size, self.screen_size), 3)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.cell_size), (self.screen_size, i * self.cell_size), 3)

        for i, cell in enumerate(self.env.board):
            x = (i % 3) * self.cell_size + self.cell_size // 2
            y = (i // 3) * self.cell_size + self.cell_size // 2
            if cell == 'X':
                text = self.font.render('X', True, (255, 0, 0))
                self.screen.blit(text, text.get_rect(center=(x, y)))
            elif cell == 'O':
                text = self.font.render('O', True, (0, 0, 255))
                self.screen.blit(text, text.get_rect(center=(x, y)))

    def handle_click(self, pos):
        """
        Handle a mouse click event.
        """
        if self.env.done:
            self.env.reset()
            return

        col = pos[0] // self.cell_size
        row = pos[1] // self.cell_size
        action = row * 3 + col

        state, reward, done = self.env.step(action)
        self.env.done = done
        if done:
            print("Game Over!")
            if self.env.winner:
                print(f"Winner: {self.env.winner}")
            else:
                print("It's a draw!")

    def run(self):
        """
        Main game loop.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.draw_board()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    gui = TicTacToeGUI()
    gui.run()
