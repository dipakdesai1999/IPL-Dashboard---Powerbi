#Checks if two lists have at least one common member.

def have_common_member(list1, list2):
    
    return bool(set(list1) & set(list2))

# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 5, 6]

print("Do the lists have at least one common member?", have_common_member(list1, list2))
