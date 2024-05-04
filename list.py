# Define a sample list
sample_list = [1, 2, 3, 4, 5]

# 1. len(): Returns the length of the list
print("Length of the list:", len(sample_list))

# 2. append(): Adds an element to the end of the list
sample_list.append(6)
print("List after appending 6:", sample_list)

# 3. extend(): Adds all elements of a list to another list
extension_list = [7, 8, 9]
sample_list.extend(extension_list)
print("List after extending with [7, 8, 9]:", sample_list)

# 4. insert(): Inserts an element at a specified position
sample_list.insert(2, 10)
print("List after inserting 10 at index 2:", sample_list)

# 5. remove(): Removes the first occurrence of a specified value
sample_list.remove(3)
print("List after removing the first occurrence of 3:", sample_list)

# 6. pop(): Removes the element at a specified position (or the last element if no position is specified) and returns it
popped_element = sample_list.pop(2)
print("Popped element at index 2:", popped_element)
print("List after popping element at index 2:", sample_list)

# 7. index(): Returns the index of the first occurrence of a specified value
index_of_5 = sample_list.index(5)
print("Index of 5 in the list:", index_of_5)

# 8. count(): Returns the number of occurrences of a specified value in the list
count_of_5 = sample_list.count(5)
print("Number of occurrences of 5 in the list:", count_of_5)

# 9. sort(): Sorts the list in ascending order
sample_list.sort()
print("Sorted list:", sample_list)

# 10. reverse(): Reverses the elements of the list in place
sample_list.reverse()
print("Reversed list:", sample_list)

# 11. clear(): Removes all elements from the list
sample_list.clear()
print("List after clearing:", sample_list)
