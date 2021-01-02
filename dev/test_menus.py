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
import time
import random

from menus_dev import MenuManager, Page, ButtonText, ButtonPicture, Picture, Text

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_CENTER_X = SCREEN_WIDTH / 2
SCREEN_CENTER_Y = SCREEN_HEIGHT / 2
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

snake_block = 10
snake_speed = 15

# Initialize pygame
pygame.init()

# Window stuff
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption('Pygame Module Testing')

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(BLUE)
            message("You Lost! Press C-Play Again or Q-Quit", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)


        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

def create_menu_manager ():
    """
    Tests all the classes in nhefner_pygame_menus.
    """

    # Create the menu manager
    man = MenuManager(screen, clock, background_color = BLACK)

    # Font that we use for text buttons
    font = pygame.font.Font("assets/fonts/ARCADECLASSIC.TTF", 50)

    # Create some pages
    home = Page("home")
    options = Page("options")
    confirm_quit = Page("confirm_quit")

    # Add the pages to the menu manager
    man.add_page(home)
    man.add_page(options)
    man.add_page(confirm_quit)

    # Home elements
    game_logo = Picture("assets/images/snake_logo.png")
    dims = game_logo.get_dimensions()
    game_logo.set_pos([SCREEN_CENTER_X - (dims[0] / 2), 20])

    start_button = ButtonText("PLAY", font, pos = [10, 300])
    options_button = ButtonText("OPTIONS", font, pos = [10, 350])
    quit_button = ButtonText("QUIT", font, pos = [10, 400])

    # Add actions to home elements
    start_button.add_action(man.exit_menu)
    options_button.add_action(man.navigate, "options")
    quit_button.add_action(man.navigate, "confirm_quit")

    # Options elements
    back_button = ButtonText("BACK", font, pos = [10, 10])
    snake_preview = Picture("assets/images/snake_preview_red.png")
    dims = snake_preview.get_dimensions()
    snake_preview.set_pos([SCREEN_CENTER_X - (dims[0] / 2), 200])
    selector_red = ButtonPicture("assets/images/snake_selector_red.png", pos = [10, 300])
    selector_blue = ButtonPicture("assets/images/snake_selector_blue.png", pos = [110, 300])
    selector_green = ButtonPicture("assets/images/snake_selector_green.png", pos = [210, 300])
    selector_pink = ButtonPicture("assets/images/snake_selector_pink.png", pos = [310, 300])
    selector_purple = ButtonPicture("assets/images/snake_selector_purple.png", pos = [410, 300])
    selector_yellow = ButtonPicture("assets/images/snake_selector_yellow.png", pos = [510, 300])

    # Add actions to options elements
    back_button.add_action(man.navigate, "home")
    selector_red.add_action(snake_preview.set_picture, "assets/images/snake_preview_red.png")
    selector_blue.add_action(snake_preview.set_picture, "assets/images/snake_preview_blue.png")
    selector_green.add_action(snake_preview.set_picture, "assets/images/snake_preview_green.png")
    selector_pink.add_action(snake_preview.set_picture, "assets/images/snake_preview_pink.png")
    selector_purple.add_action(snake_preview.set_picture, "assets/images/snake_preview_purple.png")
    selector_yellow.add_action(snake_preview.set_picture, "assets/images/snake_preview_yellow.png")

    # Confirm quit elements
    confirm_text = Text("Are you sure", font)
    dims = confirm_text.get_dimensions()
    confirm_text.set_pos([SCREEN_CENTER_X - (dims[0] / 2), 100])
    yes = ButtonText("Yes", font)
    dims = yes.get_dimensions()
    yes.set_pos([SCREEN_CENTER_X - (dims[0] / 2), 150])
    no = ButtonText("No", font)
    dims = no.get_dimensions()
    no.set_pos([SCREEN_CENTER_X - (dims[0] / 2), 200])

    # Add actions to confirm quit elements
    yes.add_action(man.kill_program)
    no.add_action(man.navigate, "home")

    # Add elements to each page
    home.add_element(game_logo)
    home.add_element(start_button)
    home.add_element(options_button)
    home.add_element(quit_button)

    options.add_element(back_button)
    options.add_element(snake_preview)
    options.add_element(selector_red)
    options.add_element(selector_blue)
    options.add_element(selector_green)
    options.add_element(selector_pink)
    options.add_element(selector_purple)
    options.add_element(selector_yellow)

    confirm_quit.add_element(confirm_text)
    confirm_quit.add_element(yes)
    confirm_quit.add_element(no)

    # Setting the start page
    man.set_start_page("home")

    return man

def main ():

    man = create_menu_manager()

    while True:

        # Run the menu manager
        man.run()

        gameLoop()

if __name__ == "__main__":

    main()
    pygame.quit()
