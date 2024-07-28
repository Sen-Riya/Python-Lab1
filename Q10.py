# (10) Declare a list/tuple containing all the twelve months. Write a Python program that converts a month name entered via the Python console to the number of days in that month (Consider leap year as well the code):
# Expected Output:
# Enter the month name : July 
# The number of days in July is :31

# Enter the month name : February 
# Enter the year : 2024
# The number of days in February is : 29 

months = ("January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December")

days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# User input
month_name = input("Enter the month name: ").strip().title()

if month_name == "February":
    year = int(input("Enter the year: "))
    if leap_year(year):
        days = 29
    else:
        days = 28
else:
    days = days_in_month.get(month_name, "Invalid month name")

if isinstance(days, int):
    print(f"The number of days in {month_name} is: {days}")
else:
    print(days)
