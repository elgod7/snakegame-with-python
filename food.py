#4.Create a Food class for the snake to eat.
import random
import pygame
class Food:
    def __init__(self, screen_width, screen_height):
        self.position = [0, 0]
        self.size = 10
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = (255, 0, 0)  # Red color for the food
    

        # Place the initial food on the screen
        self.spawn_food()

    def spawn_food(self):
        # Generate random coordinates for the food
        x = random.randrange(0, self.screen_width - self.size, self.size)
        y = random.randrange(0, self.screen_height - self.size, self.size)

        self.position = [x, y]

    def draw(self, screen):
        # Draw the food on the screen
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.size, self.size))
