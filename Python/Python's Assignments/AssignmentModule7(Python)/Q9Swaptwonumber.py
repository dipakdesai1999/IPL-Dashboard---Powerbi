#9) Write python program that swap two number with temp variable and without temp variable.
a=int(input("Enter A : "))
b=int(input("Enter B : "))

temp = a
a = b
b = temp
print("After Swapping: a =", a,"b =", b)
