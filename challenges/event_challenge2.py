# Handling event challenge 2: Player can only move to one of the intersections of
# the lanes that the apples and strawberries move along

import pygame
from random import randint, choice
pygame.init()

#Configure screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

lanes = [93, 218, 343]

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        
    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))
        
        
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
        #Check the y position of the apple
        if self.y > 500:
            self.reset()
    
    def reset(self):
        self.x = choice(lanes)
        self.y = -64

class Strawberry(GameObject):
    def __init__(self):
        y = randint(50, 400)
        super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        #Check the y position of the apple
        if self.x > 500:
            self.reset()
    
    def reset(self):
        self.x = -64
        self.y = choice(lanes)

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'images/player.png')
        self.lanes = lanes
        self.current_lane_x = 1 #this is index 1 of lane so, this is 218
        self.current_lane_y = 1
        self.reset()

    # Don't allow moving past left edge & move left one lane
    def left(self):
        if self.current_lane_x > 0:
            self.current_lane_x -= 1
            self.dx = self.lanes[self.current_lane_x]

    # Don't allow moving past right edge
    def right(self):
        if self.current_lane_x < len(self.lanes) - 1:
            self.current_lane_x += 1
            self.dx = self.lanes[self.current_lane_x]

    # Don't allow moving past top edge
    def up(self):
        if self.current_lane_y > 0:
            self.current_lane_y -= 1
            self.dy = self.lanes[self.current_lane_y]

    # Don't allow moving past bottom edge
    def down(self):
        if self.current_lane_y < len(self.lanes) - 1:
            self.current_lane_y += 1
            self.dy = self.lanes[self.current_lane_y]

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        #Start at center position
        self.current_lane_x = 1
        self.current_lane_y = 1
        self.x = self.lanes[self.current_lane_x]
        self.y = self.lanes[self.current_lane_y]
        self.dx = self.x
        self.dy = self.y


apple = Apple()
strawberry = Strawberry()
player = Player()

running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
    
    #Clear screen
    screen.fill((255, 255, 255))
    
    #Draw apple
    apple.move()
    apple.render(screen)
    
    #Draw strawberries
    strawberry.move()
    strawberry.render(screen)
    
    #Draw player
    player.move()
    player.render(screen)
    
    #Update the window
    pygame.display.flip()
    
    # tick the clock
    clock.tick(30)
    




