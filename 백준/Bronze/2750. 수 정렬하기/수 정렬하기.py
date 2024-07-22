N = int(input())
lst = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for item in lst:
    print(item)