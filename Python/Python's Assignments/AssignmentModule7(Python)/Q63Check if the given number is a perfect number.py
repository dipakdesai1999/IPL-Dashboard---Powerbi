def is_perfect(number):
    if number <= 0:
        return False

    sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
    
    return sum_of_divisors == number

number = 28
print(f"Is {number} a perfect number? {is_perfect(number)}")
