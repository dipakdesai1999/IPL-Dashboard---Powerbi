#12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
a=int(input("Enter Value Of A: "))
b=int(input("Enter Value Of B: "))
c=int(input("Enter Value Of C: "))
add=a+b+c
if a==b or b==c or a==c:
    print("Addition: ",0)
else:
    print("Addition: ",add)
