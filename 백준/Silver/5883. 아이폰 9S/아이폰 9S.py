N = int(input())
lst = [int(input()) for _ in range(N)]
# 중복 제거해서 원하는 용량의 종류를 계산
unique = set(lst)

result = 1

# 용량의 종류 중 하나씩 스킵해보면서 가장 긴 연속 구간의 길이를 구하기
for skip in unique:
    now = -1    # 현재 연속 구간의 길이를 구하고 있는 수
    cnt = 0    # 현재 연속 구간의 길이
    for n in range(N):
        if lst[n] == skip:
            continue

        if lst[n] != now:
            cnt = 1
            now = lst[n]
        else:
            cnt += 1
            result = max(result, cnt)

print(result)