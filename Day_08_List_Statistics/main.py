numbers_list = []
print("Enter a list of five numbers.")
for i in range(1,6):
    n = int(input(f"Enter number {i}: "))
    numbers_list.append(n)

# Negative Numbers
if any(n < 0 for  n in numbers_list):
    print("Yes, the list contains negative numbers.")
else:
    print("There is no negative number in the list.")

# Maximum Number in List
max_num = max(numbers_list)
print(f"The maximum number in the list is: {max_num}")

# Minimum Number in List
min_num = min(numbers_list)
print(f"The minimum number in the list is: {min_num}") 

# Sum of all numbers in list
sum_num = sum(numbers_list)
print(f"Sum of all the numbers in the list is: {sum_num}")

# Range of list
list_range = max_num - min_num
print(f"Range of the list is: {list_range}")

# Average 
average = sum_num/ len(numbers_list)
print(f"Average of the list is: {average}")


