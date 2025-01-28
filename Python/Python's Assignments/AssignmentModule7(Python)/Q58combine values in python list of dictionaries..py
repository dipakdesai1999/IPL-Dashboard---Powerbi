from collections import Counter

# List of dictionaries
list_of_dicts = [
    {'item': 'apple', 'quantity': 10},
    {'item': 'banana', 'quantity': 20},
    {'item': 'apple', 'quantity': 15},
    {'item': 'orange', 'quantity': 5},
    {'item': 'banana', 'quantity': 10}
]

combined_dict = Counter()

for d in list_of_dicts:
    combined_dict[d['item']] += d['quantity']

print("Combined Dictionary:", dict(combined_dict))
