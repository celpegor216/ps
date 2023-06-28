N, K = map(int, input().split())
lst = list(map(int, input().split()))
robots = []

cnt = 0

while lst.count(0) < K:
    cnt += 1

    lst = [lst[-1]] + lst[:-1]

    if robots:
        idx = 0
        while idx < len(robots):
            robots[idx] = (robots[idx] + 1) % (2 * N)
            if robots[idx] == N - 1:
                robots.pop(idx)
                idx -= 1
            idx += 1

        idx = 0
        while idx < len(robots):
            temp = (robots[idx] + 1) % (2 * N)
            if temp not in robots and lst[temp] > 0:
                robots[idx] = temp
                lst[temp] -= 1
                if robots[idx] == N - 1:
                    robots.pop(idx)
                    idx -= 1
            idx += 1
    
    if lst[0] > 0 and 0 not in robots:
        robots.append(0)
        lst[0] -= 1

print(cnt)