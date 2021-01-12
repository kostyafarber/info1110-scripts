import sys
import math

w = int(sys.argv[1])
h = int(sys.argv[2])
c = float(sys.argv[3])
X1 = int(sys.argv[4])
Y1 = int(sys.argv[5])
X2 = int(sys.argv[6])
Y2 = int(sys.argv[7])

x_distance = int(math.sqrt((X2-X1)**2))
y_distance = int(math.sqrt((Y2-Y1)**2))

blocks = y_distance + x_distance
total_cost = c * blocks

if x_distance > w or y_distance > h:
    print("This place isn't on the map")

elif c == 0.00 or blocks == 0:
    print("You got a free ride and you will have travelled {0} blocks".format(blocks))

else:
    print("This trip will cost ${0:.2f} and you will have travelled {1} blocks".format(total_cost, blocks))

