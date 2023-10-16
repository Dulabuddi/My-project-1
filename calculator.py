# Initialize an empty list to store the numbers
numbers = []

# Ask the user for input
while True:
    try:
        num = float(input("Enter a number (or '0' to calculate the average): "))
        if num == 0:
            break  # Exit the loop if the user enters 0
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the average
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average:.2f}")
else:
    print("No numbers were entered.")
