# Function to check whether a number is a happy number or not
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)

        # Calculate sum of squares of digits
        num = sum(int(digit) ** 2 for digit in str(num))

    return num == 1

happy_numbers = [] # list to store happy numbers
for num in numbers: # Check each number in the list
    if is_happy_number(num):
        happy_numbers.append(num)

print("Happy Numbers: ", happy_numbers)
print("Count Happy numbers: ", len(happy_numbers))











