# (4) Write a Python program to convert the given list to a list of dictionaries.
# ListColour= ["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000","800000", "FFFF00"]
# Expected Output: {'colorName': 'Black', 'colorCode': '000000'}, {'color-Name': 'Red', 'colorCode': 'FF0000'}, {'colorName': 'Maroon', 'colorCode':# '800000'}, {'colorName': 'Yellow', 'colorCode': 'FFFF00'}

listColour = [["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000", "800000", "FFFF00"]]
pair_of_colours = zip(listColour[0], listColour[1])
result = [{'colorName': name, 'colorCode': code} for name, code in pair_of_colours]
for color_dict in result :
    print(color_dict)



