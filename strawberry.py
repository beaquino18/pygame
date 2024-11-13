import pygame
from game_object import GameObject
from constants import lanes
from random import randint, choice

# Stawberry object moves horizontally
class Strawberry(GameObject):
    def __init__(self):
        y = randint(50, 400)
        super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
        self.dx = (randint(50, 200) / 100) + 1
        self.dy = 0
        self.reset()
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500:
            self.reset()
    
    def reset(self):
        direction = randint(1, 4)
        
        # Lets strawberry object move left or right
        if direction == 1: #left
            self.x = -64
            self.y = choice(lanes)
            self.dx = (randint(0, 200) / 100) + 1
            self.dy = 0
        elif direction == 2: #right
            self.x = 500
            self.y = choice(lanes)
            self.dx = (randint(0, 200) / 100) * -1
            self.dy = 0
        
        # self.x = -64
        # self.y = choice(lanes)
