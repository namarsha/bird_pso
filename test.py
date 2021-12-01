from birdclass import Bird, Flock, Border


border = Border()

flock1 = Flock(border)
print(str(flock1.get_list_of_birds()))

boid = flock1.get_list_of_birds()[1]

boid.distance_to_all_other_birds(flock1)
