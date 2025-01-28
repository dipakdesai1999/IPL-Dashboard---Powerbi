def copy_file_contents(source_path, destination_path):
    """Copy contents from the source file to the destination file."""
    with open(source_path, 'r') as source_file:
        contents = source_file.read()
    
    with open(destination_path, 'w') as destination_file:
        destination_file.write(contents)

# Example usage
source_path = 'source.txt'
destination_path = 'destination.txt'
copy_file_contents(source_path, destination_path)
