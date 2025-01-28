#Q22.Reverses the string if its length is a multiple of 4.

def reverse_string_if_multiple_of_four(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string


input_string = input("Enter a string: ")
result = reverse_string_if_multiple_of_four(input_string)
print("Result:", result)
