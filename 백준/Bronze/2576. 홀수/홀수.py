N = 7
lst = [int(input()) for _ in range(N)]

odds = [item for item in lst if item % 2]
if not odds:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))