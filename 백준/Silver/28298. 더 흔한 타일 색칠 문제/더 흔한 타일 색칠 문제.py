# 반례 참고


N, M, K = map(int, input().split())
lst = [input() for _ in range(N)]

pattern = [[[0] * 26 for _ in range(K)] for _ in range(K)]

for i in range(0, N, K):
    for j in range(0, M, K):
        for a in range(K):
            for b in range(K):
                char_idx = ord(lst[i + a][j + b]) - ord('A')
                pattern[a][b][char_idx] += 1

result = 0
result_pattern = [''] * K
for i in range(K):
    for j in range(K):
        maxv = max(pattern[i][j])
        char = chr(ord('A') + pattern[i][j].index(maxv))

        result += (N * M) // (K ** 2) - maxv
        result_pattern[i] += char

print(result)
for _ in range(N // K):
    for k in range(K):
        print(result_pattern[k] * (M // K))