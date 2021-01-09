nums = input("Enter some numbers: ").split(",")

n = 1

if len(nums) > 1:
    nums = [int(x) for x in nums]
    for i in nums:
        n *= i
    print("The product is: " + str(n))
else:
    print("You did not enter any numbers!")









