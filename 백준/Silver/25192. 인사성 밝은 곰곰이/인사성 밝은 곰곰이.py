N = int(input())

used = set()
result = 0
for _ in range(N):
    S = input()

    if S == 'ENTER':
        used = set()
    else:
        if S not in used:
            result += 1
            used.add(S)

print(result)