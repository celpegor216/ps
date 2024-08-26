N = int(input())
M = 10    # 소의 번호 최댓값

# last_position[i]: i번째 소가 가장 마지막으로 길의 어느쪽에서 관찰되었는지 저장
# 소의 번호가 1 ~ 10까지이므로 M + 1
# 초기에는 어느 위치에 있는지 모르기 때문에 -1
last_position = [-1] * (M + 1)

result = 0
for _ in range(N):
    i, j = map(int, input().split())

    # i번 소가 처음으로 관찰된 경우
    if last_position[i] == -1:
        last_position[i] = j
    # i번 소가 이미 관찰된 적이 있으면서 지금과 다른 위치에 있는 경우, 이동한 것
    elif last_position[i] != j:
        last_position[i] = j
        result += 1

print(result)