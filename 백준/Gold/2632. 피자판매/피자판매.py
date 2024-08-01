TARGET = int(input())
A, B = map(int, input().split())
lst_A = [int(input()) for _ in range(A)]
lst_B = [int(input()) for _ in range(B)]

bucket_A = [0] * (TARGET + 1)
bucket_B = [0] * (TARGET + 1)

for start in range(A):
    end = start
    total = lst_A[end]
    while total <= TARGET:
        bucket_A[total] += 1
        end = (end + 1) % A
        if end == (start - 1) % A:
            break
        total += lst_A[end]

for start in range(B):
    end = start
    total = lst_B[end]
    while total <= TARGET:
        bucket_B[total] += 1
        end = (end + 1) % B
        if end == (start - 1) % B:
            break
        total += lst_B[end]

if sum(lst_A) <= TARGET:
    bucket_A[sum(lst_A)] += 1
if sum(lst_B) <= TARGET:
    bucket_B[sum(lst_B)] += 1

result = bucket_A[-1] + bucket_B[-1]
for n in range(1, TARGET):
    result += bucket_A[n] * bucket_B[TARGET - n]

print(result)