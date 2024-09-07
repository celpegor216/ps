N = int(input())
lst = [input() for _ in range(N)]

for n in range(N - 1):
    if lst[n][::-1] in lst:
        print(len(lst[n]), lst[n][len(lst[n]) // 2])
        break