import pygame
from game_object import GameObject
from random import randint, choice
from constants import lanes

        
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'images/player.png')
        self.dx = 0
        self.dy = 0
        self.pos_x = 1 #this is index 1 of lane so, this is 218
        self.pos_y = 1
        self.reset()

    # Don't allow moving past left edge & move left one lane
    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    # Don't allow moving past right edge
    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    # Don't allow moving past top edge
    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    # Don't allow moving past bottom edge
    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        #Start at center position
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y
    
    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]
