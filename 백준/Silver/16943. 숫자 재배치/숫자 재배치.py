A, B = input().split()
B = int(B)
A = list(map(int, A))
N = len(A)

result = -1
used = [0] * N
def dfs(level, path):
    global result

    if level == N:
        if path < B:
            result = max(result, path)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, path * 10 + A[i])
            used[i] = 0

for i in range(N):
    if not A[i]:
        continue
    
    used[i] = 1
    dfs(1, A[i])
    used[i] = 0

print(result)