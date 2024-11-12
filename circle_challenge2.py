#Exercise 1 Challenge 2: 3 by 3 grey circle
import pygame
pygame.init()

# Configure screen
screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    for i in range(0,9):
        color = (96, 96, 96)
        x = ((i % 3) * 175) + 75
        y = (int(i / 3) * 175) + 75
        position = (x, y)
        
        pygame.draw.circle(screen, color, position, 40)
    
    pygame.display.flip()

