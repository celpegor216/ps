# 해답: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10986-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%82%98%EB%A8%B8%EC%A7%80-%ED%95%A9-%EA%B3%A8%EB%93%9C-3-%EB%88%84%EC%A0%81%ED%95%A9

N, M = map(int, input().split())
lst = list(map(int, input().split()))

left = [0] * M
total = 0

for n in range(N):
    total = (total + lst[n]) % M
    left[total] += 1

result = left[0]

for m in range(M):
    result += left[m] * (left[m] - 1) // 2

print(result)