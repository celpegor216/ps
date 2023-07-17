N = int(input())
questions = [input().split() for _ in range(N)]

result = 0
used = [0] * 10

def dfs(level, path):
    global result

    if level == 3:
        flag = 0

        for q in questions:
            strike = 0
            ball = 0

            for i in range(3):
                if path[i] == q[0][i]:
                    strike += 1
                elif path[i] in q[0]:
                    ball += 1
            
            if strike != int(q[1]) or ball != int(q[2]):
                flag = 1
                break
        
        if not flag:
            result += 1

        return
    
    for i in range(1, 10):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, path + str(i))
            used[i] = 0

dfs(0, '')

print(result)