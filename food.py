# food.py

import pygame
import random
import os
import constants
from pygame.math import Vector2

class Food:
    def __init__(self):
        self.cell_size = constants.cell_size
        self.cell_number = constants.cell_number

        # Spawn the initial food position
        self.spawn_food()
        self.scale = (self.cell_size,self.cell_size)

        # Load food image
        self.image = pygame.image.load(os.path.join("graphics", "apple.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.scale)
        self.image_off = self.image
        self.image_off.set_alpha(100)
        self.food = self.image

    def spawn_food(self):
        # Generate a random position for the food
        self.x = random.randint(0, self.cell_number-1)
        self.y = random.randint(1, self.cell_number-1)
        self.pos = Vector2(self.x,self.y)

    def draw(self, screen): 
        # Create a rect to represent the food's position
        self.rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y *self.cell_size, self.cell_size, self.cell_size)
        # Draw the food on the screen
        #pygame.draw.rect(screen,(25,0,0),self.rect)
      
        screen.blit(self.food,self.rect.topleft)
        
