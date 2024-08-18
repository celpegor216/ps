# 반례 참고


N = int(input())
lst = sorted(map(int, input().split()))

result = 0

for n in range(N):               # 찾으려는 값
    for left in range(N - 1):    # 왼쪽 값
        if left == n:
            continue

        start = left + 1         # 오른쪽 값의 시작 인덱스
        end = N - 1              # 오른쪽 값의 끝 인덱스
        flag = 0

        while start <= end:
            middle = (start + end) // 2

            if lst[left] + lst[middle] < lst[n]:
                start = middle + 1
            elif lst[left] + lst[middle] > lst[n]:
                end = middle - 1
            elif lst[left] + lst[middle] == lst[n]:
                flag = 1
                break
        
        if flag:
            if middle == n:
                if (middle - 1 > left and lst[middle - 1] == lst[middle]) or (middle + 1 < N and lst[middle + 1] == lst[middle]):
                    result += 1
                    break
            else:
                result += 1
                break

print(result)