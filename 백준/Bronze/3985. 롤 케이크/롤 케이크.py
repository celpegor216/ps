L = int(input())
N = int(input())

used = [0] * (L + 1)

max_dream = 0
max_dream_idx = 0
max_real = 0
max_real_idx = 0

for n in range(N):
    p, k = map(int, input().split())

    if k - p > max_dream:
        max_dream = k - p
        max_dream_idx = n + 1

    cnt = 0
    for i in range(p, k + 1):
        if not used[i]:
            used[i] = n + 1
            cnt += 1

    if cnt > max_real:
        max_real = cnt
        max_real_idx = n + 1

print(max_dream_idx)
print(max_real_idx)