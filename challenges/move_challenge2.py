import pygame
from random import randint, choice
pygame.init()

#Configure screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

#Define lanes
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
        

apple = Apple()
strawberry = Strawberry()

running = True
while running:
    #Look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Clear screen
    screen.fill((255, 255, 255))
    
    #Draw apple
    apple.move()
    apple.render(screen)
    
    strawberry.move()
    strawberry.render(screen)
    
    #Update the window
    pygame.display.flip()
    
    # tick the clock
    clock.tick(30)
    




