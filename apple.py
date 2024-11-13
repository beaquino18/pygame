import pygame
from random import randint, choice
from game_object import GameObject
from constants import lanes

# Apple object moves vertically
class Apple(GameObject):
    def __init__(self):
        x = randint(50, 400)
        super(Apple, self).__init__(0, 0, 'images/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.y > 500:
            self.reset()
    
    def reset(self):
        direction = randint(1, 4)
        
        # Lets apple object move up or down
        if direction == 3: #down
            self.x = choice(lanes)
            self.y = -64
            self.dx = 0
            self.dy = (randint(0, 200) / 100) + 1
        else:
            self.x = choice(lanes)
            self.y = 500
            self.dx = 0
        
        self.x = choice(lanes)
        self.y = -64
