#Q35.Generate and print first and last 5 squares from 1 to 30

squares = [i**2 for i in range(1, 31)]
print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])
