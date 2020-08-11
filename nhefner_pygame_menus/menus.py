"""
Noah Hefner
Pygame Menu System
Last Edit: 11 August 2020
"""

# Imports
import pygame
import string

# Initialize pygame
pygame.init()

# Settings for menu system
menu_manager_settings = {

    "element_colorkey" : [0, 0, 0],
    "menu_background_color" : [0, 0, 0],
    "menu_fps" : 60

}

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

        Arguments:
            function: The function to execute.
            args: Arguments for the function.
            kwargs: Keyword arguments for the function.
        """

        self.function = function
        self.arguments = args
        self.keyword_arguments = kwargs

    def execute (self):
        """
        Calls the function, passing it the args and kwargs.
        """

        self.function(*self.arguments, **self.keyword_arguments)

class ButtonPicture(pygame.sprite.Sprite):
    """
    Button object for menu manager.

    Attributes:
        image (pygame.image): Image for button.
        rect (pygame.image.rect): Position, height, width values for image.
        actions (list): List of action objects. These actions are executed when
                        the button is pressed.
    """

    def __init__ (self, image, pos = [0,0]):
        """
        Instantiate a button object.

        Arguments:
            image (string): Path of image file to be used for button.
            pos (list): XY position for the button.
        """

        super(ButtonPicture, self).__init__()

        self.image = pygame.image.load(image)
        self.image.set_colorkey(menu_manager_settings["element_colorkey"])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.actions = list()

    def get_pos (self):
        """
        Get the position of this picture button element.

        Returns:
            pos (list): XY position of the picture button.
        """

        position = [self.rect.x, self.rect.y]
        return position

    def set_pos (self, pos):
        """
        Set position of the button.

        Arguments:
            pos (list): XY position to set the button to. Should be 2 integers.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def add_action (self, function, *args, **kwargs):
        """
        Adds an action to the list of actions for this button.

        Arguments:
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
        Returns true if the mouse cursor position is on this sprite. False
        otherwise.

        Arguments:
            mouse_pos (list): XY position of the cursor. Should be 2 integers.
        """

        # Check x axis
        within_x = mouse_pos[0] >= self.rect.x and mouse_pos[0] <= self.rect.x + self.rect.width

        # Check y axis
        within_y = mouse_pos[1] >= self.rect.y and mouse_pos[1] <= self.rect.y + self.rect.height

        # True if within x and y area
        return within_x and within_y

