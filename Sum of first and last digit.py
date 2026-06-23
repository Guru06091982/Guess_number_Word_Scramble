# take the input from the user
num = int(input("Enter a number: "))

# if the number is negative convert that into positive
num = abs(num)

# use modulo operator to find last digit
last_digit = num % 10

# Find the first digit
first_digit = num
while first_digit >=10:
    first_digit = first_digit // 10

#Caliculate the sum of first and last digits
sum_of_digits = first_digit + last_digit

print("First Digit", first_digit)
print("Last Digit", last_digit)
print("Sum of digits", sum_of_digits)

