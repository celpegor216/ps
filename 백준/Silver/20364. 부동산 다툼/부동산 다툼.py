import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

used = dict()

for _ in range(Q):
    num = int(input())
    flag = 0
    tmp = num

    while tmp > 0:
        if used.get(tmp):
            flag = tmp
        tmp //= 2
    
    if not flag:
        used[num] = 1
    
    print(flag)