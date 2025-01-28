def find_longest_words(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip() for line in file for word in line.split()]
    
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words

# Example usage
file_path = 'example.txt'
longest_words = find_longest_words(file_path)
print("Longest words:", longest_words)
