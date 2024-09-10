N = int(input())
used = dict()

result = 0
for n in range(N):
    idx, state = map(int, input().split())

    if (state == 0 and not used.get(idx)) or (state == 1 and used.get(idx)):
        result += 1

    if state == 0 and used.get(idx):
        used.pop(idx)
    elif state == 1:
        used[idx] = 1

result += len(used)

print(result)