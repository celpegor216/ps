N = int(input())
lst = list(map(int, input().split()))

bucket = dict()
for item in lst:
    if item == 0:
        continue
    bucket[item] = bucket.get(item, 0) + 1

result = 0
while bucket.keys():
    min_key = min(bucket.keys())
    nxt_key = min_key * 2

    if bucket.get(min_key) > 1:
        bucket[nxt_key] = bucket.get(nxt_key, 0) + bucket[min_key] // 2
    bucket.pop(min_key)

    result = min_key

print(result)