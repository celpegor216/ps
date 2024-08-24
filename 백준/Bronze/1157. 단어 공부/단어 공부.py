S = input().upper()

N = 26
bucket = [0] * N

for s in S:
    bucket[ord(s) - ord('A')] += 1

max_cnt = 0
max_idx = []

for n in range(N):
    if bucket[n] > max_cnt:
        max_cnt = bucket[n]
        max_idx = [n]
    elif bucket[n] == max_cnt:
        max_idx.append(n)

print(chr(ord('A') + max_idx[0]) if len(max_idx) == 1 else '?')