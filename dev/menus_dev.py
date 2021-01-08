"""
Noah Hefner
Pygame Menu System
Last Edit: 1 January 2021
"""

# Imports
import pygame
import string
import os.path

# Initialize pygame
pygame.init()

# Some constants
BLACK    = [0, 0, 0]
WHITE    = [255, 255, 255]
MENU_FPS = 60
DEFAULT_FONT = pygame.font.SysFont("Arial", 40)
DEFAULT_TEXT_COLOR = WHITE
DEFAULT_COLORKEY = BLACK
DEFAULT_MENU_BACKGROUND_COLOR = BLACK

class Action:
    """
    Holds function and argument data for buttons.

    Attributes:
        function: The function to execute.
        arguments: Arguments for the function.
        keyword_arguments: Keyword arguments for the function.
    """

    def __init__ (self, function, args, kwargs):
        """
        Instantiate an Action object.

        Positional Arguments:
            function: The function to execute.
            args: Arguments for the function.
            kwargs: Keyword arguments for the function.
        """

        self.function = function
        self.arguments = args
        self.keyword_arguments = kwargs

    def execute (self):
        """
        Calls the function, passing in the arguments and keyword arguments from
        this Action object.
        """

        self.function(*self.arguments, **self.keyword_arguments)

class ButtonPicture(pygame.sprite.Sprite):
    """
    Button that uses a picture as its image. When clicked, the Actions attatched
    to the button will be executed.

    Attributes:
        image (pygame.image): Image for button.
        rect (pygame.image.rect): Position, height, width values for image.
        actions (list): List of Action objects to be executed when the button is
                        clicked.
    """

    def __init__ (self, filename, pos = [0,0], colorkey = DEFAULT_COLORKEY):
        """
        Instantiate a ButtonPicture object.

        Positional Arguments:
            filename (string): Path of image file to be used for button.

        Keyword Arguments:
            pos (list): XY position for the button. Default is [0,0].
            colorkey (list): Colorkey for the image used. Default is black.
        """

        super(ButtonPicture, self).__init__()

        self.image = pygame.image.load(filename)
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.actions = []

    def get_dimensions (self):
        """
        Get the width and height of the ButtonPicture.

        Returns:
            list: Width and Height of the ButtonPicture. Uses width and height
                  from self.rect.
                  Format: [width, height]
        """

        dimensions = [self.rect.width, self.rect.height]
        return dimensions

    def get_pos (self):
        """
        Get the position of this picture button element.

        Returns:
            list: XY position of the picture button.
                  Format: [x, y]
        """

        position = [self.rect.x, self.rect.y]
        return position

    def set_pos (self, pos):
        """
        Set position of the button.

        Positional Arguments:
            list: XY position to set the button to.
                  Format: [x, y]
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def add_action (self, function, *args, **kwargs):
        """
        Adds an action to the list of actions for this button.

        Positional Arguments:
            function (function reference): The function to execute.
            *args: Arguments for the function.
            **kwargs: Keyword arguments for the function.
        """

        new_action = Action(function, args, kwargs)
        self.actions.append(new_action)

    def execute_actions (self):
        """
        Execute function linked to this button.
        """

        for action in self.actions:

            action.execute()

    def is_clicked (self, mouse_pos):
        """
        Returns true if the mouse cursor position is on this sprite.

        Positional Arguments:
            mouse_pos (list): XY position of the cursor.
        """

        # Check x axis
        within_x = mouse_pos[0] >= self.rect.x and \
                   mouse_pos[0] <= self.rect.x + self.rect.width

        # Check y axis
        within_y = mouse_pos[1] >= self.rect.y and \
                   mouse_pos[1] <= self.rect.y + self.rect.height

        # True if within x and y area
        return within_x and within_y

class ButtonText (pygame.sprite.Sprite):
    """
    Button that uses text as its image. When clicked, the Actions attatched to
    the button will be executed.

    Attributes:
        text (string): Text to make the button from.
        font (pygame.font.SysFont): Font to render the text in.
        color (list): Color that the text should be. Should be supplied as a
                      list of three integers between 0 and 255, inclusive.
                      Default is [255, 255, 255], or white.
        background_color (list): Color that the background of the text should
                                 be. Should be supplied as a list of three
                                 integers between 0 and 255, inclusive. Default
                                 is [255, 255, 255], or white.
        antialias (boolean): True if pygame should antialias the image for the
                             button. True by default.
        image (pygame.image): Image for button.
        rect (pygame.image.rect): Position, height, width values for image.
        actions (list): List of Action objects to be executed when the button is
                        clicked.
    """

    def __init__ (self, text, font = DEFAULT_FONT, pos = [0,0],
                  color = DEFAULT_TEXT_COLOR, background_color = None,
                  antialias = True):
        """
        Instantiate a ButtonText object.

        Positional Arguments:
            text (string): Text to make the button from.
            font (pygame.font.SysFont): Font to render the text in.

        Keyword Arguments:
            pos (list): XY position for the button.
            color (list): Color that the text should be. Should be supplied as a
                          list of three integers between 0 and 255, inclusive.
                          Default is [255, 255, 255], or white.
            background_color (list): Color that the background of the text
                                     should be. Should be supplied as a list of
                                     three integers between 0 and 255,
                                     inclusive. Default is None, or no
                                     background color.
            antialias (boolean): True if pygame should antialias the image for
                                 the button. True by default.
        """

        super(ButtonText, self).__init__()

        self.text = text
        self.font = font
        self.color = color
        self.background_color = background_color
        self.antialias = antialias

        self.image = font.render(str(text), antialias, color, background_color)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.actions = []

    def get_dimensions (self):
        """
        Get the width and height of the button.

        Returns:
            list: Width and Height of the button. Uses width and height from
                  self.rect.
                  Format: [width, height]
        """

        dimensions = [self.rect.width, self.rect.height]
        return dimensions

    def get_pos (self):
        """
        Get the position of this text button element.

        Returns:
            pos (list): XY position of the text button.
        """

        position = [self.rect.x, self.rect.y]
        return position

    def get_text(self):
        """
        Get the text of the button.

        Returns:
            self.text (string): Text of the button.
        """

        return self.text

    def set_pos (self, pos):
        """
        Set position of the text.

        Positional Arguments:
            pos (list): XY position to set the text button to.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_text (self, new_text):
        """
        Changes the text of the button.

        Positional Arguments:
            new_text (String): New text of the button.
        """

        self.text = new_text
        self.image = self.font.render(str(new_text), self.antialias, self.color, self.background_color)

    def add_action (self, function, *args, **kwargs):
        """
        Adds an action to the list of actions for this button.

        Positional Arguments:
            function: The function to execute.
            *args: Arguments for the function.
            **kwargs: Keyword arguments for the function.
        """

        new_action = Action(function, args, kwargs)
        self.actions.append(new_action)

    def execute_actions (self):
        """
        Execute function linked to this button.
        """

        for action in self.actions:

            action.execute()

    def is_clicked (self, mouse_pos):
        """
        Returns true if the mouse cursor position is on this sprite.

        Positional Arguments:
            mouse_pos (tuple): XY position of the cursor.
        """

        # Check x area
        within_x = mouse_pos[0] >= self.rect.x and mouse_pos[0] <= self.rect.x + self.rect.width

        # Check y area
        within_y = mouse_pos[1] >= self.rect.y and mouse_pos[1] <= self.rect.y + self.rect.height

        # True if within x and y area
        return within_x and within_y

