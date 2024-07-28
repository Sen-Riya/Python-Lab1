# (9) Write a Python program to extract the rear elements from a tuple string as depicted in the following figure:
# Input:
# ("python","learn","includehelp")
# Output:
# ["n","n","p"]

Tuple = ("python", "learn", "includehelp")
rear_elements = [word[-1] for word in Tuple]
print(rear_elements)
