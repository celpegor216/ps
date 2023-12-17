# 해답: https://velog.io/@7h13200/Python%EB%B0%B1%EC%A4%80-2015%EB%B2%88-%EC%88%98%EB%93%A4%EC%9D%98-%ED%95%A94

N, K = map(int, input().split())
lst = list(map(int, input().split()))

dic = dict()
dic[0] = 1

total = 0
result = 0

for item in lst:
    total += item

    if dic.get(total - K):
        result += dic[total - K]
    
    dic[total] = dic.get(total, 0) + 1

print(result)