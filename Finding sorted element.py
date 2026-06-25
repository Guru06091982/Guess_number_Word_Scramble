# Take input from the user
user_input = input("Enter elements separated by spaces: ")

# Split the input into individual values
elements = user_input.split()

# Create an empty list
arr = []

# Convert each element to an integer and store it in the list
for element in elements:
    arr.append(int(element))

# Assume first element is minimum
minimum = arr[0]

# Traverse the list
for num in arr:
    if num < minimum:
        minimum = num

# Display minimum element
print("Minimum element:", minimum)