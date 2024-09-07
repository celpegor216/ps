T = int(input())

for _ in range(T):
    N = int(input())
    lst = sorted(map(int, input().split()))
    print((lst[-1] - lst[0]) * 2)