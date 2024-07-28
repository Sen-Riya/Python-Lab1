# (5) Write a Python program to print all the even numbers and their squares
# within the given range.
# (a) range(1,50)
# (b) range(1,100)

def print_evennumbers_squares(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:  
            print(f"Number = {num} and Square of {num} = {num ** 2}")

# For range(1,50)
print("Even numbers and their squares within the range 1 to 50:")
print_evennumbers_squares(1, 50)

print("\n")

#For range(1, 100)
print("Even numbers and their squares within the range 1 to 100:")
print_evennumbers_squares(1, 100)

print("\n")
