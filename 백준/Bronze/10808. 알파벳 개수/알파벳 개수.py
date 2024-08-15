S = input()

bucket = [0] * 26

for s in S:
    bucket[ord(s) - ord('a')] += 1

print(*bucket)