#5) Write a Python program to get the Factorial number of given numbers.

n=int(input("Enter a value : "))
fact=1
for i in range(1,n+1):
    fact*=i
    if n==i:
        print("factorial of ",i," is : ",fact)
        
