import random
import pygame

class Bird():
	def __init__(self):

		self.speed_multiplier = 10 # if this number is too low, birds turn into worms

		#birds have position
		self.x_pos = random.randint(0, 800)
		self.y_pos = random.randint(0, 400)

		#they have color and size, which I abbreviate as form and are instantiated as pygame surfaces
		self.form = pygame.Surface((5,5))
		self.form.fill('White')

		#they have individual velocities in both the x and y direction; these velocities are random for now
		# self.x_vel = random.randint(-10, 10)
		# self.y_vel = random.randint(-10, 10)

		self.x_vel = random.randint(-1,1) * self.speed_multiplier
		self.y_vel = random.randint(-1,1) * self.speed_multiplier

	def get_x_velocity(self):
		return self.x_vel

	def get_y_velocity(self):
		return self.y_vel
	
	def change_velocity(self):
		self.x_vel = random.randint(-1,1) * self.speed_multiplier
		self.y_vel = random.randint(-1,1) * self.speed_multiplier

	def get_position(self):
			return (self.x_pos, self.y_pos)

		#they are also dynamic creatures so they need a setter function

	def move(self):
		#change direction 50% of the time:
		die = random.randint(1,6)
		if die >= 3:
			self.change_velocity()
		self.x_pos = self.x_pos + self.x_vel
		self.y_pos = self.y_pos + self.y_vel

	def get_form(self):
		return self.form 



class Flock():
	def __init__(self, num_birds=5):

		self.list_of_birds = []

		for i in range(num_birds):

			bird_instance = Bird()
			self.list_of_birds.append(bird_instance)

	def get_list_of_birds(self):
		return self.list_of_birds




# #make a new bird

# new_bird = Bird()
# new_bird2 = Bird()

# #get its xy position
# print(f"first bird's position is: {new_bird.get_position()}")
# print(f"second bird's position is: {new_bird2.get_position()}")


# #now try making a bunch of birds

# # list_of_birds = []

# # for i in range(10):
# # 	bird_instance = Bird()
# # 	print(f"Bird {i}'s' position is: {bird_instance.get_position()}\
# # 	 and its velocity is {bird_instance.get_x_velocity()} in the x direction and {bird_instance.get_y_velocity()} in the y direction.")
# # 	list_of_birds.append(bird_instance)



# # # Write method for getting position and velocity of a given bird--in this case the fifth bird
# # fifth_bird = list_of_birds[5]
# # print(f"Bird {fifth_bird}'s' position is: {fifth_bird.get_position()}\
# # 	 and its velocity is {fifth_bird.get_x_velocity()} in the x direction and {fifth_bird.get_y_velocity()} in the y direction.")



# #make a flock

# flock_1 = Flock()
# print(flock_1.get_list_of_birds())