# Python program to calculate the area of a rectangle

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_rectangle_area(length, width)

# Display the result
print("The area of the rectangle is:", area)
