# (1) Declare a python datatype list and do the following:
# (a) Write a Python program to sum all the items of the list.
# (b) Write a Python program to multiply all the items.
# (c) Write a Python program to get the largest number from a list.
# (d) Write a Python program to get the smallest number from a list.

numbers = [31, 42, 53, 74, 85,20]

# Sum 
def sum_list(numbers):
    return sum(numbers)

# Product
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Largest 
def largest_number(numbers):
    return max(numbers)

# Smallest
def smallest_number(numbers):
    return min(numbers)


print("The Sum of all the numbers in the list is :", sum_list(numbers))
print("The Product of all the numbers in the list is :", multiply_list(numbers))
print("Largest number in the list is :", largest_number(numbers))
print("Smallest number in the list is :", smallest_number(numbers))
