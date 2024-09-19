# 반례 참고


N = int(input())
lst = []
for _ in range(N):
    start, end = input().split()
    start = int(start[:2]) * 60 + int(start[2:])
    end = int(end[:2]) * 60 + int(end[2:])
    lst.append((start, end))
lst.sort()

result = 0
now = 10 * 60

for s, e in lst:
    result = max(result, s - 10 - now)
    now = max(now, e + 10)

last = 22 * 60
if now < last:
    result = max(result, last - now)

print(result)