# (2) Let A=[‘abc’, ‘xyz’, ‘aba’, 1221’] be a given string, and write a Python
# program that prints the string or strings and their index from the given list,
# ensuring that the first and last characters of the strings to be printed are
# identical.
A = ['abc', 'xyz', 'aba', '1221']


def print_strings(strings):
    for index, string in enumerate(strings):
        if string[0] == string[-1]:  
            print(f"Index: {index}, String: '{string}'")

print_strings(A)




