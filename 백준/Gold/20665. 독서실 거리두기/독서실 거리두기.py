# 반례를 못 찾겠음
# 해답: https://u.acmicpc.net/aa3f41ca-1736-4f6a-9a41-8bae6ecf081d/2020_shake!_solution.pdf

N, T, P = map(int, input().split())
lst = []

for _ in range(T):
    s, e = input().split()
    s = int(s[:2]) * 60 + int(s[2:])
    e = int(e[:2]) * 60 + int(e[2:])
    lst.append((s, e))

lst.sort()

seats = [0] * N
result = 0
for i in range(9 * 60, 21 * 60):
    # 퇴실
    for n in range(N):
        if seats[n] == i:
            seats[n] = 0
    
    # 입실
    for t in range(T):
        if lst[t][0] == i and lst[t][0] != lst[t][1]:
            maxv = -1
            seat = -1

            for n in range(N):
                if not seats[n]:
                    v = 1
                    while n - v >= 0 or n + v < N:
                        if (n - v >= 0 and seats[n - v]) or (n + v < N and seats[n + v]):
                            v -= 1
                            break
                        v += 1
                    if v > maxv:
                        maxv = v
                        seat = n
            
            seats[seat] = lst[t][1]
    
    # 선호하는 자리 비어있는지 확인
    if not seats[P - 1]:
        result += 1

print(result)