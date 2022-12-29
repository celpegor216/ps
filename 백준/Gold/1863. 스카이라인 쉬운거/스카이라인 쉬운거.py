# 힌트: 스택 사용
# 해답: https://sinawi.tistory.com/473?category=649580

import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

result = 0
stack = [0]

for i in range(n):
    if lst[i][1] > stack[-1]:
        result += 1
        stack.append(lst[i][1])
    else:
        while lst[i][1] < stack[-1]:
            stack.pop()
            
        if lst[i][1] > stack[-1]:
            result += 1
            stack.append(lst[i][1])

print(result)