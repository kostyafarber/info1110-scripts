import sys

arguments = sys.argv[1::]

# count check for strings
eels = 0
eel = 0
other = 0

# iterate through list and assign count to number
for s in arguments:
    if s == "eels":
        eels += 1   
    elif s == "eel":
        eel += 1
    else:
        other += 1

# control flow logic for print statements
if eels > 0 and eel > 0 and other == 0:
    print(", ".join(arguments))
    print("Wow, there are so many eels here!")
elif eels > 0 or eel > 0:
    print(", ".join(arguments))
    print("There are a few eels here.")
else:
    print(", ".join(arguments))
    print("Where are the eels?")