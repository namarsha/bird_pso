import pygame

pygame.init()
#create display surface...aka a screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bird Sim')
clock = pygame.time.Clock() 

#make a big square block
def make_fading_block():
	
	block = pygame.Surface((200, 200))
	block.fill('White')



game_running = True
while(game_running):
	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			print("Bye! Thanks for simulating!")
			exit()

	#implement color decay
	screen.blit(block, (100, 100))

	pygame.display.update()
	clock.tick(60)