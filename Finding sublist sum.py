# list given in the task
numbers = [4,2,-3,1,6]
# Flag to indicate zero-sum exits in the sub-lists
found = False
# To check all possible sub-lists, and make current_sum equals to zero
for i in range(len(numbers)):
    current_sum = 0
    for j in range(i, len(numbers)):
        current_sum += numbers[j] # Adding current element to the sum

        # Check if sum equals to zero
        if current_sum == 0:
            print("Sub-lists with sum zero found: ", numbers[i:j+1])
            #print(numbers[i:j+1])
            found = True

    if found:
        break

if not found:
    print("No Sub-lists with sum zero found: ")
