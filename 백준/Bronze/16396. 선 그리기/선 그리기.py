# 선의 개수 N의 최댓값 10 ** 4
# 좌표의 범위 1 ~ 10 ** 4
# 만약 시작값이 1, 끝값이 10 ** 4인 선이 10 ** 4개 들어올 경우,
# used 배열을 사용해서 특정 좌표의 방문 여부를 하나씩 변경해준다면
# 10 ** 4 * 10 ** 4, 즉 10 ** 8이 되므로 시간초과가 될 가능성이 있음
# 따라서, 모든 선분을 시작값에 따라 정렬한 다음
# 조금이라도 겹치는 부분이 있다면 선분을 연장하는 방식으로 진행하는 것이 좋음

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()    # 시작값이 작은 순서로 정렬

result = 0
start = end = 0    # 지금까지 이어지고 있는 선분들의 시작값, 끝값

for s, e in lst:
    # 지금까지 이어지고 있는 선분들과 겹치는 부분이 없다면
    # 지금까지의 선분 값을 정답에 더하고 새로운 선분을 시작함
    if end < s:
        result += end - start
        start = s
        end = e
    # 겹치는 부분이 있다면 선분을 연장시킴
    # 이때, 시작값이 작은 순서로 정렬했으므로 시작값은 연장될 일이 없음
    else:
        end = max(end, e)

# 잊어버리기 쉬운 부분, lst 탐색이 끝났을 때에도 지금까지 선분 값을 정답에 더해야 함
result += end - start

print(result)