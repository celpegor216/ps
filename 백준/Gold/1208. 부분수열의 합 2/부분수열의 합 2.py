# 이분 탐색 같은데 풀이를 모르겠음
# 해답: https://thought-process-ing.tistory.com/m/293

N, S = map(int, input().split())
lst = list(map(int, input().split()))

middle = N // 2

left = dict()
right = dict()

def backtracking(tmp, total, idx, dic):
    global left, right

    if dic:
        left[total] = left.get(total, 0) + 1
    else:
        right[total] = right.get(total, 0) + 1
    
    for i in range(idx, len(tmp)):
        backtracking(tmp, total + tmp[i], i + 1, dic)

backtracking(lst[:middle], 0, 0, 1)
backtracking(lst[middle:], 0, 0, 0)

result = 0

for key in left.keys():
    if (S - key) in right.keys():
        result += left[key] * right[S - key]

if S == 0:
    result -= 1

print(result)