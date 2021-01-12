import sys

if len(sys.argv) < 3:
    print("Not enough arguments.")
    sys.exit()

elif len(sys.argv) > 3:
    print("Too many arguments.")
    sys.exit()

else:
    r = float(sys.argv[1])
    h = float(sys.argv[2])

if r < 0:
    print("Radius cannot be negative.")
    sys.exit()

elif h < 0:
    print("Height cannot be negative.")
    sys.exit()

else:
    V = 3.141592*r**2*h

print("The volume of the cylinder is {0:.2f}.".format(V))
