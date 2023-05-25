N = int(input())
lst = sorted(map(int, input().split()))

if N % 2:
    print(lst[N // 2] ** 2)
else:
    print(lst[0] * lst[-1])