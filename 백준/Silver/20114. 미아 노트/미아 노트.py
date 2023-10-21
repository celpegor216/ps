N, H, W = map(int, input().split())
lst = [input() for _ in range(H)]

result = ''

for n in range(N):
    tmp = '?'

    for h in range(H):
        if tmp == '?':
            for w in range(W):
                if lst[h][n * W + w] != '?':
                    tmp = lst[h][n * W + w]
                    break
        else:
            break
    
    result += tmp

print(result)