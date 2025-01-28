#Creating a Dictionary from Tuples
#1.Using dict() Constructor:

tuple_list = [('name', 'Alice'), ('age', 30)]
dictionary = dict(tuple_list)

#2.Using Dictionary Comprehension:

tuple_list = [('name', 'Alice'), ('age', 30)]
dictionary = {key: value for key, value in tuple_list}