class Picture (pygame.sprite.Sprite):
    """
    Picture object for menu manager.

    Attributes:
        image (pygame.image): Image for picture.
        rect (pygame.image.rect): Position, height, width values for picture.
    """

    def __init__ (self, filename, pos = [0,0], colorkey = DEFAULT_COLORKEY):
        """
        Instantiate a Picture object.

        Positional Arguments:
            filename (string): Path of image file to be used for picture.

        Keyword Arguments:
            pos (tuple): XY position for the picture. Default is [0, 0].
            colorkey (list): Colorkey for the picture file used. Default is
                             black.
        """

        super(Picture, self).__init__()

        self.image = pygame.image.load(filename)
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def get_dimensions (self):
        """
        Get the width and height of the picture.

        Returns:
            list: Width and Height of the picture. Uses width and height from
                  self.rect.
                  Format: [width, height]
        """

        dimensions = [self.rect.width, self.rect.height]
        return dimensions

    def get_pos (self):
        """
        Get the position of this picture element.

        Returns:
            pos (list): XY position of the picture.
        """

        position = [self.rect.x, self.rect.y]
        return position

    def set_pos (self, pos):
        """
        Set position of the picture.

        Arguments:
            pos (tuple): XY position to set the picture to.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_picture (self, new_image, new_colorkey = DEFAULT_COLORKEY):
        """
        Set a new picture for this instance of Picture. Preserves x and y
        position of the old picture.

        Positional Arguments:
            new_image (string): File name of the new picture.

        Keyword Arguments:
            new_colorkey (list): Colorkey for the picture file used. Should be
                                 given as a list of three integers. Default is
                                 black.
        """

        # Store the current position
        temp_old_pos = self.get_pos()

        # Load the new image
        self.image = pygame.image.load(new_image)
        self.image.set_colorkey(new_colorkey)
        self.rect = self.image.get_rect()

        # Set the x and y position using the old position
        self.rect.x = temp_old_pos[0]
        self.rect.y = temp_old_pos[1]

class Text (pygame.sprite.Sprite):
    """
    Text object for MenuManager.

    Attributes:
        text (String): Text to be rendered.
        font (pygame.font): Font used to render the text.
        pos (tuple): Position of the text.
        color (List): Color of the text.
        antialias (Boolean): Adds antialias to text.
        background_color (List): Background color of the text.
        image (pygame.image): Rendered text.
        rect (pygame.image.rect): Position, height, width values for Text.
    """

    def __init__ (self, text, font = DEFAULT_FONT, pos = [0,0],
                  color = DEFAULT_TEXT_COLOR, antialias = True,
                  background_color = None):
        """
        Instantiates a new Text object.

        Positional Arguments:
            text (String): Text to be rendered.
            font (pygame.font): Font used to render the text.

        Keyword Arguments:
            pos (tuple): Position of the text.
            color (List): Color of the text.
            antialias (Boolean): Adds antialias to text.
            background_color (List): Background color of the text.
        """

        super(Text, self).__init__()

        self.text = text
        self.font = font
        self.pos = pos
        self.color = color
        self.antialias = antialias

        self.image = font.render(str(text), antialias, color, background_color)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def get_dimensions (self):
        """
        Get the width and height of the Text.

        Returns:
            list: Width and Height of the Text. Uses width and height from
                  self.rect.
                  Format: [width, height]
        """

        dimensions = [self.rect.width, self.rect.height]
        return dimensions

    def get_pos (self):
        """
        Get the position of this text element.

        Returns:
            pos (list): XY position of the text.
        """

        position = [self.rect.x, self.rect.y]
        return position

    def set_pos (self, pos):
        """
        Set position of the text.

        Arguments:
            pos (list): XY position to set the text to.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_text (self, new_text, new_font = DEFAULT_FONT,
                  new_color = DEFAULT_TEXT_COLOR, new_antialias = True,
                  new_background_color = None):
        """
        Set a new string as the text. Maintains the x and y position of the
        original text.

        Positional Arguments:
            text (String): Text to be rendered.
            font (pygame.font): Font used to render the text.

        Keyword Arguments:
            pos (tuple): Position of the text.
            color (List): Color of the text.
            antialias (Boolean): Adds antialias to text.
            background_color (List): Background color of the text.
        """

        # Store the current position
        temp_old_pos = self.get_pos()

        # Re-render the text, setting image and rect
        self.image = font.render(str(new_text), new_antialias, new_color, \
                                 new_background_color)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        # Set the x and y position using the old position
        self.rect.x = temp_old_pos[0]
        self.rect.y = temp_old_pos[1]

