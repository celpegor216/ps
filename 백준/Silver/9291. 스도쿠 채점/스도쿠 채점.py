TC = int(input())
N = 9

def check():
    used_row = [[0] * N for _ in range(N)]
    used_col = [[0] * N for _ in range(N)]
    used_box = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            num = lst[i][j] - 1

            if used_row[i][num]:
                return 'INCORRECT'
            used_row[i][num] = 1

            if used_col[j][num]:
                return 'INCORRECT'
            used_col[j][num] = 1

            box_idx = (i // 3) * 3 + (j // 3)
            if used_box[box_idx][num]:
                return 'INCORRECT'
            used_box[box_idx][num] = 1

    return 'CORRECT'

for tc in range(1, TC + 1):
    lst = [list(map(int, input().split())) for _ in range(N)]
    print(f'Case {tc}: {check()}')

    if tc != TC:
        _ = input()
