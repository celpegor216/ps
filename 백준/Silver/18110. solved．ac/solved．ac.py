N = int(input())

def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    return int(num)

if not N:
    print(0)
else:
    lst = sorted([int(input()) for _ in range(N)])

    out = round(N * 0.15)

    if out > 0:
        print(round(sum(lst[out:-out]) / (N - out * 2)))
    else:
        print(round(sum(lst) / N))