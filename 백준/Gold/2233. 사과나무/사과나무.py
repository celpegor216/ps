# 13%에서 계속 틀리는데 반례를 못 찾겠음
# 해답: https://peisea0830.tistory.com/110

N = int(input())
path = input()
X, Y = list(map(int, input().split()))

stack = []
nodes = [0] * (2 * N)

num = 0

parents = [[] for _ in range(N)]
height = [0] * N

for i in range(2 * N):
    if path[i] == '0':
        if stack:
            height[num] = height[stack[-1]] + 1
        stack.append(num)
        nodes[i] = num
        num += 1
    else:
        now = stack.pop()
        nodes[i] = now
        if stack:
            parents[now].append(stack[-1])

# 썩은 사과들이 방문하는 횟수를 저장
cnt = [0] * N

X, Y = nodes[X - 1], nodes[Y - 1]

def dfs(a):
    cnt[a] += 1
    for next in parents[a]:
        dfs(next)

dfs(X)
dfs(Y)

result = [(cnt[i], height[i], i) for i in range(N)]
result.sort(key=lambda x: (-x[0], -x[1]))

for i in range(2 * N):
    if nodes[i] == result[0][2]:
        print(i + 1, end = ' ')