N = 10
M = 20
result = [['.'] * M for _ in range(N)]

Q = int(input())
for _ in range(Q):
    tmp = input()
    i = ord(tmp[0]) - ord('A')
    j = int(tmp[1:]) - 1
    result[i][j] = 'o'

for line in result:
    print(''.join(line))