N = int(input())
lst = [input() for _ in range(N)]
K = int(input())

if K == 2:
    lst = [line[::-1] for line in lst]
elif K == 3:
    lst = [lst[n] for n in range(N - 1, -1, -1)]

for line in lst:
    print(line)