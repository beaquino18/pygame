#Example 1: Getting started with pygame - Challenge 1

import pygame
pygame.init()

# Configure screen
screen = pygame.display.set_mode([500, 500])

circles = [
    {"color": (252, 231, 45), "pos": (250, 250)},  # yellow
    {"color": (255, 51, 51), "pos": (100, 100)},   # red
    {"color": (255, 128, 0), "pos": (400, 100)},   # orange
    {"color": (102, 255, 102), "pos": (100, 400)}, # green
    {"color": (102, 178, 255), "pos": (400, 400)}  # blue
]

# Create the game loop
running = True 
while running: 
	# Looks at events a
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# Clear the screen
	screen.fill((255, 255, 255))

	for circle in circles:
		pygame.draw.circle(screen, circle["color"], circle["pos"], 40)

	pygame.display.flip()
