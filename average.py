# initialise empty list to store user integers

num_list = []

# create while loop to keep asking user for integers

while 0 not in num_list:
    num = int(input("Integer: "))
    num_list.append(num)

# if zero appears in list break while loop and print out average of those numbers excluding zero.

if 0 in num_list:
    average = sum(num_list)/(len(num_list)-1)
    print("The average of those numbers is {0:.2f}.".format(average))