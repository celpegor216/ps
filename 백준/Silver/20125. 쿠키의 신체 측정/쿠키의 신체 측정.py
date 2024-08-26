# 허리는 심장의 바로 아래 쪽에 붙어있고 아래 쪽으로 뻗어 있다
# 왼쪽 다리는 허리의 왼쪽 아래에, 오른쪽 다리는 허리의 오른쪽 아래에 바로 붙어있고, 각 다리들은 전부 아래쪽으로 뻗어 있다
# 허리, 팔, 다리의 길이는 1 이상이며, 너비는 무조건 1

N = int(input())
lst = [input() for _ in range(N)]

found_head = 0    # 머리를 찾았는지 여부
heart = []    # 심장의 위치
result = [0] * 5    # 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리

for i in range(N):
    for j in range(N):
        if lst[i][j] == '_':
            continue

        # 머리는 심장 바로 윗 칸에 1칸 크기
        if not found_head:
            found_head = 1
            heart = [i + 1, j]
        else:
            if i == heart[0]:
                # 왼쪽 팔
                if j < heart[1]:
                    result[0] += 1
                # 오른쪽 팔
                if j > heart[1]:
                    result[1] += 1
            else:
                # 허리
                if j == heart[1]:
                    result[2] += 1
                # 왼쪽 다리
                elif j < heart[1]:
                    result[3] += 1
                # 오른쪽 다리
                else:
                    result[4] += 1

print(heart[0] + 1, heart[1] + 1)
print(*result)