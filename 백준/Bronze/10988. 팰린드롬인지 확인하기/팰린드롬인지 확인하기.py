S = input()

while S:
    if S[0] == S[-1]:
        S = S[1:-1]
    else:
        break

print(0 if S else 1)