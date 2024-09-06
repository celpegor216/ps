lst = [0] + list(map(int, input().split()))
rotates = [
    # 가로 1줄 회전
    [13, 14, 5, 6, 17, 18, 21, 22],
    # 가로 2줄 회전
    [15, 16, 7, 8, 19, 20, 23, 24],
    # 세로 1줄 회전
    [1, 3, 5, 7, 9, 11, 22, 24],
    # 세로 2줄 회전
    [2, 4, 6, 8, 10, 12, 21, 23],
    # 위 가로 1줄 회전
    [3, 4, 17, 19, 10, 9, 16, 14],
    # 위 가로 2줄 회전
    [1, 2, 18, 20, 12, 11, 15, 13],
]
MAX = 24

def check():
    for rotate in rotates:
        left_rotate = rotate[2:] + rotate[:2]
        right_rotate = rotate[-2:] + rotate[:-2]

        for r in (left_rotate, right_rotate):
            # 두 칸 밀기
            original = [lst[i] for i in rotate]

            for i in range(6):
                lst[rotate[i]] = lst[r[i]]
            lst[rotate[-2]] = original[0]
            lst[rotate[-1]] = original[1]

            # 확인
            flag = 0
            for i in range(1, MAX + 1, 4):
                for j in range(1, 4):
                    if lst[i] != lst[i + j]:
                        flag = 1
                        break
                if flag:
                    break

            if not flag:
                return 1

            # 원복
            for i in range(8):
                lst[rotate[i]] = original[i]

    return 0

print(check())