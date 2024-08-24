S = input()

N = 26
bucket = [0] * N

for s in S:
    bucket[ord(s) - ord('a')] += 1

print(*bucket)