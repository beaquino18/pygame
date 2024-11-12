import pygame
pygame.init()

#Configure screen
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        
    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

strawberry = GameObject(120, 300, 'images/strawberry.png')

running = True
while running:
    #Look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Draw a circle
    screen.fill((255, 255, 255))
    #Draw box
    strawberry.render(screen)
    #Update the window
    pygame.display.flip()


