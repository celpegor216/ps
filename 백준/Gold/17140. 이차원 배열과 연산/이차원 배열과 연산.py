ty, tx, tk = map(int, input().split())
ty -= 1
tx -= 1
MAX = 100    # 최대 크기는 100
N = M = 3    # 초기 크기는 3
lst = [list(map(int, input().split())) for _ in range(N)]

def row_calc():
    global N, M

    new_M = M
    for i in range(N):
        # 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
        # dic[i]: i가 등장한 횟수
        dic = dict()
        for j in range(M):
            # 수를 정렬할 때 0은 무시
            # [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.
            if not lst[i][j]:
                continue
            dic[lst[i][j]] = dic.get(lst[i][j], 0) + 1

        # 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저
        lst[i] = []
        tmp_M = 0
        for key, value in sorted(dic.items(), key=lambda x: (x[1], x[0])):
            lst[i].append(key)
            lst[i].append(value)

            tmp_M += 2
            new_M = max(new_M, tmp_M)

            # 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
            if tmp_M == 100:
                break

    # 행 또는 열의 크기가 커진 곳에는 0이 채워진다
    for n in range(N):
        lst[n] += [0] * (new_M - len(lst[n]))

    M = new_M


result = 0
while 1:
    # A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간
    if ty < N and tx < M and lst[ty][tx] == tk:
        print(result)
        break
    elif result > 100:
        print(-1)
        break

    result += 1

    # R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
    if N >= M:
        row_calc()
    # C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
    else:
        # 배열을 전치
        N, M = M, N
        lst = list(map(list, zip(*lst)))

        # 행 연산이랑 똑같이 한 다음
        row_calc()

        # 다시 전치
        N, M = M, N
        lst = list(map(list, zip(*lst)))