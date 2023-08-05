# 해답: https://rhdtka21.tistory.com/131

N = int(input())
lst = list(map(int, input().split()))

# 총합이 3의 배수인가?
if sum(lst) % 3:
    print('NO')

# 총합이 3의 배수라면, 1&2, 3의 조합으로 만들 수 있는가?
# -> 할당 가능한 2의 개수가 총합//3 이상이어야 함
else:
    cnt = 0
    for item in lst:
        cnt += item // 2
    
    if cnt >= sum(lst) // 3:
        print('YES')
    else:
        print('NO')