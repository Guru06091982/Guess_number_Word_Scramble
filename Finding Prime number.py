# input the list containing numbers
numbers = [10,22,501,37,999,351,87,100]
prime_num =[] # Empty list to store numbers
for num in numbers: # loop through each number from the list
    if num > 1: # If the prime number is greater than one
        is_prime = True # Assume the number is prime
        for i in range (2, int(num ** 0.5) + 1): # check divisible by two to Square root of num
            if num % i == 0:
                is_prime = False
                break
        if is_prime: #if the number is prime add that it into empty list
            prime_num.append(num)

print ("Prime Numbers", prime_num)
print("Count of prime numbers", len(prime_num)) # Display the count of prime numbers
