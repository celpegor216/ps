a = input()
b = input()

bucket_a = [0] * 26
bucket_b = [0] * 26

for s in a:
    bucket_a[ord(s) - ord('a')] += 1
for s in b:
    bucket_b[ord(s) - ord('a')] += 1

result = 0
for i in range(26):
    result += abs(bucket_a[i] - bucket_b[i])

print(result)