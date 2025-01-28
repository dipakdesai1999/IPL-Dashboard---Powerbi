#39.Finds the second smallest number in a list

def second_smallest(lst):
    return sorted(set(lst))[1] if len(set(lst)) > 1 else None

# Example usage
numbers = [7, 5, 9, 1, 5, 7]
print("Second smallest number:", second_smallest(numbers))
