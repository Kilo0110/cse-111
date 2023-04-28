import math

# Get the number of manufactured items from the user
num_of_items = int(input("Enter the number of manufactured items: "))

# Get the number of items per box from the user
items_per_box = int(input("Enter the number of items per box: "))

# Compute the number of boxes needed
num_0f_boxes = math.ceil(num_of_items / items_per_box)

# Print the result
print(f"For {num_of_items} items. packing {items_per_box} items in each box, you will need {num_0f_boxes} boxes.")
