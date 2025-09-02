# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Pre-calculate all operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

# Display all results
print("You entered:", num1, operation, num2)
print("Addition:      ", num1, "+", num2, "=", add)
print("Subtraction:   ", num1, "-", num2, "=", sub)
print("Multiplication:", num1, "*", num2, "=", mul)
print("Division:      ", num1, "/", num2, "=", div)