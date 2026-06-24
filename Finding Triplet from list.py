# Given list of numbers
numbers = [10,20,30,9]
target = 59 # Target Sum

found = False

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            #Caliculate the sum of triplet
            current_sum = numbers[i] + numbers[j] + numbers[k]

            #Check if the sum equals to target value
            if current_sum == target:
                print("Triplet value found: ", numbers[i], numbers[j], numbers[k])
                found = True
if not found:
    print("Triplet value not found")
    

