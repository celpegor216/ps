N, A, D = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
now = A - D
for item in lst:
    if now + D == item:
        now = item
        result += 1

print(result)