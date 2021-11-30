import pygame
from birdclass import Bird, Flock
from sys import exit
import random

pygame.init()
#create display surface...aka a screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bird Sim')
clock = pygame.time.Clock() 


flock_1 = Flock()

game_running = True
while(game_running):
	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			print("Bye! Thanks for simulating!")
			exit()

	flock = flock_1.get_list_of_birds() # get the list of birds of flock 1
	#assign each bird to its x y pos
	for bird in flock:
		bird.move()
		screen.blit(bird.get_form(), (bird.get_position()))

	pygame.display.update()
	screen.fill([0, 0, 0])	
	clock.tick(60)

#Step 1: Create a white square - DONE

#Step 2: Create a number of random white squares with x y positions -  DONE
#2a - instantiate Bird Class and all necessary methods and attributes
#2b - instantiate a flock class... a better way to store birds than in a bird_list

#Step 3: Assign velocities to white squares so they move around - DONE

#Step 4: Update screen with black background so that birds don't become worms. DONE 
#LATER: Improve movement and update image so that squares fade over time

#Step 5: 


#Step 5: Start to implement actual swarm techniques. 
#5a implement euclidean distance between birds.

