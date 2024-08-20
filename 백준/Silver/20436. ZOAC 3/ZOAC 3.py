# 자음은 왼손으로만, 모음은 오른손으로만... 문제를 제대로 읽지 않았음


keyboards = [
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm'
]

# 키보드의 각 줄에서 모음이 시작되는 위치
limits = [5, 5, 4]

left_pos = dict()
right_pos = dict()

for i in range(3):
    for j in range(len(keyboards[i])):
        if j >= limits[i]:
            right_pos[keyboards[i][j]] = (i, j)
        else:
            left_pos[keyboards[i][j]] = (i, j)

left, right = input().split()
S = input()
N = len(S)

result = 0

for s in S:
    if left == s or right == s:
        continue

    if s in left_pos:
        result += abs(left_pos[left][0] - left_pos[s][0]) + abs(left_pos[left][1] - left_pos[s][1])
        left = s
    else:
        result += abs(right_pos[right][0] - right_pos[s][0]) + abs(right_pos[right][1] - right_pos[s][1])
        right = s

print(result + len(S))