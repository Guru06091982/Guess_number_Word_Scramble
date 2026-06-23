num = [10,501,22,37,100,999,87,351] #Input the list containing numbers

even_num = [] # create a empty list to store even numbers
odd_num = [] # Create a empty list to store Odd numbers

for i in num: # loop each numbers from the list
    if i % 2 == 0: # Check if the number is divisible by 2
        even_num.append(i)
    else:
        odd_num.append(i)

# display the list of even and odd numbers
print("Even Numbers", even_num)
print("Odd Numbers", odd_num)