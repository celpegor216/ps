# 크기가 n * n
N, L = map(int, input().split())
M = N
lst = [list(map(int, input().split())) for _ in range(N)]

# 지나갈 수 있는 열과 행의 총 개수를 출력하는 프로그램
result = 0
def find():
    global result

    for i in range(N):
        stack = []
        for j in range(M):
            if not stack or stack[-1][0] != lst[i][j]:
                stack.append([lst[i][j], 1])
            else:
                stack[-1][1] += 1

        # 모든 높이가 똑같을 경우
        if len(stack) == 1:
            result += 1
        else:
            flag = 0
            for j in range(len(stack) - 1):
                # 경사로는 높이 차이가 1이 나는 보도블럭에 설치가능하며,
                # 낮은 칸에 설치됩니다.
                # 오른쪽이 1칸 더 높을 경우
                if stack[j][0] + 1 == stack[j + 1][0]:
                    # 경사로의 길이 L동안 바닥에 접촉해야하며,
                    # 경사로가 놓인 보도블럭의 높이는 모두 같아야 합니다.
                    if stack[j][1] < L:
                        flag = 1
                        break
                # 왼쪽이 1칸 더 높을 경우
                elif stack[j][0] == stack[j + 1][0] + 1:
                    if stack[j + 1][1] < L:
                        flag = 1
                        break
                    stack[j + 1][1] -= L
                # 높이 차이가 1칸 이상 나는 경우
                else:
                    flag = 1
                    break

            if not flag:
                result += 1


find()    # 행
lst = list(map(list, zip(*lst)))
find()    # 열

print(result)