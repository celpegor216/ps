N, M = map(int, input().split())
J = int(input())
now = 0
result = 0

for _ in range(J):
    idx = int(input()) - 1

    if now > idx:
        result += now - idx
        now = idx
    elif now + M <= idx:
        result += idx - (now + M - 1)
        now += idx - (now + M - 1)

print(result)