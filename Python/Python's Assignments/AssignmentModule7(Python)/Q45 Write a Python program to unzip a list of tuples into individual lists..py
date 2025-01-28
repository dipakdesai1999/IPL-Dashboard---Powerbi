#45 List of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

list1, list2 = zip(*list_of_tuples)

list1 = list(list1)
list2 = list(list2)

print("List 1:", list1)
print("List 2:", list2)
