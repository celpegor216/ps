# 리스트를 거꾸로 순회
# 스택이 비어있지 않다면 현재 높이보다 높은 값이 나오기 전까지 계속 제거
# 이후에도 스택이 비어있지 않다면 현재 높이보다 높은 값이 있는 것이므로 그 곳에서 막힘
#   -> 볼 수 있는 최대 옥상의 수는 해당 위치 - 현재 위치 - 1
# 스택이 비어있다면 현재 높이가 가장 높으므로 막히는 곳이 없음
#   -> 볼 수 있는 최대 옥상의 수는 전체 빌딩 수 - 현재 위치 - 1

N = int(input())
lst = [int(input()) for _ in range(N)]
result = [0] * N

stack = []
for n in range(N - 1, -1, -1):
    while stack and lst[stack[-1]] < lst[n]:
        stack.pop()

    if stack:
        result[n] = stack[-1] - n - 1
    else:
        result[n] = N - n - 1

    stack.append(n)

print(sum(result))
