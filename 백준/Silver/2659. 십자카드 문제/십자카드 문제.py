N = 4
numbers = []
MAX = 10 ** 4

for i in range(1111, MAX):
    string = list(str(i))

    if '0' in string:
        continue

    minv = MAX
    for _ in range(N):
        minv = min(minv, int(''.join(string)))
        string.append(string.pop(0))
    
    if i != minv:
        continue

    numbers.append(i)

S = input().split()
minv = MAX
for _ in range(N):
    minv = min(minv, int(''.join(S)))
    S.append(S.pop(0))

print(numbers.index(minv) + 1)