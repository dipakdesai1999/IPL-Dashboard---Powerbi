def read_file_to_variable(file_path):
    content = ""
    with open(file_path, 'r') as file:
        for line in file:
            content += line
    return content

# Example usage
file_path = 'example.txt'
file_content = read_file_to_variable(file_path)
print(file_content)
