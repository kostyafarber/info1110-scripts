num_string = [int(x) for x in list(input())]

nums = list(range(0,10))

for n in nums:
    if n in num_string:
       print(str(n) + ":", num_string.count(n))

    elif n not in num_string:
        print(str(n) + ": 0")