class ButtonText (pygame.sprite.Sprite):
    """
    Text Button object for menu manager.

    Attributes:
        font (pygame.font.SysFont): Font to render the text button in.
        text (string): Text to make the button from.
        antialias (boolean): Sets on/off antialias for the rendering of the
                             text button.
        background_color (list): RGB values for the background color of the
                                 text button.
        color (list): RGB values for the color of this text button.
        image (pygame.image): Pygame image for the text button.
        rect (pygame.image.rect): Position, height, width values for image.
        actions (list): List of action objects. These actions are executed when
                        the text button is pressed.
    """

    def __init__ (self, font, text, antialias = True, \
                  background_color = [0, 0, 0], color = [255, 255, 255], \
                  pos = [0,0]):
        """
        ButtonText constructor.

        Arguments:
            font (pygame.font.SysFont): Font to render the text button in.
            text (string): Text to make the button from.
            antialias (boolean): Sets on/off antialias for the rendering of the
                                 text.
            background_color (list): RGB values for the background color of the
                                     text button.
            color (list): RGB values for the color of this text button.
            pos (list): XY position for the text button.
        """

        super(ButtonText, self).__init__()

        self.font = font
        self.text = text

        self.antialias = antialias
        self.background_color = background_color
        self.color = color

        self.image = self.__render()
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.actions = list()

    def get_antialias (self):
        """
        Get antialias boolean.

        Returns:
            antialias (boolean): True if antialias is set to True, False
                                 otherwise.
        """

        return self.antialias

    def get_background_color (self):
        """
        Get the background color of the text button.

        Returns:
            background_color (list): RGB values for the background color of the
                                     text button. Should be 3 integers.
        """

        return self.background_color

    def get_pos (self):
        """
        Get the position of this text button.

        Returns:
            pos (list): XY position of the text button.
        """

        position = [self.rect.x, self.rect.y]
        return position

    def get_color (self):
        """
        Get the color of this text button.

        Returns:
            color (list): RGB values for the color of this text button.
        """

        return self.color

    def set_antialias (self, new_antialias):
        """
        Set the antialias boolean for the text button.

        Arguments:
            new_antialias (boolean): Antialias boolean. True for on, False for
                                     off.
        """

        self.antialias = new_antialias
        self.__render()

    def set_background_color (self, new_background_color):
        """
        Set the background color of the text.

        Arguments:
            new_background_color (list): RGB values for the background color of
                                         the text button. Should be 3 integers.
        """

        self.background_color = new_background_color
        self.__render()

    def set_pos (self, pos):
        """
        Set position of the text.

        Arguments:
            pos (list): XY position to set the text button to. Should be 2
                        integers.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_color (self, new_color):
        """
        Set the color of the text button.

        Arguments:
            new_color (list): RGB values for the new color of this text button.
                              Should be 3 integers.
        """

        self.color = new_color
        self.__render()

    def add_action (self, function, *args, **kwargs):
        """
        Adds an action to the list of actions for this button.

        Arguments:
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

        Arguments:
            mouse_pos (list): XY position of the cursor.
        """

        # Check x area
        within_x = mouse_pos[0] >= self.rect.x and mouse_pos[0] <= self.rect.x + self.rect.width

        # Check y area
        within_y = mouse_pos[1] >= self.rect.y and mouse_pos[1] <= self.rect.y + self.rect.height

        # True if within x and y area
        return within_x and within_y

    def __render (self):
        """
        Render the image of the button using the attributes of this instance.
        Also updates rect in case text change alters rect area.

        Returns:
            image (pygame.image): Pygame image for the text button.
        """

        image = self.font.render(str(self.text), self.antialias, self.color, self.background_color)
        self.rect = image.get_rect()

        return image

class Picture (pygame.sprite.Sprite):
    """
    Picture object for menu manager.

    Attributes:
        image (pygame.image): Image for picture.
        rect (pygame.image.rect): Position, height, width values for picture.
    """

    def __init__ (self, image, pos = [0,0]):
        """
        Instantiate a picture object.

        Arguments:
            image (string): Path of image file to be used for picture.
            pos (list): XY position for the picture.
        """

        super(Picture, self).__init__()

        self.image = pygame.image.load(image)
        self.image.set_colorkey(menu_manager_settings["element_colorkey"])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

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
            pos (list): XY position to set the picture to.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Text (pygame.sprite.Sprite):
    """
    Text object for MenuManager.

    Attributes:
        font (pygame.font): Font used to render the text.
        text (string): Text to be rendered.
        antialias (boolean): Adds antialias to text.
        background_color (list): Background color of the text.
        color (list): Color of the text.
        pos (list): Position of the text.
        image (pygame.image): Rendered text.
        rect (pygame.image.rect): Position, height, width values for Text.
    """

    def __init__ (self, font, text, antialias = True, \
                  background_color = [0, 0, 0], color = [255, 255, 255], \
                  pos = [0, 0]):
        """
        Instantiates a new Text object.

        Arguments:
            font (pygame.font): Font used to render the text.
            text (String): Text to be rendered.
            antialias (Boolean): Adds antialias to text.
            background_color (list): Background color of the text.
            color (list): Color of the text.
            pos (list): Position of the text.
        """

        super(Text, self).__init__()

        self.font = font
        self.text = text

        self.antialias = antialias
        self.background_color = background_color
        self.color = color
        self.pos = pos

        self.image = self.__render()
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def get_antialias (self):
        """
        Get antialias boolean.

        Returns:
            antialias (boolean): True if antialias is set to True, False
                                 otherwise.
        """

        return self.antialias

    def get_background_color (self):
        """
        Get the background color of the text.

        Returns:
            background_color (list): RGB values for the background color of the
                                     text.
        """

        return self.background_color

    def get_pos (self):
        """
        Get the position of this text button element.

        Returns:
            pos (list): XY position of the text button.
        """

        position = [self.rect.x, self.rect.y]
        return position

    def get_color (self):
        """
        Get the color of this text button element.

        Returns:
            color (list): RGB values for the color of this text button.
        """

        return self.color

    def set_antialias (self, new_antialias):
        """
        Set the antialias boolean for the text.

        Arguments:
            new_antialias (boolean): Antialias boolean. True for on, False for
                                     off.
        """

        self.antialias = new_antialias
        self.__render()

    def set_background_color (self, new_background_color):
        """
        Set the background color of the text.

        Arguments:
            new_background_color (list): RGB values for the background color of
                                         the text. Should be 3 integers.
        """

        self.background_color = new_background_color
        self.__render()

    def set_pos (self, pos):
        """
        Set position of the text.

        Arguments:
            pos (list): XY position to set the text button to.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_color (self, new_color):
        """
        Set the color of the text.

        Arguments:
            new_color (list): RGB values for the new color of this text button.
        """

        self.color = new_color
        self.__render()

    def __render (self):
        """
        Render the image of the button using the attributes of this instance.
        Also updates rect in case text change alters rect area.

        Returns:
            image (pygame.image): Pygame image for the text button.
        """

        image = self.font.render(str(self.text), self.antialias, self.color, self.background_color)
        self.rect = image.get_rect()

        return image

class MenuManager:
    """
    Menu manager for pygame.

    Attributes:
        pages (list): List of pages in the menu manager.
        current_page (Page): Page currently being displayed.
        screen (pygame.display): Surface to blit the pages and game to.
        clock (pygame.time.Clock): Used to set/cap game FPS.
        start_page_set (Boolean): Switch that checks if start page has been set.
    """

    def __init__ (self, screen, clock):
        """
        Instantiate a MenuManager object.
        """

        self.pages = list()
        self.current_page = None
        self.screen = screen
        self.clock = clock
        self.start_page = None
        self.exiting = False

    def run (self):
        """
        Puts the menu loop into a function for ease of use.
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
        exit()

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

    def __display (self):
        """
        Blit everything from backend to the screen.
        """

        # Fill background
        self.screen.fill(menu_manager_settings["menu_background_color"])

        # Display current screen
        self.current_page.display(self.screen)
        pygame.display.flip()
        self.clock.tick(menu_manager_settings["menu_fps"])

    def __update (self):
        """
        Handles user events. Also checks if a start page has been set. This
        function will prevent the program from running if a sart page has not
        beem set.

        Returns:
            Boolean: True if program execution should continue, False otherwise.
        """

        if self.start_page == None:

            print("Start page not set!")
            self.kill_program()

        if self.exiting:

            self.exiting = False
            self.current_page = self.start_page

            return False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.kill_program()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                for element in self.current_page.elements:

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

        Arguments:
            id (string/int): ID for this page.
        """

        self.id = id
        self.elements = list()

    def add_element (self, new_element):
        """
        Adds an element to the page.

        Arguments:
            new_element (Button): Element to add to the page.
        """

        self.elements.append(new_element)

    def display (self, screen):
        """
        Show this screen in the window.

        Arguments:
            screen (pygame.display): Surface to blit the elements to.
        """

        for element in self.elements:

            screen.blit(element.image, [element.rect.x, element.rect.y])
