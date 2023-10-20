# snake.py

import pygame
import os
import constants
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.cell_size = constants.cell_size
        self.scale = (self.cell_size,self.cell_size)
        self.new_block =False

        # Load snake graphics
        self.head_up = pygame.image.load(os.path.join("graphics", "head_up.png")).convert_alpha()
        self.head_u = pygame.transform.scale(self.head_up,self.scale)
        self.head_down = pygame.image.load(os.path.join("graphics", "head_down.png")).convert_alpha()
        self.head_d = pygame.transform.scale(self.head_down,self.scale)
        self.head_left = pygame.image.load(os.path.join("graphics", "head_left.png")).convert_alpha()
        self.head_l= pygame.transform.scale(self.head_left,self.scale)
        self.head_right = pygame.image.load(os.path.join("graphics", "head_right.png")).convert_alpha()
        self.head_r = pygame.transform.scale(self.head_right,self.scale)

        self.tail_up = pygame.image.load(os.path.join("graphics", "tail_up.png")).convert_alpha()
        self.tail_u = pygame.transform.scale(self.tail_up,self.scale)
        self.tail_down = pygame.image.load(os.path.join("graphics", "tail_down.png")).convert_alpha()
        self.tail_d= pygame.transform.scale(self.tail_down,self.scale)
        self.tail_left = pygame.image.load(os.path.join("graphics", "tail_left.png")).convert_alpha()
        self.tail_l= pygame.transform.scale(self.tail_left,self.scale)
        self.tail_right = pygame.image.load(os.path.join("graphics", "tail_right.png")).convert_alpha()
        self.tail_r = pygame.transform.scale(self.tail_right,self.scale)

        self.body_horizontal = pygame.image.load(os.path.join("graphics", "body_horizontal.png")).convert_alpha()
        self.body_h = pygame.transform.scale(self.body_horizontal,self.scale)
        self.body_vertical = pygame.image.load(os.path.join("graphics", "body_vertical.png")).convert_alpha()
        self.body_v = pygame.transform.scale(self.body_vertical,self.scale)
        self.body_topleft = pygame.image.load(os.path.join("graphics", "body_topleft.png")).convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_topleft,self.scale)
        self.body_topright = pygame.image.load(os.path.join("graphics", "body_topright.png")).convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_topright,self.scale)
        self.body_bottomleft = pygame.image.load(os.path.join("graphics", "body_bottomleft.png")).convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bottomleft,self.scale)
        self.body_bottomright = pygame.image.load(os.path.join("graphics", "body_bottomright.png")).convert_alpha()
        self.body_br = pygame.transform.scale(self.body_bottomright,self.scale)


        # Set initial position for the snake head
        self.head_image = self.head_right
        self.head_rect = self.head_image.get_rect()
        self.head_rect.topleft = (100, 100)

        # List to store body segments
        #self.body = [self.head_rect]

        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]

        self.direction = Vector2(1,0) # right
        self.score = 0

    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
        # # Move the snake based on the current direction
        # if self.direction == pygame.K_UP:
        #     self.head_rect = self.head_rect.move(0, -30)
        #     self.head_image = self.head_up
        # elif self.direction == pygame.K_DOWN:
        #     self.head_rect = self.head_rect.move(0, 30)
        #     self.head_image = self.head_down
        # elif self.direction == pygame.K_LEFT:
        #     self.head_rect = self.head_rect.move(-30, 0)
        #     self.head_image = self.head_left
        # elif self.direction == pygame.K_RIGHT:
        #     self.head_rect = self.head_rect.move(30, 0)
        #     self.head_image = self.head_right

        # # Move the rest of the body
        # self.body.insert(0, self.head_rect)

        # # Remove the last segment if not growing
        # if len(self.body) > self.score + 1:
        #     self.body.pop()

    def grow(self):
        # Increase the size of the snake
        self.new_block = True
        self.score += 1

    def check_collision(self):
        # Check collision with walls
        if (
            self.head_rect.left < 0
            or self.head_rect.right > self.screen_width
            or self.head_rect.top < 0
            or self.head_rect.bottom > self.screen_height
        ):
            return True  # Collision with walls

        # Check collision with itself
        for segment in self.body[1:]:
            if self.head_rect.colliderect(segment):
                return True  # Collision with itself

        return False  # No collision

    def get_body_orientation(self, current_segment, previous_segment):
        # Determine the orientation of the body segment
        if current_segment.x == previous_segment.x: 
            return self.body_vertical
        elif current_segment.y == previous_segment.y:
            return self.body_horizontal
        return self.body_topleft

   
    def draw(self,screen):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            x_pos = int(block.x * self.cell_size)
            y_pos = int(block.y * self.cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,self.cell_size,self.cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index - 1] - block 
                next_block = self.body[index + 1] - block 

                if previous_block.x == next_block.x:
                    screen.blit(self.body_v,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_h,block_rect)
                elif next_block.x== -1 and previous_block.y==-1 or next_block.y== -1 and previous_block.x==-1:
                    screen.blit(self.body_tl,block_rect)
                elif next_block.x== 1 and previous_block.y==-1 or next_block.y== -1 and previous_block.x==1:
                    screen.blit(self.body_tr,block_rect)
                elif next_block.x== -1 and previous_block.y==1 or next_block.y== 1 and previous_block.x==-1:
                    screen.blit(self.body_bl,block_rect)
                elif next_block.x== 1 and previous_block.y==1 or next_block.y== 1 and previous_block.x==1:
                    screen.blit(self.body_br,block_rect)
                
            # else:
            #     pygame.draw.rect(screen,(0,114,25),block_rect)
        # screen.blit(self.head_image, self.head_rect)

        # for i in range(1,len(self.body)):
        #     segment = self.body[i]
        #     orientation = self.get_body_orientation(segment,self.body[i-1])
        #     screen.blit(orientation,segment)

    def update_head_graphics(self):
        head_rel = self.body[1] -self.body[0]
        if head_rel == Vector2(1,0):self.head = self.head_l
        elif head_rel == Vector2(-1,0):self.head = self.head_r
        elif head_rel == Vector2(0,1):self.head = self.head_u
        elif head_rel == Vector2(0,-1):self.head = self.head_d

    def update_tail_graphics(self):
        tail_rel = self.body[-2] - self.body[-1]
        if tail_rel == Vector2(1,0): self.tail = self.tail_l
        elif tail_rel == Vector2(-1,0): self.tail = self.tail_r
        elif tail_rel == Vector2(0,1): self.tail = self.tail_u
        elif tail_rel == Vector2(0,-1): self.tail = self.tail_d
        
