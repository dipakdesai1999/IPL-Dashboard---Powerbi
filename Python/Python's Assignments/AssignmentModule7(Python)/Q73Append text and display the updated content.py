file_path = 'example.txt'
text_to_append = "This is the appended text.\n"

# Append text and display the updated content
with open(file_path, 'a') as file:
    file.write(text_to_append)

with open(file_path, 'r') as file:
    print("Updated file content:")
    print(file.read())
