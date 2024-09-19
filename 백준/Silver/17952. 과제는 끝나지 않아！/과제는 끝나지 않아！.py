import sys
input = sys.stdin.readline

N = int(input())

works = []
result = 0
for _ in range(N):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        works.append([cmd[1], cmd[2]])

    if works:
        works[-1][-1] -= 1
        if works[-1][-1] == 0:
            result += works.pop()[0]

print(result)