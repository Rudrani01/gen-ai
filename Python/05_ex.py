# Calculator

a = float(input("a: "))
b = float(input("b: "))
op = input("Enter operator (+, -, *, /, *, **)")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == "**":
    print(a ** b)
else:
    print("Invalid Operation")