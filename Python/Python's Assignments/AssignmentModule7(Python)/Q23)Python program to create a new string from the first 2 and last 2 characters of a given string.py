#23)Python program to create a new string from the first 2 and last 2 characters of a given string

def create_new_string(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]

input_string = input("Enter a string: ")
result = create_new_string(input_string)
print("Result:", result)
