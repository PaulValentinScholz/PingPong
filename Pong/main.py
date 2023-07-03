import pygame
from game import Game

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 1200
window_height = 900
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Paddle Ball Game")

# Create an instance of the game world
game = Game(window)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the game world
    game.update()

    # Render the game world
    game.render()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
