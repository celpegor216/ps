N = int(input())
lst = [[0] * 26 for _ in range(26)]

for n in range(N):
    a, b = input().split(' is ')

    a = ord(a) - ord('a')
    b = ord(b) - ord('a')

    lst[a][b] = 1

result = 'F'

used = [0] * 26
def dfs(now, end):
    global result

    if now == end:
        result = 'T'
        return
    
    for i in range(26):
        if lst[now][i] and not used[i]:
            used[i] = 1
            dfs(i, end)
            used[i] = 0

M = int(input())

for m in range(M):
    a, b = input().split(' is ')

    a = ord(a) - ord('a')
    b = ord(b) - ord('a')

    result = 'F'
    dfs(a, b)

    print(result)