def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Example usage
file_path = 'example.txt'
lines_list = read_file_to_list(file_path)
print(lines_list)
