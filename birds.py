import pygame
from birdclass import Bird, Flock
from sys import exit
import random

pygame.init()
#create display surface...aka a screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bird Sim')
clock = pygame.time.Clock() 

bird_x_pos = 100
bird_y_pos = 100
bird_x_vel = random.randint(-10, 10)
bird_y_vel = random.randint(-10, 10)


bird = pygame.Surface((5,5))
bird.fill('White')

flock_1 = Flock()

game_running = True
while(game_running):
	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			print("Bye! Thanks for simulating!")
			exit()

	bird_x_vel = random.randint(-10, 10)
	bird_y_vel = random.randint(-10, 10)

	bird_x_pos += bird_x_vel
	bird_y_pos += bird_y_vel

	flock = flock_1.get_list_of_birds() # get the list of birds of flock 1
	#assign each bird to its x y pos
	for bird in flock:
		screen.blit(bird.get_form(), (bird.get_position()))

	pygame.display.update()
	clock.tick(60)

#Step 1: Create a white square - DONE

#Step 2: Create a number of random white squares with x y positions DONE
#2a - instantiate Bird Class and all necessary methods and attributes
#2b - instantiate a flock class... a better way to store birds than in a bird_list

#Step 3: Assign velocities to white squares so they move around

