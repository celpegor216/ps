# 시간 초과
# 이분 탐색을 사용해야 함,,,
# 해답: https://velog.io/@veonico/%EB%B0%B1%EC%A4%80-14003.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-5-python%ED%8C%8C%EC%9D%B4%EC%8D%AC

N = int(input())
lst = list(map(int, input().split()))

result_list = [lst[0]]
result_level = [1] * N    # num, idx

# result_list에서 num 보다 작은 값 중 최댓값의 idx + 1
def find_idx(num):
    start = 0
    end = len(result_list) - 1
    result = -1

    while start <= end:
        middle = (start + end) // 2

        if num > result_list[middle]:
            result = middle
            start = middle + 1
        else:
            end = middle - 1
    
    return result + 1

for n in range(1, N):
    if lst[n] > result_list[-1]:
        result_list.append(lst[n])
        result_level[n] = len(result_list)
    else:
        idx = find_idx(lst[n])
        result_list[idx] = lst[n]
        result_level[n] = idx + 1

maxv = len(result_list)
result = []

for n in range(N - 1, -1, -1):
    if result_level[n] == maxv:
        result.append(lst[n])
        maxv -= 1

print(len(result))
print(*result[::-1])