while True:
    num = int(input("Integer: "))
    if num == 0:
        print("Bye")
        break
    if num % 2 == 0 and num in range(20,201) or num % 2 != 0 and num < 0:
        print(num, "passes the test!")
    else:
        print(num, "fails the test :(")

