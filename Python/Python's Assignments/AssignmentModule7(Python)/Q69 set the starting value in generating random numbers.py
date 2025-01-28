import random


random.seed(42)

random_integer = random.randint(1, 10)
random_float = random.random()

print(f"Random integer with seed 42: {random_integer}")
print(f"Random float with seed 42: {random_float}")
