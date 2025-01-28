# Find the highest 3 values


my_dict = {'a': 50, 'b': 200, 'c': 150, 'd': 100, 'e': 250}

highest_three = sorted(my_dict.values(), reverse=True)[:3]

print("Highest 3 values:", highest_three)
