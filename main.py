#TODO


#7.Implement collision detection logic for the snake hitting walls, itself, or the food.👍
#8.Keep track of the player's score (length of the snake).
#9.Implement game-over conditions and display the final score.
#10.Place food randomly on the screen when it is eaten by the snake.
#11.Optimize the code for better performance.
#12.Add comments and document your code for better understanding

#1.Import the necessary libraries (pygame and others if needed).👍
import pygame
import sys
import random

#Import snake and food classes
from snake import Snake
from food import Food


#5.Implement the main game loop.

def main():
    #2.Initialize Pygame and set up the game window.👍
    pygame.init()

    #Define Constant for Screen 
    SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    #Define Constant for Color
    BLACK = pygame.Color(0,0,0)
    WHITE = pygame.Color(255,255,255)
    RED = pygame.Color(255,0,0)
    GREEN = pygame.Color(0,255,0)
    
    #Define the snake
    snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT, GREEN)
    # Define the food
    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, random)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #6.Handle user input to control the snake.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                # Change snake direction
                    if snake.direction != "DOWN":
                        snake.direction = "UP"
                if event.key == pygame.K_DOWN:
                # Change snake direction
                    if snake.direction != "UP":
                        snake.direction = "DOWN"
                if event.key == pygame.K_LEFT:
                # Change snake direction
                    if snake.direction != "RIGHT":
                        snake.direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                # Change snake direction
                    if snake.direction != "LEFT":
                        snake.direction = "RIGHT"
        if not game_over:
            # Handle user input and update game state
            # Update game logic (snake movement, collisions, etc.)
            snake.move()
            snake.check_collision()

            # Check if the snake has eaten the food
            if snake.head == food.position:
                snake.grow()
                food.spawn_food()

            # Draw the snake and food on the screen
            screen.fill((0, 0, 0))  # Clear the screen
            snake.draw(screen,pygame)
            food.draw(screen,pygame)

            # Display the score on the screen (you can customize the position and font)
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {snake.score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            # Check game-over conditions
            if snake.check_collision():
                game_over = True

            pygame.display.flip()
            pygame.time.Clock().tick(6)  # Control the frame rate

    # Game over logic
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {snake.score}", True, (255, 255, 255))

    screen.blit(game_over_text, (SCREEN_WIDTH// 2 - 150, SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 50))

    pygame.display.flip()

    # Wait for a moment before exiting (you can adjust the time)
    pygame.time.delay(3000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()