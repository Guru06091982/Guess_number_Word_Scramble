#take the input from the user to create list
user_input = input("Enter the integers separated by spaces: ")
items = user_input.split(" ") # Split the input into a list of strings
numbers = [] # Create a empty list

# Convert each string to an integer and add it to the list
for item in items:
    numbers.append(int(item))
    print(numbers)

#variable to store non-repeating numbers
first_non_repeat_number =  None
#Travers each element in the list
for num in numbers:
    if numbers.count(num)==1:
        first_non_repeat_number = num
        break # stop when first non-repeating numbers found

# Output
if first_non_repeat_number is not None:
    print("First non repeating Element: ", first_non_repeat_number)
else:
    print("First non repeating found")