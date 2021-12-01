from birdclass import Bird, Flock, Border


border = Border()

flock1 = Flock(border)

boid = flock1.get_list_of_birds()[1]

boid.get_neighboring_birds(flock1)

print(boid.get_average_xy_velocity_of_nearest_neighbors(flock1))