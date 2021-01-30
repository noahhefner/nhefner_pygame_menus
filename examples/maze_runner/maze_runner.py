"""
This script shows how to implement a menu system with nhefner_pygame_menus. The
general structure should be laid out as follows:

imports

classes

def main:

    game setup stuff here (create players, setup world, etc.)

    menu manager stuff here (create manager, buttons, pages, etc.)

    while true:

        manager.run()

        game_in_progress = True

        while game_in_progress:

            game logic here

            game drawing here

        game reset code here

if __name__ == "__main__":
    main()
    pygame.quit()

---------------------------- CREDITS FOR THIS GAME -----------------------------

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

From:
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py

Explanation video: http://youtu.be/5-SbFanyUkQ

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

--------------------------------------------------------------------------------

"""
import pygame

# Imports for the menu system
import os
from nhefner_pygame_menus import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def set_color(self, new_color):
        """ Change color of player block. """

        self.image.fill(new_color)

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
    clock = pygame.time.Clock()

    # Set the title of the window
    pygame.display.set_caption('Maze Runner')

    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    """ Menu Manager Additions --------------------------------------------- """

    # Step One: Create menu manager --------------------------------------------
    man = MenuManager(screen, clock)

    # Step Two: Create pages ---------------------------------------------------
    home = Page("home")
    options = Page("options")
    confirm_exit = Page("confirm_exit")

    # Step Three: Create elements for the pages --------------------------------
    font = pygame.font.Font("arcade_font.ttf", 40) # Font for text buttons

    button_play = ButtonText("PLAY", font, pos = [20, 375], background_color = [255, 0, 0])
    button_options = ButtonText("OPTIONS", font, pos = [20, 400], background_color = [255, 0, 0])
    button_quit = ButtonText("QUIT", font, pos = [20, 425], background_color = [255, 0, 0])
    # When making buttons, we need to use the add_action method to define their functionality
    # If the function requires arguments, we simply pass them to the add_action method after
    # the function name.
    button_play.add_action(man.exit_menu)
    button_options.add_action(man.navigate, "options") # Function with arguments example.
                                                       # The navigate function on the MenuManager
                                                       # takes one argument, the id of the page we
                                                       # want to navigate to, so we pass the id of
                                                       # our options page as an argument to the
                                                       # add_action method.
    button_quit.add_action(man.navigate, "confirm_exit")

    button_back_op = ButtonText("BACK", font, pos = [10, 10], background_color = [255, 0, 0])

    text_player_color = Text("CHOSSE YOUR PLAYER COLOR", font, pos = [10, 100])
    button_blue_player = ButtonText("BLUE", font, pos = [10, 150])
    button_red_player = ButtonText("RED", font, pos = [10, 200])
    picture_arrow = Picture("arrow.png", pos = [120, 120])

    button_back_op.add_action(man.navigate, "home")
    button_blue_player.add_action(player.set_color, BLUE)
    button_blue_player.add_action(picture_arrow.set_pos, [120, 120])
    button_red_player.add_action(player.set_color, RED)
    button_red_player.add_action(picture_arrow.set_pos, [120, 170])
    # Notice we can use the set_color method on the Player class to change the
    # color of the player when the user presses this button.

    text_confirmation = Text("ARE YOU SURE ABOUT THAT", font, pos = [20, 20], background_color = [255, 0, 0])
    button_yes = ButtonText("YES", font, pos = [20, 70], background_color = [255, 0, 0])
    button_no = ButtonText("NO", font, pos = [20, 95], background_color = [255, 0, 0])

    button_yes.add_action(man.kill_program)
    button_no.add_action(man.navigate, "home")

    # Step Four: Add elements to their pages -----------------------------------
    home.add_element(button_play)
    home.add_element(button_options)
    home.add_element(button_quit)

    options.add_element(button_back_op)
    options.add_element(text_player_color)
    options.add_element(button_blue_player)
    options.add_element(button_red_player)
    options.add_element(picture_arrow)

    confirm_exit.add_element(text_confirmation)
    confirm_exit.add_element(button_yes)
    confirm_exit.add_element(button_no)

    # Step Five: Add pages to menu manager -------------------------------------
    man.add_page(home)
    man.add_page(options)
    man.add_page(confirm_exit)

    # Step Six: Set a start page -----------------------------------------------
    man.set_start_page("home")

    """
    NOTICE: Put everything in an infinite loop. What will happen is that after
    we exit the menu, we will enter the game.
    """
    while True:

        # Call this function to run the menu manager
        man.run()

        # Game code goes here, use while loop as normal
        in_game = True
        while in_game:

            # --- Event Processing ---

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit() # Kill the program when we hit the X

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(-5, 0)
                    if event.key == pygame.K_RIGHT:
                        player.changespeed(5, 0)
                    if event.key == pygame.K_UP:
                        player.changespeed(0, -5)
                    if event.key == pygame.K_DOWN:
                        player.changespeed(0, 5)
                    if event.key == pygame.K_q:
                        in_game = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(5, 0)
                    if event.key == pygame.K_RIGHT:
                        player.changespeed(-5, 0)
                    if event.key == pygame.K_UP:
                        player.changespeed(0, 5)
                    if event.key == pygame.K_DOWN:
                        player.changespeed(0, -5)

            # --- Game Logic ---

            player.move(current_room.wall_list)

            if player.rect.x < 0:
                if current_room_no == 0:
                    player.rect.x = 0
                elif current_room_no == 1:
                    current_room_no = 0
                    current_room = rooms[current_room_no]
                    player.rect.x = 790
                elif current_room_no == 2:
                    current_room_no = 1
                    current_room = rooms[current_room_no]
                    player.rect.x = 790

            if player.rect.x > 801:
                if current_room_no == 0:
                    current_room_no = 1
                    current_room = rooms[current_room_no]
                    player.rect.x = 0
                elif current_room_no == 1:
                    current_room_no = 2
                    current_room = rooms[current_room_no]
                    player.rect.x = 0
                else:
                    in_game = False

            # --- Drawing ---
            screen.fill(BLACK)

            movingsprites.draw(screen)
            current_room.wall_list.draw(screen)

            pygame.display.flip()

            clock.tick(60)

        """
        This is important! When we are done playing the game, we need to reset
        everything to how it was before the game started. This allows us to play
        the game multiple times without killing the program. In this case, we
        need to reset the current room, current room number, player position,
        and the change_x and change_y attributes of the player.
        """
        current_room_no = 0
        current_room = rooms[current_room_no]
        player.rect.x = 50
        player.rect.y = 50
        player.change_x = 0
        player.change_y = 0

if __name__ == "__main__":
    main()
    pygame.quit()
