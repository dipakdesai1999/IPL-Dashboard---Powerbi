from collections import Counter
import re

def count_word_frequency(file_path):
    """Count the frequency of each word in a text file."""
    with open(file_path, 'r') as file:
        # Read the entire file content
        text = file.read()
        
        # Use regular expressions to find words
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Count word frequency using Counter
        word_counts = Counter(words)
    
    return word_counts

# Example usage
file_path = 'example.txt'
word_frequencies = count_word_frequency(file_path)
print("Word frequencies:", word_frequencies)
