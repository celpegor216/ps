N = int(input())
candidates = [[0] * 4 + [n + 1] for n in range(3)]

for _ in range(N):
    tmp = list(map(int, input().split()))

    for i in range(3):
        candidates[i][0] += tmp[i]
        candidates[i][tmp[i]] += 1

candidates.sort(key=lambda x: (-x[0], -x[3], -x[2], -x[1]))

def compare():
    if candidates[0][0] == candidates[1][0]:
        if candidates[0][3] == candidates[1][3]:
            if candidates[0][2] == candidates[1][2]:
                return 0, candidates[0][0]
    return candidates[0][-1], candidates[0][0]

print(*compare())