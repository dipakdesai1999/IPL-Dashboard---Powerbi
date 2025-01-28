def insert_in_middle(original, to_insert):
    mid = len(original) // 2
    new_string = original[:mid] + to_insert + original[mid:]
    return new_string


original_string = input("Enter the original string: ")
string_to_insert = input("Enter the string to insert: ")

result = insert_in_middle(original_string, string_to_insert)

print("Result:", result)

