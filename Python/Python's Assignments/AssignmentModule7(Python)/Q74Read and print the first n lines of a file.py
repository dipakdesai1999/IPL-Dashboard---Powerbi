def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        for _ in range(n):
            line = file.readline()
            if not line:
                break  
            print(line, end='')

# Example usage
file_path = 'example.txt'
n = 5  
read_first_n_lines(file_path, n)
