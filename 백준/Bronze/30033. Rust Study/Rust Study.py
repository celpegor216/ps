N = int(input())
plans = list(map(int, input().split()))
dids = list(map(int, input().split()))

result = 0
for n in range(N):
    if plans[n] <= dids[n]:
        result += 1

print(result)