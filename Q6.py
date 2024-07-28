# (6) Write a Python program to read a four-digit number and find its
# (a) Sum of digits
# (b) Reverse

#Sum of Four digit Number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# To reverse 
def reverse_number(number):
    return int(str(number)[::-1])

# Input and check if its 4 digits or not 
number = int(input("Enter a four-digit number: "))

if 1000 <= number <= 9999:
    sum_digits = sum_of_digits(number)
    
    reversed_number = reverse_number(number)
    
    print(f"The sum of the digits of {number} is: {sum_digits}")
    print(f"The reverse of {number} is: {reversed_number}")
else:
    print("Please enter a four-digit number.")

