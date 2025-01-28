#16) Write a Python program to count the number of characters (character frequency) in a string
user_str = input("Enter a string: ")

char_count = {}

for char in user_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character frequencies in the string:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
