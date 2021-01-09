import sys
import math

size = int(sys.argv[1])


def row_num(n, k):
    if k in (0, n):
        return 1
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


def pascal_rows(rows):
    result = []

    for n in range(size):
        rows = []
        for k in range(n+1):
            rows.append(str(row_num(n, k)))
        result.append(rows)
    return result


for i in pascal_rows(size):
    print(" ".join(i))
