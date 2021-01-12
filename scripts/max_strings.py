import sys

# Initialise empty list
string_list = []

print("Input 3 strings and find what string is the longest")

# set up while loop to store strings and append those strings to empty list
while len(string_list) < 3:
    strings = str(input())
    string_list.append(strings)

# check for empty inputs
if '' in string_list:
    print("All strings are empty")
    sys.exit()

# check if strings are same length if not print the largest string
if len(string_list) == 3:
    if len(string_list[0]) == len(string_list[1]) == len(string_list[2]):
        print("All strings are the same length")
    else:
        max_string = max(string_list, key=len)
        print('"{0}" is the longest string'.format(max_string))

# if you need to print quotations in a print statement enclose the outside statement in '' and inside "".
