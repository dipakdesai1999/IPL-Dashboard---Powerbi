#31)Counts the number of strings where the string length is 2 or more and the first and last characters are the same.

def count_special_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
            
    return count

# Example usage
string_list = ['aba', 'xyx', 'a', 'abcd', 'bbb', 'xyz']
result = count_special_strings(string_list)

print("Count of special strings:", result)
