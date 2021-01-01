"""
Noah Hefner
Pygame Menu System Test Script
Last Edit: 1 January 2021

Theres not really a good way to write a test script for these modules, so I
essentially just tried to test all the functionality I could with a simple menu
system implementation.

Run the update_dist.sh script to copy the contents of test_menus.py to
nhefner_pygame_menus/menus.py.
"""

# Imports
import pygame
from menus_dev import MenuManager, Page, ButtonText, ButtonPicture, Picture, Text

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
    font = pygame.font.SysFont("Ubuntu-B", 60)

    # Create the menu manager
    man = MenuManager(screen, clock, background_color = [0, 0, 0])

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

    start_button = ButtonPicture("images/button_play.png", pos = [10, 300])
    char_select_button = ButtonText("SELECT CHARACTER", font, pos = [10, 400],
                                    color = [255, 0, 0])
    quit_button = ButtonText("QUIT", font, pos = [10, 500],
                             color = [255, 0, 0])
    coin = Picture("images/coin.png")
    dims = coin.get_dimensions()
    coin.set_pos([SCREEN_WIDTH - 10 - dims[0], SCREEN_HEIGHT - 10 - dims[1]])

    # Add actions to home elements
    char_select_button.add_action(man.navigate, "character_select")
    quit_button.add_action(man.kill_program)

    # Character select elements
    back_button = ButtonText("BACK", font, pos = [10, 10])

    # Add actions to character select elements
    back_button.add_action(man.navigate, "home")

    # Add elements to each page
    home.add_element(game_title)
    home.add_element(start_button)
    home.add_element(char_select_button)
    home.add_element(quit_button)
    home.add_element(coin)

    character_select.add_element(back_button)

    # Setting the start page
    man.set_start_page("home")

    # Run the menu manager
    man.run()

if __name__ == "__main__":

    main()
    pygame.quit()
