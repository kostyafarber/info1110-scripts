import math
import sys

try:

    if len(sys.argv) < 2:
        print("Not enough arguments.")
        sys.exit()

    elif len(sys.argv) > 2:
        print("Too many arguments.")
        sys.exit()

    size = int(sys.argv[1])

    def row_num(n, k):
        if k in (0, n):
            return 1
        return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


    def pascal_rows(rows):
        result = []

        for n in range(size + 1):
            rows = []
            for k in range(n + 1):
                rows.append(str(row_num(n, k)))
            result.append(rows)
        return result


    for i in pascal_rows(size):
        print(" ".join(i))

except ValueError:
    print("Invalid argument.")
