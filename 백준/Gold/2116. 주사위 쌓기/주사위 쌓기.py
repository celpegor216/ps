# 아래에 있는 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 한다
# 4개의 옆면 중에서 어느 한 면의 숫자의 합이 최대가 되도록 주사위를 쌓고자 한다
# 주사위를 위 아래를 고정한 채 옆으로 90도, 180도, 또는 270도 돌릴 수 있다

# a-f b-d c-e 짝
# 1번이 무엇을 윗면과 아랫면으로 두는지에 따라서 전체 결과가 정해짐

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
pairs = [5, 3, 4, 1, 2, 0]

result = 0
for i in range(6):         # 1번이 아랫면으로 둘 것
    total = 0              # 각 주사위에서 윗면과 아랫면을 제외한 최댓값들의 합
    bottom = lst[0][i]        # 아랫면 값
    top = lst[0][pairs[i]]    # 윗면 값(다음 아랫면 값)

    for n in range(N):
        total += max([x for x in range(1, 7) if x != top and x != bottom])

        if n == N - 1:
            break

        bottom_idx = lst[n + 1].index(top)
        bottom = lst[n + 1][bottom_idx]
        top = lst[n + 1][pairs[bottom_idx]]

    result = max(result, total)

print(result)