from collections import deque

# 하나라도 해당하지 않는 경우가 있으면 바로 종료시키기 위해 함수 사용
def check():
    # 3×3
    N = 3
    # 패턴의 길이는 3 이상이다.
    L = int(input())
    lst = list(map(lambda x: int(x) - 1, input().split()))

    # 패턴을 나타내는 수열에는 같은 점이 두번 이상 등장하지 않는다.
    used = [0] * 9
    for item in lst:
        if used[item]:
            return 'NO'
        
        used[item] += 1

    # 수열의 인접한 점을 연결해 만든 선분 위에는 아직 등장하지 않은 점이 있을 수 없다.
    lst = [(x // N, x % N) for x in lst]
    for l in range(L - 1):
        y_diff, x_diff = abs(lst[l][0] - lst[l + 1][0]), abs(lst[l][1] - lst[l + 1][1])
    
        if x_diff == 0 and y_diff == 2 and (1, lst[l][1]) not in lst[:l]:
            return 'NO'
            
        if x_diff == 2 and y_diff == 0 and (lst[l][0], 1) not in lst[:l]:
            return 'NO'
            
        if x_diff == 2 and y_diff == 2 and (1, 1) not in lst[:l]:
            return 'NO'

    return 'YES'

print(check())