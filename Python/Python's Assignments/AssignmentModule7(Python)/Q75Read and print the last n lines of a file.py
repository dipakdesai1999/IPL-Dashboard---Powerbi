def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Get the last n lines
    last_n_lines = lines[-n:] if n <= len(lines) else lines

    # Print each line
    for line in last_n_lines:
        print(line, end='')

# Example usage
file_path = 'example.txt'
n = 3  # Number of lines to read from the end
read_last_n_lines(file_path, n)
