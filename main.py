import pygame
from random import randint, choice
from game_object import GameObject
from apple import Apple
from bomb import Bomb
from player import Player
from strawberry import Strawberry
from constants import lanes

pygame.init()

# Configure screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

#Change background color
background_color = (135, 206, 250)



# Instantiate all objects
apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()

# Make a group
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()

# Add fruit objects to sprite group
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)


# Game Loop
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
    
    # Set background color
    screen.fill(background_color)
    
    # Move and render Sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)
    
    #Check colisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()
    
    #Check collision player and bomb
    if pygame.sprite.collide_rect(player, bomb):
        running = False
        
    # Update the window
    pygame.display.flip()
    
    # tick the clock
    clock.tick(60)
    

