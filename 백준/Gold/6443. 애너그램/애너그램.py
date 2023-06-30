N = int(input())

def dfs(level, path, bucket):
    global length
    
    if level == length:
        print(path)
        return

    for i in range(26):
        if bucket[i]:
            bucket[i] -= 1
            dfs(level + 1, path + chr(i + ord('a')), bucket)
            bucket[i] += 1

for n in range(N):
    s = input()
    bucket = [0] * 26

    for i in s:
        bucket[ord(i) - ord('a')] += 1
    
    length = len(s)
    dfs(0, '', bucket)