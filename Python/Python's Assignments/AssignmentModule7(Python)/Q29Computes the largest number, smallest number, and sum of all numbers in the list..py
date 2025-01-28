#Q.29)Computes the largest number, smallest number, and sum of all numbers in the list.


def list_statistics(numbers):
    if not numbers:
        return (None, None, 0) 
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)

    return (largest, smallest, total_sum)

# Example usage
my_list = [4, 2, 9, 7, 5]
largest, smallest, total_sum = list_statistics(my_list)

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", total_sum)
