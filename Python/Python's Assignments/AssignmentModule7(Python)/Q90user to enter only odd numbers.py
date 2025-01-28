def get_odd_number():
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("The number is even, not odd.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        print(f"Thank you! You entered the odd number {num}.")
    finally:
        print("Program execution completed.")

# Example usage
get_odd_number()
