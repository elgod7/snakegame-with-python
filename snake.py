#3.Create a Snake class to manage the snake's attributes and behavior.
class Snake:
    def __init__(self,screen_width, screen_height, snake_color):
        # Initialize snake attributes (position, size, etc.)
        self.size = 1  # Initial size of the snake
        self.speed = 10  # Speed of the snake
        self.direction = 'RIGHT'  # Initial direction
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.score = 0  # Initialize score to 0
        self.color = snake_color  

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

    def draw(self, screen, pygame):
        # Create a surface for the head
        head_surface = pygame.Surface((10, 10))
        head_surface.fill(self.color)  # Snake color
        screen.blit(head_surface, (self.head[0], self.head[1]))

        # Create a surface for the body segments
        body_surface = pygame.Surface((10, 10))
        body_surface.fill(self.color)  # Snake color
        for segment in self.body[1:]:
            screen.blit(body_surface, (segment[0], segment[1]))

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
