# union-find 사용
# group: 각 정점이 속한 그룹의 리더 번호, 처음에는 모두 개별 그룹에 속해있음
# find(a): 입력받은 정점 a의 그룹 리더를 찾는 함수
#          자신이 리더가 아니라면 다른 사람이 리더
#          -> 다른 사람도 리더인지 확인하기 위해 find(group[a])로 재귀 수행
#          이후 그 값을 자신의 리더 번호로 변경해서 다음에 리더를 찾을 때의 시간을 단축시킴
# union(a, b): 입력받은 정점 a와 b의 그룹 리더를 찾음
#              서로 다른 리더를 가지고 있다면, 값이 더 큰 리더가 작은 리더의 밑으로 들어감
#              서로 같은 리더를 가지고 있다면, 이미 연결되어 있으므로 사이클이 완성됨

N, M = map(int, input().split())
group = [n for n in range(N)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        if group_a < group_b:
            group[group_b] = group_a
        else:
            group[group_a] = group_b
        return 0
    return 1

result = 0
for m in range(1, M + 1):
    a, b = map(int, input().split())

    if union(a, b) and not result:    # 처음으로 사이클이 완성된 자리를 찾아야 하므로 result == 0 일때에만 갱신
        result = m

print(result)