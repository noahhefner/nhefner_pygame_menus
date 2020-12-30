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
from menus import MenuManager, Page, ButtonText, ButtonPicture, Picture

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
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

    # Create the menu manager
    man = MenuManager(screen, clock)

    # Create some pages
    home = Page("home")
    page2 = Page("page2")
    page3 = Page("page3")
    page4 = Page("page4")

    # Add the pages to the menu manager
    man.add_page(home)
    man.add_page(page2)
    man.add_page(page3)
    man.add_page(page4)

    # Font that we use for text buttons
    font = pygame.font.SysFont("C059", 40)

    # Creating some text buttons
    b_home_p2 = ButtonText("PAGE2", font, pos = [200, 10], background_color = BLUE)
    b_home_p3 = ButtonText("PAGE3", font, pos = [200, 100], background_color = GREEN)
    b_p2_p4 = ButtonText("PAGE4", font, pos = [10, 10])
    b_p4_home = ButtonText("HOME", font, pos = [10, 10])

    # Creating an picture button
    b_play = ButtonPicture("button_play.png", pos = [0, 0])

    # Create a regular picture (not a button)
    picture_ship = Picture("player_white.png", pos =  [500, 500])

    # Adding actions to the text buttons
    b_home_p2.add_action(man.navigate, "page2")
    b_home_p3.add_action(man.navigate, "page3")
    b_p2_p4.add_action(man.navigate, "page4")
    b_p4_home.add_action(man.navigate, "home")

    # Add an action to the picture button
    b_play.add_action(man.exit_menu)

    # Adding buttons to the pages
    home.add_element(b_home_p2)
    home.add_element(b_home_p3)
    home.add_element(b_play)
    home.add_element(picture_ship)
    page2.add_element(b_p2_p4)
    page4.add_element(b_p4_home)

    # Setting the start page
    man.set_start_page("home")

    # Run the menu manager
    man.run()

if __name__ == "__main__":

    main()
