# (3) Write a python program to print patterns given below:
#         A                                  *
#       A   B                                * *
#     A   B   C                              * * *
#   A   B   C   D                            * * * *
# A   B   C   D   E                          * * * * *

def alphabet_pattern(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print("  ", end="")
        for j in range(i + 1):
            print(chr(65 + j), end="   ")
        print()
rows = 5
alphabet_pattern(rows)

def star_pattern(rows):
    for i in range (rows):
        for j in range (rows -i -1):
            print(end="")
        for j in range (i+1):
            print("*",end="")
        print()
rows=5
star_pattern(rows)

