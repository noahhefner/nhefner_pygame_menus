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
from snake import Snake

from menus_dev import MenuManager, Page, ButtonText, ButtonPicture, Picture, Text

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_CENTER_X = int(SCREEN_WIDTH / 2)
SCREEN_CENTER_Y = int(SCREEN_HEIGHT / 2)
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
PINK = [255, 192, 203]
PURPLE = [128, 0, 128]
YELLOW = [255, 255, 0]

# Initialize pygame
pygame.init()

# Window stuff
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption('Pygame Module Testing')

""" Game Stuff ------------------------------------------------------------- """
snake_block_size = 20

snake = Snake(starting_pos = [SCREEN_CENTER_X, SCREEN_CENTER_Y],
              block_size = snake_block_size)


""" Menu Stuff ------------------------------------------------------------- """

# Create the menu manager
man = MenuManager(screen, clock)
man.set_background_color(RED)

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
highscore_button = ButtonText("HIGHSCORES", font, pos = [10, 350])
options_button = ButtonText("OPTIONS", font, pos = [10, 400])
quit_button = ButtonText("QUIT", font, pos = [10, 450])

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
selector_red.add_action(snake.set_color, RED)
selector_blue.add_action(snake_preview.set_picture, "assets/images/snake_preview_blue.png")
selector_blue.add_action(snake.set_color, BLUE)
selector_green.add_action(snake_preview.set_picture, "assets/images/snake_preview_green.png")
selector_green.add_action(snake.set_color, GREEN)
selector_pink.add_action(snake_preview.set_picture, "assets/images/snake_preview_pink.png")
selector_pink.add_action(snake.set_color, PINK)
selector_purple.add_action(snake_preview.set_picture, "assets/images/snake_preview_purple.png")
selector_purple.add_action(snake.set_color, PURPLE)
selector_yellow.add_action(snake_preview.set_picture, "assets/images/snake_preview_yellow.png")
selector_yellow.add_action(snake.set_color, YELLOW)

# Confirm quit elements
confirm_text = Text("Are you sure?")
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
home.add_element(highscore_button)
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

man.add_highscore_page(highscore_button, "home", font)

# Setting the start page
man.set_start_page("home")

""" Main Program Loop ------------------------------------------------------ """

while True:

    # Run the menu manager
    man.run()

    change_x = 0
    change_y = 0

    apple_size = snake_block_size
    apple = [5 * snake_block_size, 5 * snake_block_size]

    game_over = False

    while not game_over:

        # Handle user input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                exit(0)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    change_y = (-1) * snake_block_size
                    change_x = 0

                elif event.key == pygame.K_DOWN:

                    change_y = snake_block_size
                    change_x = 0

                elif event.key == pygame.K_LEFT:

                    change_x = (-1) * snake_block_size
                    change_y = 0

                elif event.key == pygame.K_RIGHT:

                    change_x = snake_block_size
                    change_y = 0

                elif event.key == pygame.K_q:

                    game_over = True

        # Game logic
        screen.fill(BLACK)
        snake_head = snake.get_head()

        # End the game if the snake bites itself or goes off screen
        if (snake.collides_with(snake_head) and snake.get_length() > 1) or \
           snake_head[0] < 0 or snake_head[0] > SCREEN_WIDTH or \
           snake_head[1] < 0 or snake_head[1] > SCREEN_HEIGHT:

            game_over = True

        # Move the snake and the apple (if the snake gets it)
        new_block = [snake_head[0] + change_x, snake_head[1] + change_y]
        snake.add_block(new_block)

        if not snake.collides_with(apple):

            snake.remove_tail()

        else:

            apple_x = random.randrange(0, SCREEN_WIDTH - apple_size)
            apple_y = random.randrange(0, SCREEN_HEIGHT - apple_size)
            apple = [apple_x, apple_y]

        # Displaying the game
        snake.draw(screen)
        pygame.draw.rect(screen, RED, [apple[0], apple[1], apple_size, apple_size])

        pygame.display.flip()

        clock.tick(20)

    man.save_highscore("fatchungus", 100)

pygame.quit()
