N = int(input())
lst = [input() for _ in range(N)]

K = len(lst[0])
for k in range(1, K + 1):
    if N > 10 ** k:
        continue

    used = set()
    for n in range(N):
        tmp = lst[n][K - k:]

        if tmp in used:
            break

        used.add(tmp)
    else:
        print(k)
        break