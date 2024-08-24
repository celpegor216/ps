M = 26

A = input()
B = input()

bucket_A = [0] * M
bucket_B = [0] * M

for a in A:
    bucket_A[ord(a) - ord('a')] += 1

for b in B:
    bucket_B[ord(b) - ord('a')] += 1

result = 0
for m in range(M):
    result += abs(bucket_A[m] - bucket_B[m])

print(result)