def write_list_to_file(file_path, data_list):
    """Write each item of a list to a file, each on a new line."""
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

# Example usage
file_path = 'output.txt'
data_list = ['apple', 'banana', 'cherry']
write_list_to_file(file_path, data_list)
