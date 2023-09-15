# 재귀인 건 알겠는데 어떻게 구현해야 할지 감이 하나도 안 온다
# 해답: https://ku-hug.tistory.com/149

N = int(input())
result = [[' '] * 2 * N for _ in range(N)]

def recursion(i, j, size):
    if size == 3:
        result[i][j] = '*'
        result[i + 1][j - 1] = result[i + 1][j + 1] = '*'
        for k in range(-2, 3):
            result[i + 2][j + k] = '*'
    
    else:
        newSize = size // 2
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)

recursion(0, N - 1, N)

for line in result:
    print(''.join(line))