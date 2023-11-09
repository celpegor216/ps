# 예전에 이렇게 풀었던 것 같은데 시간 초과 발생
# dp는 맞을텐데 여기서 시간을 어떻게 더 줄일 수 있지?

# 힌트: 이분 탐색
# 아니 정렬이 안 되어 있는데 이걸 어떻게 이분 탐색으로 풀 수 있지??

# 해답: https://my-coding-notes.tistory.com/121
# 솔직히 납득되지 않음

N = int(input())
lst = list(map(int, input().split()))

result = [0]

for i in range(N):
    if lst[i] > result[-1]:
        result.append(lst[i])
    else:
        start, end = 0, len(result) - 1
        idx = end

        while start <= end:
            middle = (start + end) // 2

            if result[middle] >= lst[i]:
                idx = middle
                end = middle - 1
            else:
                start = middle + 1

        result[idx] = lst[i]

print(len(result) - 1)