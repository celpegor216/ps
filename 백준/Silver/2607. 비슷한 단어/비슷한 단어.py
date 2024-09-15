N = int(input())
M = 26

standard = input()
length_standard = len(standard)
bucket_standard = [0] * M
for s in standard:
    bucket_standard[ord(s) - ord('A')] += 1

result = 0
for _ in range(N - 1):
    S = input()

    if abs(len(S) - length_standard) > 1:
        continue

    bucket_S = [0] * M
    for s in S:
        bucket_S[ord(s) - ord('A')] += 1
    
    what_standard_has = []
    what_S_has = []

    for m in range(M):
        diff = abs(bucket_standard[m] - bucket_S[m])
        if bucket_standard[m] > bucket_S[m]:
            what_standard_has += [m] * diff
        elif bucket_standard[m] < bucket_S[m]:
            what_S_has += [m] * diff
    
    if len(what_standard_has) > 1 or len(what_S_has) > 1:
        continue

    result += 1

print(result)