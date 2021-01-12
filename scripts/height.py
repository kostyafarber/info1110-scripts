import sys

h = float(sys.argv[1])

cent = h * 100

print(int(cent), "cm")

feet = cent/30.48
inches = cent % 30.48 / 2.54

print(int(feet), "ft", int(inches), "in")