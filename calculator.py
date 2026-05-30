
def add(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    if y == 0:
        raise ValueError("cannot be divided by zero.")
    return x / y


while True:
    try:
        num1 = int(input("Enter first number: "))
        op = input("Choose an operator (*, -, +, /): ")
        num2 = int(input("Enter second number: "))
        
        if op == "+":
            result = add(num1, num2)

        elif op == "/":
            result = division(num1, num2)

        elif op == "-":
            result = subtraction(num1, num2)

        elif op == "*":
            result = multiplication(num1, num2)

        else:
            print('invalid operator')
            continue

        print(f"Result: {num1} {op} {num2} = {result}")
        break

    except ValueError:
        print("Enter a  valid number.")