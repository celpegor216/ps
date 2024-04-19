M, N = map(int, input().split())
spaces = [list(map(int, input().split())) for _ in range(M)]

def check(i1, j1, i2, j2):
    if (i1 > j1 and i2 <= j2) or (i1 == j1 and i2 != j2) or (i1 < j1 and i2 >= j2):
        return -1
    return 0

result = 0
for a in range(M):
    for b in range(a + 1, M):
        flag = 1

        for i in range(N):
            if not flag:
                break

            for j in range(i + 1, N):
                flag += check(spaces[a][i], spaces[a][j], spaces[b][i], spaces[b][j])

                if not flag:
                    break
        
        result += flag

print(result)