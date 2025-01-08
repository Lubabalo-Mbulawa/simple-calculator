# Addition
def add(num1, num2):
    results = num1 + num2
    return results

# Subtraction
def sub(num1, num2):
    results = num1 - num2
    return results

# Multiplication
def multiply(num1, num2):
    results = num1 * num2
    return results

# Division
def div(num1, num2):
    
    if num2 == 0:
        return "You can not divide by 0"
    else:
        results = num1 / num2
        return results

# Input values
def input_value():
    operation_symbols = "+-*/"
    while True:
        operator = input("write the operator: ")
        if operator not in operation_symbols:
            print("Invalid operator. Enter a valid operator (+, -, *, /)")
            continue
        try:
            num1 = float(input("write first number: "))
            num2 = float(input("write second number: "))
        except ValueError:
            print("Please enter a valid number.")
        return operator, num1, num2

def main():
    operator, num1, num2 = input_value()
    
    if operator == "+":
        return add(num1, num2)

    elif operator == "-":
        return sub(num1, num2)

    elif operator == "*":
        return multiply(num1, num2)

    elif operator == "/":
        return div(num1, num2)

if __name__ == "__main__":
    print("Results: ",main())  
