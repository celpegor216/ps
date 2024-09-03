N = int(input())

for n in range(N):
    lst = list(map(int, input().split()))
    for i in range(10):
        if lst[i] != i % 5 + 1:
            break
    else:
        print(n + 1)