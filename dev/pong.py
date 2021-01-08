"""
Noah Hefner
Pong w/ Menu System Example
Last Edit: 8 January 2021
"""

# Imports
import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WHITE = [255, 255, 255]
BLACK = [  0,   0,   0]
RED   = [255,   0,   0]
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 800
PLAYER_SPEED = 8
FPS = 60
FONT = pygame.font.SysFont("Ubuntu-B", 60)
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
CLOCK = pygame.time.Clock()

# Set window title
pygame.display.set_caption('Pong')

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

    def get_pos (self):

        return [self.rect.x, self.rect.y]

    def get_size (self):

        return [self.rect.width, self.rect.height]

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

    def reset (self):

        self.rect.x = (SCREEN_WIDTH / 2) - (self.rect.width / 2)
        self.rect.y = (SCREEN_HEIGHT / 2) - (self.rect.height / 2)
        self.change_x = random.randrange(-6, -2)
        self.change_y = random.randrange(-6, -2)

def play_game ():

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
    score_p1 = 0
    score_p2 = 0

    while not game_over:

        # Handle user input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                exit(0)

            elif event.type == pygame.KEYDOWN:

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

        # Bounce the ball off the players
        if pygame.sprite.collide_mask(player_one, ball) or \
           pygame.sprite.collide_mask(player_two, ball):

           ball.bounce(True, False)

        # Ball goes off screen
        ball_pos = ball.get_pos()
        ball_size = ball.get_size()

        if ball_pos[0] <= 0:

            score_p2 += 1
            ball.reset()

        elif ball_pos[0] + ball_size[0] >= SCREEN_WIDTH:

            score_p1 += 1
            ball.reset()

        # Drawing
        SCREEN.fill(BLACK)

        # Center line
        pygame.draw.rect(SCREEN, RED, [(SCREEN_WIDTH / 2) - 5, 0, 10, SCREEN_HEIGHT])

        # Text surfaces
        score_p1_surface = FONT.render(str(score_p1), True, WHITE)
        score_p2_surface = FONT.render(str(score_p2), True, WHITE)

        # Position calculations and blitting the scores
        score_p1_x = (SCREEN_WIDTH / 2) - score_p1_surface.get_rect().width - 20
        score_p1_y = SCREEN_HEIGHT - score_p1_surface.get_rect().height - 20
        SCREEN.blit(score_p1_surface, [score_p1_x, score_p1_y])

        score_p2_x = (SCREEN_WIDTH / 2) + score_p2_surface.get_rect().width + 20
        score_p2_y = SCREEN_HEIGHT - score_p2_surface.get_rect().height - 20
        SCREEN.blit(score_p2_surface, [score_p2_x, score_p2_y])

        # Draw the player and ball
        moving_sprites.draw(SCREEN)

        pygame.display.flip()
        CLOCK.tick(FPS)

play_game()
