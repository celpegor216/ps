# 힌트: DFS
# 힌트: 0번 노드가 루트가 아닐 수 있음, 자식 노드보다 부모 노드가 더 클 수 있음
# 해답 참조

N = int(input())
lst = list(map(int, input().split()))
delete = int(input())

result = 0

def dfs_delete(parent):
    lst[parent] = -2

    for i in range(N):
        if lst[i] == parent:
            dfs_delete(i)

dfs_delete(delete)

for i in range(N):
    if lst[i] != -2 and i not in lst:
        result += 1

print(result)