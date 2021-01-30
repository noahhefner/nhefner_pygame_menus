"""
Pygame Menu Manager Example Program
Snake Class
"""

import pygame

pygame.init()

GREEN = [0, 255, 0]

class Snake:

    def __init__ (self, starting_pos = [0, 0], color = GREEN, block_size = 20):

        self.blocks = [starting_pos]
        self.color = color
        self.block_size = block_size

    def get_length (self):

        return len(self.blocks)

    def set_color (self, new_color):

        self.color = new_color

    def draw (self, screen):

        for block in self.blocks:

            pygame.draw.rect(screen, self.color, [block[0], block[1],
                                                  self.block_size,
                                                  self.block_size])

    def add_block (self, position):

        self.blocks.insert(0, position)

    def get_head (self):

        return [self.blocks[0][0], self.blocks[0][1]]

    def remove_tail (self):

        self.blocks.pop()

    def collides_with (self, apple):

        for block in self.blocks:

            if apple[0] in range(block[0], block[0] + self.block_size) and \
               apple[1] in range(block[1], block[1] + self.block_size):

               return True
