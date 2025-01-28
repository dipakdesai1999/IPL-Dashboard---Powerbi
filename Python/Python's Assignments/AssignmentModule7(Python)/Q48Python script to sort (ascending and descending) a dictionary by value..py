#Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'apple': 10, 'banana': 5, 'cherry': 7, 'date': 15}

sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by value (ascending):", sorted_asc)

sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by value (descending):", sorted_desc)
