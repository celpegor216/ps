# 해답: https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4

N = int(input())
lst = list(map(int, input().split()))

increase = [1] * N
decrease = [1] * N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            increase[i] = max(increase[i], increase[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if lst[i] > lst[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

result = 0

for i in range(N):
    if increase[i] + decrease[i] - 1 > result:
        result = increase[i] + decrease[i] - 1

print(result)