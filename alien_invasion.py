# Creates the game instance and maintains global instance variables (title, background color, screen size, Etc.)

import sys

import pygame

class AlienInvasion:

    """ Overall class to manage game assets and behavior. """
    def __init__(self):
        """ Initialize the game, and create game resources. """

        pygame.init()

        # Set the resolution/window size for the game
        self.screen = pygame.display.set_mode((1200, 800))

        # Set the title for the game
        pygame.display.set_caption('Alien Invasion')

        # Set the background color for the game surface
        self.bg_color = (0, 0, 0)

    def run_game(self):

        """ Start the main loop for the game. """
        while True:
            # Watch keyboard and mouse events.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':

    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()