#6) Write a Python program to get the Fibonacci series of given range.
n=int(input("Enter N: "))
a,b=0,1
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b
