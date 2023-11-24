# 해답: https://velog.io/@chocochip/2023-KAKAO-BLIND-RECRUITMENT-%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-%EB%AA%85%EB%A0%B9%EC%96%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%EB%B0%8F-%ED%92%80%EC%9D%B4

import sys
sys.setrecursionlimit(100000000)

answer = 'z'

def dfs(n, m, x, y, r, c, k, path, cnt):
    global answer
    
    if k < cnt + abs(r - x) + abs(c - y):
        return
    
    if cnt == k and x == r and y == c:
        answer = path
        return
    
    for dx, dy, p in ((1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')):
        nx, ny = x + dx, y + dy
        if 1 <= nx <= n and 1 <= ny <= m and path < answer:
            dfs(n, m, nx, ny, r, c, k, path + p, cnt + 1)
    

def solution(n, m, x, y, r, c, k):
    global answer
    
    diff = abs(r - x) + abs(c - y)
    
    if diff <= k and not (k - diff) % 2:
        dfs(n, m, x, y, r, c, k, '', 0)
    else:
        answer = 'impossible'
    
    return answer