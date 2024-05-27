# 누적합이 아니라 이분매칭
# 해답: https://dev-scratch.tistory.com/72

import sys
input = sys.stdin.readline

T = int(input())

def matching(m):
    for book in lst[m]:
        if used[book]:
            continue
        used[book] = 1
        if not books[book] or matching(books[book]):
            books[book] = m
            return 1
    return 0

for _ in range(T):
    N, M = map(int, input().strip().split())
    lst = [[]]
    
    for _ in range(M):
        a, b = list(map(int, input().strip().split()))
        lst.append([x for x in range(a, b + 1)])

    books = [0] * (N + 1)
    result = 0

    for m in range(1, M + 1):
        used = [0] * (N + 1)
        result += matching(m)
        
    print(result)