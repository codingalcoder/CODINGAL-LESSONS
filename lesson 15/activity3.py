def add (P,Q):
    return P + Q
def substract (P,Q):
    return P - Q
def multiply (P,Q):
    return P * Q
def divide (P,Q):
    return P / Q
e = input(")Type for your operation for - Add (type a))substract (type b)Multiply (type c)Divide (type d)")
choice = input("Please enter your choice (a/b/c/d):")
num_1 = int(input("Please enter the first number :"))
num_2 = int(input("Please enter the second number :"))
if choice == 'a':
    print(num_1, "+" ,num_2,"=",add(num_1, num_2))

elif choice == 'b':
    print(num_1, "-" ,num_2,"=",substract(num_1, num_2))

elif choice == 'c' :
    print(num_1, "*" ,num_2,"=",multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/" ,num_2,"=",divide(num_1, num_2))
else:
    print("this is invalid input")
