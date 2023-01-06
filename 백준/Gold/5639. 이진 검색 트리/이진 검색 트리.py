# 재귀 에러 문제 해결: https://omjinlts.github.io/algorithm/5639/

import sys
sys.setrecursionlimit(10 ** 5)

tree = []

while 1:
    try:
        a = int(input())
        tree.append(a)
    except:
        break

N = len(tree)

def pre_to_post(start, end):
    
    if start == end:
        print(tree[start])
        return
    
    root = tree[start]
    
    start += 1
    middle = -1
    
    for i in range(start, end + 1):
        if tree[i] > root:
            middle = i
            break
    
    # 왼쪽 혹은 오른쪽 자식만 있는 경우
    if middle == -1 or middle == start:
        pre_to_post(start, end)        
    # 둘 다 있는 경우
    else:
        # 왼쪽 자식이 하나인 경우
        if middle == start + 1:
            print(tree[start])
        else:
            pre_to_post(start, middle - 1)
        
        # 오른쪽 자식이 하나인 경우
        if middle == end:
            print(tree[end])
        else:
            pre_to_post(middle, end)
        
    print(root)

pre_to_post(0, N - 1)