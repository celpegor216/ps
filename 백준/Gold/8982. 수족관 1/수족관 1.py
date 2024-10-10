N = int(input())

# 선의 높이, 가로 시작, 가로 끝
lines = [(0, 0, 0)]
input()
for _ in range(N // 2 - 1):
    x1, y = map(int, input().split())
    x2, _ = map(int, input().split())
    lines.append((y, x1, x2))
input()
lines.append((0, 0, 0))

N = len(lines)
minus = [0] * N

K = int(input())
for _ in range(K):
    x1, y, x2, _ = map(int, input().split())

    idx = lines.index((y, x1, x2))
    minus[idx] = max(minus[idx], y)

    left = idx - 1
    now = y
    while left > 0:
        now = min(now, lines[left][0])
        if minus[left] >= now:
            break
        minus[left] = now
        left -= 1

    now = y
    right = idx + 1
    while right < N - 1:
        now = min(now, lines[right][0])
        if minus[right] >= now:
            break
        minus[right] = now
        right += 1

result = 0
for i in range(1, N - 1):
    result += (lines[i][0] - minus[i]) * (lines[i][2] - lines[i][1])

print(result)