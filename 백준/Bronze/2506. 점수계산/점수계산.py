N = int(input())
lst = list(map(int, input().split()))

result = 0
now = 0
for item in lst:
    if item == 1:
        now += 1
        result += now
    else:
        now = 0

print(result)