from math import ceil


T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    now = a / b
    result = 0

    while 1:
        result = ceil(b / a)
        a, b = a * result - b, b * result

        if a == 0:
            break

    print(result)