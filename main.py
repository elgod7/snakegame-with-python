# main.py

import pygame
import sys
from snake import Snake
from food import Food
from constants import cell_size,cell_number
from pygame.math import Vector2

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
    
    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail()

    def draw_element(self,screen):
        self.food.draw(screen)
        self.snake.draw(screen)

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.spawn_food()
            self.snake.grow()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
          # Game over logic
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {self.snake.score}", True, (255, 255, 255))

        screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 50))
        screen.blit(score_text, (screen_width // 2 - 180, screen_height // 2 + 50))

        pygame.display.flip()

        # Wait for a moment before exiting (you can adjust the time)
        pygame.time.delay(3000)

        pygame.quit()
        sys.exit()

# Set up the screen
screen_width = cell_number * cell_size
screen_height = cell_number * cell_size
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

def main():
    
    # Load background image
    background = pygame.image.load("graphics/background.jpeg")
    background = pygame.transform.scale(background, (screen_width, screen_height))

    clock = pygame.time.Clock()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,150)

    main_game = Game()

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and main_game.snake.direction != (0,1):
                    main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_DOWN and main_game.snake.direction != (0,-1):
                    main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT and main_game.snake.direction != (1,0):
                    main_game.snake.direction = Vector2(-1,0)
                if event.key == pygame.K_RIGHT and main_game.snake.direction != (-1,0):
                    main_game.snake.direction = Vector2(1,0)

        if not game_over:

            screen.fill((175,215,70))
            main_game.draw_element(screen)
            pygame.display.flip()

        clock.tick(60)  # Control the frame rate


if __name__ == "__main__":
    main()
