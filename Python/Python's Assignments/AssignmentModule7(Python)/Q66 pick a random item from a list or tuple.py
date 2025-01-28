import random

# Sample list and tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = ('a', 'b', 'c', 'd')

# Pick a random item from the list
random_item_list = random.choice(my_list)
print(f"Random item from list: {random_item_list}")

# Pick a random item from the tuple
random_item_tuple = random.choice(my_tuple)
print(f"Random item from tuple: {random_item_tuple}")
