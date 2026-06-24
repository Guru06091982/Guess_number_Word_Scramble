# Define three lists
list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80]
list3 = [20, 30, 40, 90, 100]

# Define empty list to store duplicates

Duplicates = []

#Check the elements present in the all the lists
for item in list1:
    if item in list2 and item in list3:
        Duplicates.append(item)

print("Duplicates Elements: ", Duplicates)
print("Count:", len(Duplicates))

