#CALCULATOR

a = int(input("Enter a: "))
b = int(input("Enter b: "))

operator = input("Enter operator: ")

if operator == '+':
    print("sum of a + b is: ", a+b)
elif operator == '-':
    print("Subtraction of a - b is: " , a-b)
elif operator == '*':
    print("Multification of a * b is: ", a*b)
elif operator == '%':
    print("Modulus of a % b is: ", a % b)
elif operator == '**':
    print("a power b is: ", a ** b)
else:
    print("Invalid choice")