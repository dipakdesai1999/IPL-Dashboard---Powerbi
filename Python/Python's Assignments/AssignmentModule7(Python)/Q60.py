from collections import Counter

input_string = 'w3resource'

char_count = Counter(input_string)

result_dict = dict(char_count)

print("Dictionary of character counts:", result_dict)
