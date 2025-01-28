import random

# Define a range
my_range = range(1, 10)  # Range from 1 to 9

# Convert range to list and pick a random item
random_item = random.choice(list(my_range))
print(f"Random item from range: {random_item}")
