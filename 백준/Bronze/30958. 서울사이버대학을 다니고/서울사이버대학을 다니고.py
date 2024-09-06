N = int(input())
S = input()

bucket = [0] * 26
for s in S:
    if 'a' <= s <= 'z':
        bucket[ord(s) - ord('a')] += 1

print(max(bucket))