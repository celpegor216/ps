N = int(input())
lst = [[0] * 3 for _ in range(N)]

for i in range(3):
    if i == 2:
        tmp = input().split()
    else:
        tmp = list(map(int, input().split()))
    for j in range(N):
        lst[j][i] = tmp[j]

def find():
    for i in range(N - 1):
        for j in range(i + 1, N):
            if abs(lst[i][0] - lst[j][0]) <= lst[i][1] + lst[j][1] and lst[i][2] != lst[j][2]:
                print('YES')
                print(i + 1, j + 1)
                return
    print('NO')

find()