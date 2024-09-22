import sys
input = sys.stdin.readline

N, M = map(int, input().split())

group_size = int(N ** 0.5)
last_group_size = N % group_size
if last_group_size == 0:
    last_group_size = group_size
group_cnt = N // group_size
if N % group_size:
    group_cnt += 1

rabbits = [0] * N
groups = [0] * group_cnt

for _ in range(M):
    cnt, start = map(int, input().split())
    start -= 1
    result = 0

    # 시작점이 해당 그룹의 첫 번째가 아니라면 그 그룹부터 채우기
    fill_first_group = start % group_size
 
    if fill_first_group:
        fill_first_group = group_size - fill_first_group

        for i in range(fill_first_group):
            rabbits[start] += 1
            result += rabbits[start]
            cnt -= 1
            start += 1

            if not cnt:
                break
    
    # 채울 수 있는 그룹 채우기
    group_idx = start // group_size
    while cnt >= group_size:
        groups[group_idx] += 1
        result += groups[group_idx]
        cnt -= group_size
        group_idx += 1
        start += group_size

    # 마지막도 그룹으로 채울 수 있는지 확인
    if start + 1 + group_size >= N and cnt == last_group_size:
        groups[-1] += 1
        result += groups[-1]
    else:
        for i in range(cnt):
            rabbits[start] += 1
            result += rabbits[start]
            start += 1
    
    print(result)
