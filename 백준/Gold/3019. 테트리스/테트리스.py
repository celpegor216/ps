# 블록과 블록 또는 블록과 바닥 사이에 채워져있지 않은 칸이 생기면 안 된다
# 블록을 놓는 서로 다른 방법의 수를 구하는 프로그램

# 도착할 바닥의 앞에서 뒤를 뺀 값
blocks = [
    [[0, 0, 0]],    # + C
    [[0]],
    [[0, -1], [1]],
    [[1, 0], [-1]],
    [[0, 0], [-1], [1, -1], [1]],
    [[0, 0], [0], [-1, 0], [2]],
    [[0, 0], [-2], [0, 1], [0]]
]

C, P = map(int, input().split())
lst = list(map(int, input().split()))

P -= 1
result = 0 if P else C

for shape in blocks[P]:
    length = len(shape)
    for i in range(C - length):
        flag = 0
        for j in range(length):
            if lst[i + j] - lst[i + j + 1] != shape[j]:
                flag = 1
                break
        if not flag:
            result += 1

print(result)