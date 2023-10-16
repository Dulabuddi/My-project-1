# Function to calculate factorials
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user the input
user_number = int(input("Enter a number to calculate its factorial: "))

# Check if the input is non-negative
if user_number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the function and display the results
    print(f"The factorial of {user_number} is {result}.")
