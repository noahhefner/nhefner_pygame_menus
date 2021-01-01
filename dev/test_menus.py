"""
Noah Hefner
Pygame Menu System Test Script
Last Edit: 30 December 2020

Theres not really a good way to write a test script for these modules, so I
essentially just tried to test all the functionality I could with a simple menu
system implementation.
"""

# Imports
import pygame
from menus import MenuManager, Page, ButtonText, ButtonPicture, Picture, Text

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_CENTER_X = SCREEN_WIDTH / 2
SCREEN_CENTER_Y = SCREEN_HEIGHT / 2
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]

def main ():
    """
    Tests all the classes in nhefner_pygame_menus.
    """

    # Initialize pygame
    pygame.init()

    # Window stuff
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    pygame.display.set_caption('Pygame Module Testing')

    # Font that we use for text buttons
    font = pygame.font.SysFont("C059", 40)

    # Create the menu manager
    man = MenuManager(screen, clock)

    # Create some pages
    home = Page("home")
    character_select = Page("character_select")

    # Add the pages to the menu manager
    man.add_page(home)
    man.add_page(character_select)

    # Home elements
    game_title = Text("GAME TITLE HERE", font)
    dims = game_title.get_dimensions()
    game_title.set_pos([SCREEN_CENTER_X - (dims[0] / 2), 20])

    # Add elements to each page
    home.add_element(game_title)

    # Setting the start page
    man.set_start_page("home")

    # Run the menu manager
    man.run()

if __name__ == "__main__":

    main()
