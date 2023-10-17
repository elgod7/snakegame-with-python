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
BLUE = pygame.Color(0,0,255)

#3.Create a Snake class to manage the snake's attributes and behavior.
class Snake:
    def __init__(self,screen_width, screen_height):
        # Initialize snake attributes (position, size, etc.)
        self.size = 1  # Initial size of the snake
        self.speed = 10  # Speed of the snake
        self.direction = 'RIGHT'  # Initial direction
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.score = 0  # Initialize score to 0

        # Initial position of the snake (you can choose any starting position)
        self.head = [100, 50]
        self.body = [[100, 50]]  # Initial body segments


    def move(self):
        if self.direction == 'UP':
            self.head[1] -= self.speed
        elif self.direction == 'DOWN':
            self.head[1] += self.speed
        elif self.direction == 'LEFT':
            self.head[0] -= self.speed
        elif self.direction == 'RIGHT':
            self.head[0] += self.speed

        # Update the body segments based on the new head position
        self.body.insert(0, list(self.head))

        # If the snake has grown, don't remove the last segment (tail)
        if len(self.body) > self.size:
            self.body.pop() 


    def grow(self):
        # Increase the size of the snake
        self.size += 1
        # Optionally, you can update other attributes or perform additional actions
        # For example, you might want to increase the player's score.
        self.score += 1  # Increment the score when the snake grows

        # You can also add more sophisticated logic for growing if needed.

    def draw(self, screen):
         # Draw the head of the snake
        pygame.draw.rect(screen, GREEN, pygame.Rect(self.head[0], self.head[1], 10, 10))

        # Draw the body segments
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], 10, 10))

    def check_collision(self):
        # Check collision with walls
        if (
            self.head[0] < 0
            or self.head[0] >= self.screen_width
            or self.head[1] < 0
            or self.head[1] >= self.screen_height
        ):
            # Snake has collided with the walls, handle game over or reset
            #self.reset()
            return True  # Collision with walls

        # Check collision with itself
        for segment in self.body[1:]:
            if self.head == segment:
                # Snake has collided with itself, handle game over or reset
                #self.reset()
                return True  # Collision with walls
            
        return False  # No collision
    
    def reset(self):
        # Reset the snake to its initial state
        self.size = 1
        self.speed = 10
        self.direction = 'RIGHT'
        self.head = [100, 50]
        self.body = [[100, 50]]

#4.Create a Food class for the snake to eat.
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



#5.Implement the main game loop.

def main():
    #Define the snake
    snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT)
    # Define the food
    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)

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
            snake.draw(screen)
            food.draw(screen)

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

main()