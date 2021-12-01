import pygame
from birdclass import Bird, Flock, Border
from sys import exit
import random

pygame.init()
#create display surface...aka a screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bird Sim')
clock = pygame.time.Clock() 



border = Border()
flock_1 = Flock(border, 250)

Color_line=(255,0,0)

game_running = True
while(game_running):
	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			print("Bye! Thanks for simulating!")
			exit()

	pygame.draw.line(screen,Color_line,(border.get_left(), border.get_top()),(border.get_right(), border.get_top()))
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

#Step 5: Create border on screen. Border will be class object. DONE
#5a: birds are escaping border. Diagnose and correct. -- quick fix: alter speed multiplier so that birds have less of a chance of inadvertently jumping the border


#Step 5: Start to implement actual swarm techniques. 
#5a implement euclidean distance between birds. DONE
#5b: identify nearest neighbor based on euclidean distance... 
	#I can see this already getting rather complex. Is it the case that every bird must have an awareness of every other bird? If so, every
	#bird's memory is a effectively a len(flock - 1) long vector... so, for 350 birds, I'll have to track 350**2 distances...


#Step 6: When birds move, they adjust their velocity based on the closest three birds to them. 
