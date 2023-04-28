import math


def get_positive_integer(prompt):
    """
    Purpose: Make sure the user only inputs a positive integer and continually runs a loop when the user doesn't
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Error: Please enter a positive integer.")
# end def


width = get_positive_integer("Enter the width of the tire: ")
aspect_ratio = get_positive_integer("Enter the aspect ratio of the tire: ")
diameter = get_positive_integer(
    "Enter the diameter of the tire: ")

# Calculate the volume
volume = (math.pi * width**2 * aspect_ratio *
          (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Output the result
print(f"The approximate {volume:.2f} is cubic cm.")
