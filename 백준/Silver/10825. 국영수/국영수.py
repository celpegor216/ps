import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    name, *scores = input().split()
    scores = list(map(int, scores))
    lst.append((*scores, name))

lst.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for line in lst:
    print(line[-1])