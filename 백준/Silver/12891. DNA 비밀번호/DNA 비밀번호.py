N, P = map(int, input().split())
S = input()
cnt = list(map(int, input().split()))    # A C G T

dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

bucket = [0] * 4

for p in range(P):
    if S[p] in dic:
        bucket[dic[S[p]]] += 1

result = 0
for n in range(P, N + 1):
    flag = 0

    for i in range(4):
        if bucket[i] < cnt[i]:
            flag = 1
            break

    if not flag:
        result += 1

    if n == N:
        break

    if S[n - P] in dic:
        bucket[dic[S[n - P]]] -= 1
    if S[n] in dic:
        bucket[dic[S[n]]] += 1

print(result)