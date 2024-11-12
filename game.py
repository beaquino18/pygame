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

running = True
while running:
    # Make an instance of GameObject
    # box = GameObject(120, 300, 50, 50)
    apple = GameObject(120, 300, 'images/apple.png')

    #Look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Draw a circle
    screen.fill((255, 255, 255))
    #Draw box
    apple.render(screen)
    #Update the window
    pygame.display.flip()


