# 최장 증가 부분 수열
# 구현 방법을 모르겠음,,, dp처럼 푸는 건가?
# 최장 증가 부분 수열 해설: https://kimmessi.tistory.com/191

N = int(input())
lst = list(map(int, input().split()))

temp = [lst[0]]
dp = [1] * N

for i in range(N):
    if temp[-1] < lst[i]:
        temp.append(lst[i])
        dp[i] = len(temp)
    else:
        start, end = 0, len(temp)
        t = 0

        while start <= end:
            middle = (start + end) // 2
            
            if temp[middle] == lst[i]:
                t = middle
                break
            elif temp[middle] > lst[i]:
                t = middle
                end = middle - 1
            else:
                start = middle + 1
        
        temp[t] = lst[i]
        dp[i] = t + 1

print(max(dp))