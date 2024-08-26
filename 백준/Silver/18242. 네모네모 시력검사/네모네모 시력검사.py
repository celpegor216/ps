N, M = map(int, input().split())
lst = [input() for _ in range(N)]

def find():
    for i in range(N):
        for j in range(M):
            if lst[i][j] == '#':
                return (i, j)


# 정사각형의 왼쪽 위 좌표
# 위 > 아래 / 왼쪽 > 오른쪽 순서로 탐색하기 때문에 가장 먼저 발견한 #의 위치를 저장하면 됨
left_up = find()
up_cnt = left_cnt = 0

# 위쪽 선 길이
for i in range(left_up[1], M):
    if lst[left_up[0]][i] == '#':
        up_cnt += 1

# 왼쪽 선 길이
for i in range(left_up[0], N):
    if lst[i][left_up[1]] == '#':
        left_cnt += 1

# 둘이 다르면 둘 중에 하나 부족한 게 정답
if up_cnt != left_cnt:
    if up_cnt < left_cnt:
        print('UP')
    else:
        print('LEFT')
# 둘이 같으면 오른쪽 선 중간이랑 아래쪽 선 중간 중 비어있는 것 찾아서 정답 반환
else:
    down_middle = lst[left_up[0] + left_cnt - 1][left_up[1] + up_cnt // 2]
    right_middle = lst[left_up[0] + up_cnt // 2][left_up[1] + up_cnt - 1]

    if down_middle == '.':
        print('DOWN')
    else:
        print('RIGHT')