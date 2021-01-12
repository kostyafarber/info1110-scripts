n = int(input("Starting Number: "))

num_list = [n]

for i in num_list:
    if 1 in num_list:
        print("".join(str(num_list).strip("[]")))
    elif i % 2 == 0:
        num_list.append(int(i / 2))
    else:
        num_list.append(int(i * 3 + 1))

# Very useful function .strip to take the brackets out of a list if you want for printing.
