
my_dict = {'name': 'Dipak', 'age': 30, 'city': 'New delhi'}

keys_to_check = ['name', 'age']

if set(keys_to_check).issubset(my_dict):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
