N = 8
lst = []
for n in range(N):
    score = int(input())
    lst.append((score, n))

lst.sort(reverse=True)
total = 0
result = []

for score, idx in lst[:5]:
    total += score
    result.append(idx + 1)

print(total)
print(*sorted(result))