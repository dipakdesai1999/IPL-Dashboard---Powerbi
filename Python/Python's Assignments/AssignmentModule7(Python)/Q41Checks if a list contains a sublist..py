#41 Checks if a list contains a sublist.
def contains_sublist(main_list, sub_list):
    return str(sub_list) in str(main_list)

# Example usage
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4]
print("Contains sublist:", contains_sublist(main_list, sub_list))  # Output: True

# Test with a sublist not present
sub_list = [7, 8]
print("Contains sublist:", contains_sublist(main_list, sub_list))  # Output: False
