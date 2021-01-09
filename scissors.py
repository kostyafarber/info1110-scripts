import sys

# initialise variables
col = int(sys.argv[1])
file = open(sys.argv[2])

# Loop through file, split lines into a list and grab the elements according to command-line input.
for s in file:
    lines = s.split()
    print(lines[col - 1])


