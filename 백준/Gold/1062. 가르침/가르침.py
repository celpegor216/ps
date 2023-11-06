# 해답: https://oh2279.tistory.com/158

N, K = map(int, input().split())
fixed = set('antatica')
words = [set(input()[4:-4]) - fixed for _ in range(N)]

used = [0] * 26

for item in fixed:
    used[ord(item) - ord('a')] = 1

K -= len(fixed)

result = 0

def dfs(level, now):
    global result

    if level == K:
        total = 0

        for word in words:
            flag = 0

            for item in word:
                if used[ord(item) - ord('a')] == 0:
                    flag = 1
                    break
            
            if not flag:
                total += 1
        
        result = max(result, total)
        return
    
    for n in range(now + 1, 26):
        if not used[n]:
            used[n] = 1
            dfs(level + 1, n)
            used[n] = 0

if K == 26:
    print(N)
elif K >= 0:
    dfs(0, -1)

print(result)