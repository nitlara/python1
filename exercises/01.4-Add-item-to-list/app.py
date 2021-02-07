#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
def generate_new_list():
    for i in range(0,10):
        x = random.randint(1,100)
        my_list.append(x)

generate_new_list()
print(my_list)


