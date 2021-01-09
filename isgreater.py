import sys

num_list = sys.argv[1::]

if int(num_list[0]) > int(num_list[1]):
    print("Is {0} > {1}? true".format(num_list[0],num_list[1]))

else:
    print("Is {0} > {1}? false".format(num_list[0],num_list[1]))