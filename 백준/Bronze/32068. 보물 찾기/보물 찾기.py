T = int(input())

for t in range(T):
    L, R, S = map(int, input().split())
    print(min((S - L) * 2 + 1, (R - S) * 2))