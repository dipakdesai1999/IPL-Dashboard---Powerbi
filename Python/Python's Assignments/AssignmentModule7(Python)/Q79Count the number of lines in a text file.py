def count_lines(file_path):
    """Count the number of lines in a text file."""
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

# Example usage
file_path = 'example.txt'
num_lines = count_lines(file_path)
print("Number of lines:", num_lines)
