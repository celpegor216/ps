N = int(input())

used = set()

for _ in range(N):
    S = input()
    length = len(S)

    for start in range(length):
        if S[start:] + S[:start] in used:
            break
    else:
        used.add(S)

print(len(used))