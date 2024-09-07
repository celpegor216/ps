import sys
input = sys.stdin.readline

T = int(input())
left = right = 0
result = 0

for i in range(T):
    l, r = map(int, input().split())

    if l != 0 and left == l:
        result += 1
    if r != 0 and right == r:
        result += 1
    if l == r != 0:
        result += 1
    
    left = l
    right = r

print(result)