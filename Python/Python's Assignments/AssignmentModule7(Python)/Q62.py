def is_in_range(number, start, end):
    return start <= number <= end

# Test the function
number = 5
start = 1
end = 10

print(f"Is {number} in the range {start} to {end}? {is_in_range(number, start, end)}")
