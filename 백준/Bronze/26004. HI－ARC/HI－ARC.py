N = int(input())
S = input()

bucket = dict()
for s in S:
    bucket[s] = bucket.get(s, 0) + 1

result = N
for key in 'HIARC':
    result = min(result, bucket.get(key, 0))

print(result)