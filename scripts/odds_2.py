import sys

# check flag -a

if str(sys.argv[1]) == "-a":
    for num in range(1,100):
        print(num)

# check flag -d

elif str(sys.argv[1]) == "-d":
    for num in reversed(range(1,100)):
        print(num)

# if user is an idiot
else:
    print("Please input the correct flag!")

