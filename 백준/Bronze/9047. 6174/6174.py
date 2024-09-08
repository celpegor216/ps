T = int(input())

used = dict()
used['6174'] = 0

for _ in range(T):
    S = input()

    stack = [S]

    while 1:
        now = stack[-1]
        
        if used.get(now, -1) == -1:
            tmp = ''.join(sorted(str(now)))
            tmp = str(int(tmp[::-1]) - int(tmp))
            tmp = '0' * (4 - len(tmp)) + tmp
            stack.append(tmp)
        else:
            length = len(stack)
            for i in range(length - 1):
                used[stack[i]] = used[now] + length - i - 1
            break
    
    print(used[S])