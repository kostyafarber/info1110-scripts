import sys

n = int(sys.argv[1])
num_list = []

for i in range(2,n+1):
    if i == 1:
        print(num_list)
    elif i % 2 == 0:
        num_list.append(int(i/2))
    else:
        num_list.append(int(i * 3 + 1))


