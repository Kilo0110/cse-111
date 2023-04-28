import math
import datetime


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


tire_width = get_positive_integer("Enter the width of the tire: ")
aspect_ratio = get_positive_integer("Enter the aspect ratio of the tire: ")
diameter = get_positive_integer(
    "Enter the diameter of the tire: ")

# Calculate the volume
volume = (math.pi * tire_width**2 * aspect_ratio *
          (tire_width * aspect_ratio + 2540 * diameter)) / 10000000000

# Output the result
print(f"The approximate {volume:.2f} is cubic cm.")


# Ask user if they want to buy tires
buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ")

if buy_tires.lower() == "yes":
    # Ask for phone number
    phone_number = input("Please enter your phone number: ")

    # Get current date
    current_date = datetime.datetime.now().strftime("[%Y-%m-%d]")

    # Append data to file
    with open("volumes.txt", "a") as f:
        f.write(f"{current_date} - Tire Width: {tire_width}, Aspect Ratio: {aspect_ratio}, Diameter: {diameter}, Volume: {volume:.2f}, Phone Number: {phone_number}\n")
elif buy_tires.lower() == "no":
    # Get current date
    current_date = datetime.datetime.now().strftime("[%Y-%m-%d]")

    # Append data to file
    with open("volumes.txt", "a") as f:
        f.write(f"{current_date} - Tire Width: {tire_width}, Aspect Ratio: {aspect_ratio}, Diameter: {diameter}, Volume: {volume:.2f}\n")

else:
    print("You have inputed a wrong option")
    exit()
