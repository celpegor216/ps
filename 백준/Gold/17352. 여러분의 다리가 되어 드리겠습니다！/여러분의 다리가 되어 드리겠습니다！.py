# union find는 맞췄는데 메모리 초과
# 해답: https://computer-science-student.tistory.com/659

N = int(input())

group = [x for x in range(N + 1)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a < group_b:
        group[group_b] = group_a
    else:
        group[group_a] = group_b

for n in range(N - 2):
    a, b = map(int, input().split())

    union(a, b)

result = []

for n in range(1, N + 1):
    if n == group[n]:
        result.append(n)

print(*result)