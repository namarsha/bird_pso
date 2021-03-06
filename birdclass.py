import random
import pygame
import numpy as np
from math import dist

class Border():
	# Border has a top, bottom, left side, and right side
	def __init__(self):
		self.top = 100
		self.bottom = 350
		self.left = 40
		self.right = 550

	def get_top(self):
		return self.top

	def get_left(self):
		return self.left

	def get_bottom(self):
		return self.bottom

	def get_right(self):
		return self.right



class Bird():
	def __init__(self, known_border):

		self.known_border = known_border

		self.speed_multiplier = .75 

		#birds have position, starting position is inside border
		self.x_pos = random.randint(self.known_border.left, self.known_border.right)
		self.y_pos = random.randint(self.known_border.top, self.known_border.bottom)

		#they have color and size, which I abbreviate as 'form' and are instantiated as pygame surfaces
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

	def reverse_direction(self):
		self.x_vel = self.x_vel * -1
		self.y_vel = self.y_vel * -1

	def get_position(self):
			return [self.x_pos, self.y_pos]

	def is_in_border(self):
		cond_1 = self.x_pos >= self.known_border.left and self.x_pos <= self.known_border.right
		cond_2 = self.y_pos >= self.known_border.top and self.y_pos <= self.known_border.bottom
		return cond_1 and cond_2

		#they are also dynamic creatures so they need a setter function

	def move(self):

		#change direction 33% of the time:
		die = random.randint(1,100)
		if die <= 5:
			self.change_velocity()
		#check for border crossing and then update:
		self.x_pos = self.x_pos + self.x_vel
		self.y_pos = self.y_pos + self.y_vel
		if not self.is_in_border():
			self.reverse_direction()

	def get_form(self):
		return self.form 

	def distance_to_all_other_birds(self, flock):
		distances = []
		list_of_birds = flock.get_list_of_birds()
		for bird in list_of_birds:
			if bird != self:
				bird_pos = bird.get_position()
				self_pos = self.get_position()

				distance = dist(bird_pos, self_pos)
				distances.append((bird, distance))
		distances = sorted(distances, key = lambda x: x[1])
		return distances

	def get_neighboring_birds(self, flock):
		k = 3 # how many neighbors to get
		distances_of_nearest_birds = self.distance_to_all_other_birds(flock)
		return distances_of_nearest_birds[:3]

	def get_average_xy_velocity_of_nearest_neighbors(self, flock, num_nearest_neighbors=3):
		average_x_velocity = 0
		average_y_velocity = 0
		distances = self.get_neighboring_birds(flock)
		for elem in distances:
			bird = elem[0] #grab the first element of each tuple, i.e. the bird object
			average_x_velocity += bird.get_x_velocity()
			average_y_velocity += bird.get_y_velocity()
		average_x_velocity = average_x_velocity / num_nearest_neighbors
		average_y_velocity = average_y_velocity / num_nearest_neighbors
		return (average_x_velocity, average_y_velocity)

	def update_velocity_according_to_nearest_neighbors(self, flock):
		update_rate = .01
		avg_vel = self.get_average_xy_velocity_of_nearest_neighbors(flock)
		self.x_vel += update_rate * avg_vel[0]
		self.y_vel += update_rate * avg_vel[1]



class Flock():
	def __init__(self, known_border, num_birds=5):

		self.list_of_birds = []

		for i in range(num_birds):

			bird_instance = Bird(known_border)
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