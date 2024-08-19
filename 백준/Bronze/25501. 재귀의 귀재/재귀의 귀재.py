def recursion(l, r):
    global cnt

    cnt += 1

    if l >= r:
        return 1

    if S[l] != S[r]:
        return 0

    return recursion(l + 1, r - 1)

T = int(input())

for _ in range(T):
    S = input()

    cnt = 0
    result = recursion(0, len(S) - 1)

    print(result, cnt)