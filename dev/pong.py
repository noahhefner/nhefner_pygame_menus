"""
Noah Hefner
Pong w/ Menu System Example
Last Edit: 8 January 2021
"""

# Imports
import pygame
import random

# Constants
WHITE = [255, 255, 255]
BLACK = [  0,   0,   0]
RED   = [255,   0,   0]
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 800
PLAYER_SPEED = 8
FPS = 60

# Initialize pygame
pygame.init()

class Player (pygame.sprite.Sprite):

    def __init__ (self, color = WHITE):

        super(Player, self).__init__()

        self.image = pygame.Surface([20, 80])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.change_y = 0

    def get_rect (self):

        return self.rect

    def set_position (self, x, y):

        self.rect.x = x
        self.rect.y = y

    def change_speed (self, change_y):

        self.change_y += change_y

    def move (self):

        self.rect.y += self.change_y

        if self.rect.y < 0:

            self.rect.y = 0

        elif self.rect.y + self.rect.height > SCREEN_HEIGHT:

            self.rect.y = SCREEN_HEIGHT - self.rect.height

class Ball (pygame.sprite.Sprite):

    def __init__ (self, color = WHITE):

        super(Ball, self).__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH / 2) - (self.rect.width / 2)
        self.rect.y = (SCREEN_HEIGHT / 2) - (self.rect.height / 2)
        self.change_x = 0
        self.change_y = 0

    def change_speed (self, change_x, change_y):

        self.change_x += change_x
        self.change_y += change_y

    def bounce (self, horizontal, vertical):

        if horizontal:

            self.change_x *= -1

        if vertical:

            self.change_y *= -1

    def move (self):

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.y < 0:

            self.rect.y = 0
            self.change_y *= -1

        elif self.rect.y + self.rect.height > SCREEN_HEIGHT:

            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.change_y *= -1

# Window setup
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption('Pong')

# Create players
player_one = Player()
player_two = Player()

p1_x = 0
p1_y = (SCREEN_HEIGHT / 2) - (player_one.get_rect().height / 2)
p2_x = SCREEN_WIDTH - player_two.get_rect().width
p2_y = (SCREEN_HEIGHT / 2) - (player_one.get_rect().height / 2)

player_one.set_position(p1_x, p1_y)
player_two.set_position(p2_x, p2_y)

# Create the ball
ball = Ball()
ball.change_speed(random.randrange(-6, -2), random.randrange(-6, -2))

# Add players and ball to sprite group
moving_sprites = pygame.sprite.Group()
moving_sprites.add(player_one)
moving_sprites.add(player_two)
moving_sprites.add(ball)

game_over = False

while not game_over:

    # Handle user input
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:

                player_one.change_speed(-1 * PLAYER_SPEED)

            elif event.key == pygame.K_a:

                player_one.change_speed(PLAYER_SPEED)

            elif event.key == pygame.K_p:

                player_two.change_speed(-1 * PLAYER_SPEED)

            elif event.key == pygame.K_l:

                player_two.change_speed(PLAYER_SPEED)

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_q:

                player_one.change_speed(PLAYER_SPEED)

            elif event.key == pygame.K_a:

                player_one.change_speed(-1 * PLAYER_SPEED)

            elif event.key == pygame.K_p:

                player_two.change_speed(PLAYER_SPEED)

            elif event.key == pygame.K_l:

                player_two.change_speed(-1 * PLAYER_SPEED)

    # Game logic
    player_one.move()
    player_two.move()
    ball.move()

    if pygame.sprite.collide_mask(player_one, ball) or \
       pygame.sprite.collide_mask(player_two, ball):

       ball.bounce(True, False)

    # Drawing
    screen.fill(BLACK)

    # Draw the board
    pygame.draw.rect(screen, RED, [(SCREEN_WIDTH / 2) - 5, 0, 10, SCREEN_HEIGHT])

    # Draw the player and ball
    moving_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
