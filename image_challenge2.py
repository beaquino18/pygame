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

apples = [
    {"pos": (150, 150)},  # top left
    {"pos": (350, 150)},  # top right
    {"pos": (250, 250)},  # center
    {"pos": (150, 350)},  # bottom left
    {"pos": (350, 350)},  # bottom right
]

strawberries = [
    {"pos": (250, 150)},  # top middle
    {"pos": (150, 250)},  # middle left
    {"pos": (350, 250)},  # middle right
    {"pos": (250, 350)},  # bottom middle
]

apple_objects = [
    GameObject(pos['pos'][0], pos["pos"][1], 'images/apple.png')
    for pos in apples
]

strawberry_objects = [
    GameObject(pos['pos'][0], pos["pos"][1], 'images/strawberry.png')
    for pos in strawberries
]

running = True
while running:
    #Look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Clear screens
    screen.fill((255, 255, 255))
    
    #Render images
    for apple in apple_objects:
        apple.render(screen)
        
    for strawberry in strawberry_objects:
        strawberry.render(screen)
        
    #Update the window
    pygame.display.flip()


