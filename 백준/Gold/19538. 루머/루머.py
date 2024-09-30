import sys
input = sys.stdin.readline

N = int(input())
lst = [[]]
for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp.pop()
    lst.append(tmp)

M = int(input())
q = list(map(int, input().split()))

# 내 주변 사람들 중 몇 명이 루머를 믿는가?
neighbors = [0] * (N + 1)

# 내가 믿는가?
used = [-1] * (N + 1)
for now in q:
    used[now] = 0

time = 0
while q:
    time += 1

    nq = []

    for now in q:
        for nxt in lst[now]:
            if used[nxt] != -1:
                continue

            neighbors[nxt] += 1
            if neighbors[nxt] >= len(lst[nxt]) / 2:
                used[nxt] = time
                nq.append(nxt)

    q = nq

print(*used[1:])