class MenuManager:
    """
    Menu manager for pygame.

    Attributes:
        pages (List): List of pages in the menu manager.
        current_page (Page): Page currently being displayed.
        screen (pygame.display): Surface to blit the pages and game to.
        clock (pygame.time.Clock): Used to set/cap game FPS.
        start_page_set (Boolean): Switch that checks if start page has been set.
    """

    def __init__ (self, screen, clock,
                  background_color = DEFAULT_MENU_BACKGROUND_COLOR):
        """
        Instantiate a MenuManager object.

        Positional Arguments:
            screen (pygame.Surface): Surface we are blitting objects to.
            clock (pygame.time.Clock): Pygame clock.

        Keyword Arguments:
            background_color (list): Background color for the menu system.
                                     Should be supplied as a list of three
                                     integers. Default is black.

        NOTE: For the menu manager system to work as intended, you will want to
              use the same screen and clock objects for the menu manager and
              your game.
        """

        self.screen = screen
        self.clock = clock
        self.background_color = background_color
        self.pages = list()
        self.current_page = None
        self.start_page = None
        self.exiting = False
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.highscore_list = list()
        self.num_highscores = 5

    def run (self):
        """
        Update and display the menu system. Puts the menu loop into a function
        for ease of use.
        """

        while self.__update():

            self.__display()

    def add_page (self, new_page):
        """
        Adds a page to the menu manager.

        Arguments:
            new_page (Page): Page to be added to the menu manager.
        """

        self.pages.append(new_page)

    def set_start_page (self, page_id):
        """
        Set a start page for the menu manager. This function must be called
        before calling ManuManager.run() or the program will be terminated.

        Arguments:
            page_id (String/Int): ID of the desired page destination.

        NOTE: See Page class for more info on page id's.
        """

        for page in self.pages:

            if (page_id == page.id):

                self.current_page = page
                self.start_page = page
                return

        print("Invalid start page id!")
        exit(-1)

    def navigate (self, page_id):
        """
        Sets the currently showing page using the id attribute of Page class.

        Arguments:
            page_id (String/Int): ID of the desired page destination.

        NOTE: See Page class for more info on page id's.
        """

        for page in self.pages:

            if page.id == page_id:

                self.current_page = page

                return

        print("Invalid page id, " + str(page_id) + "! Exiting.")
        exit(-1)

    def exit_menu (self):
        """
        For exiting the menu manager. Flips the exiting flag.
        """

        self.exiting = True

    def kill_program (self):
        """
        Terminates the entire program.
        """

        exit()

    def add_highscore_page (self, button, back_page_id, font,
                            num_highscores = 5,
                            hs_score_file = "highscores.txt"):
        """
        Adds a highscore page to the MenuManager.

        Positional Arguments:
            button (ButtonText, ButtonPicture): The button you want to use to
                                                navigate to the highscore page.
            back_page_id (Page): The highscore page has a back button.
                                 "back_page_id" should be the ID of the page you
                                 want to return to when the back button is
                                 pressed.
            font (pygame.font.Font/Sysfont): Font used to render the Text
                                             objects on the highscore page.

        Keyword Arguments:
            hs_score_file (string): Path to the file where highscores are saved.
                                    Default is in cwd with filename
                                    "highscores.txt".

        Prerequisites:
            - The button passed as the "button" argument should be of type
              ButtonText or ButtonPicture.
            - The page with ID back_page_id should be a page that is already in
              the MenuManager.
        """

        # Save highscore stuff to the MenuManager instance
        self.num_highscores = num_highscores

        # Create the highscore page
        highscore_page = Page("highscores")

        # Add navigation action to the button
        button.add_action(self.navigate, "highscores")

        # Fetch the highscores and usernames from the highscores.txt file
        users = []
        scores = []

        with open(hs_score_file, 'r') as f:

            contents = f.readlines()

            for line in contents:

                user_score = line.strip().split(" ")

                print(user_score)

                if len(user_score) == 2:

                    users.append(user_score[0])
                    scores.append(user_score[1])

                    # Save the score to self.highscore_list
                    self.highscore_list.append([str(user_score[0]), \
                                                int(user_score[1])])

        screen_center_x = self.screen_width / 2
        vert_division = self.screen_height / (num_highscores + 1)

        # Create UI elements and add them to the highscore page
        button_back = ButtonText("Back", font, pos = [10, 10])
        button_back.add_action(self.navigate, back_page_id)
        highscore_page.add_element(button_back)

        for i in range(len(self.highscore_list)):

            text = str(users[i]) + " " + str(scores[i])

            score = Text(text, font)

            dims = score.get_dimensions()
            pos_x = screen_center_x - ((1/2) * dims[0])
            pos_y = ((i + 1) * vert_division) - ((1/2) * dims[1])
            score.set_pos([pos_x, pos_y])

            highscore_page.add_element(score)

        # Add the page to the MenuManager
        self.add_page(highscore_page)

    def save_highscore (score):

        pass

    def __write_highscore (self, user, score, hs_score_file):
        """
        Saves a score to the highscores file.

        Positional Arguments:
            user (string): Username of the player.
            score (int): Score the player got.
            hs_score_file (string): Path to the file where highscores are saved.
        """

        # Read contents from file
        f = open(hs_score_file, 'r')
        contents = f.readlines()
        f.close()

        # Find the index of where this score goes
        index = 0

        for line in contents:

            user_score = line.strip().split(" ")

            if len(user_score) == 2:

                f_user = user_score[0]
                f_score = int(user_score[1])

                if score < f_score:

                    index += 1

        # Add the score to whatever index it should be at
        contents.insert(index, f"{user} {score}\n")

        # Add the score to the highscore list in the MenuManager
        self.highscore_list.insert(index, [user, score])

        # Make sure we don't exceed the maximum number of scores we are allowed
        # to save
        if len(contents) > self.num_highscores:

            contents = contents[0:self.num_highscores]

        # Write the new contents to the highscore file
        f = open(hs_score_file, 'w')
        contents = "".join(contents)
        f.write(contents)
        f.close()

    def __update_highscore_page (self):
        """
        Updates the elements on the highscore page.
        """

        pass

    def __display (self):
        """
        Blit everything from backend to the screen.
        """

        # Fill background
        self.screen.fill(self.background_color)

        # Display current screen
        self.current_page.display(self.screen)
        pygame.display.flip()
        self.clock.tick(MENU_FPS)

    def __update (self):
        """
        Handles user events. Also checks if a start page has been set. This
        function will prevent the program from running if a sart page has not
        beem set.

        Returns:
            boolean: True if program execution should continue, False otherwise.
        """

        # Ensure start page has been set
        if self.start_page == None:

            print("Start page not set!")
            exit(-1)

        # Exit procedures, resets current page to start page
        if self.exiting:

            self.exiting = False
            self.current_page = self.start_page

            return False

        for event in pygame.event.get():

            # Window close
            if event.type == pygame.QUIT:

                self.kill_program()

            # Left mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                for element in self.current_page.elements:

                    # Check fif we clicked a button type
                    if isinstance(element, ButtonPicture) or \
                       isinstance(element, ButtonText):

                        if element.is_clicked(mouse_pos):

                            element.execute_actions()

        return True

class Page:
    """
    Page object for menu manager.

    Attributes:
        id (string/int): ID for this page.
        elements (list): List of elements on the page.

    NOTE: The ID doesn't have to be a string/int, it just has to be some
          distinct identifier for this page. I just recommend using a string or
          an integer for simplicity and readability.
    """

    def __init__ (self, id):
        """
        Instantiate a page object.

        Positional Arguments:
            id (string/int): ID for this page.
        """

        self.id = id
        self.elements = list()

    def add_element (self, new_element):
        """
        Adds an element to the page.

        Positional Arguments:
            new_element (Button): Element to add to the page.
        """

        self.elements.append(new_element)

    def clear (self):
        """
        Removes all elements from the page.
        """

        self.elements = list()

    def display (self, screen):
        """
        Show this screen in the window.

        Positional Arguments:
            screen (pygame.display): Surface to blit the elements to.
        """

        for element in self.elements:

            screen.blit(element.image, [element.rect.x, element.rect.y])
