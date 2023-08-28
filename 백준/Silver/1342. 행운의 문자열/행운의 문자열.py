S = input()
N = len(S)

bucket = [0] * 26

for s in S:
    bucket[ord(s) - ord('a')] += 1

result = 0
def dfs(level, path):
    global result

    if level == N:
        flag = 0

        for n in range(N - 1):
            if path[n] == path[n + 1]:
                flag = 1
                break
        
        if not flag:
            result += 1
        return

    for i in range(26):
        if bucket[i]:
            bucket[i] -= 1
            dfs(level + 1, path + chr(ord('a') + i))
            bucket[i] += 1

dfs(0, '')

print(result)