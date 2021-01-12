import sys

if len(sys.argv) == 1:
    print("No arguments")
    sys.exit()

elif len(sys.argv) > 3:
    print("Too many arguments")
    sys.exit()

elif len(sys.argv) < 3:
    print("Too few arguments")
    sys.exit()

width = int(sys.argv[1])
height = int(sys.argv[2])

if width < 0 and height < 0:
    print("Negative dimensions")
    sys.exit()

elif width < 0:
    print("Negative width")
    sys.exit()

elif height < 0:
    print("Negative height")
    sys.exit()

for n in range(1,height+1):
    print("*"*width)