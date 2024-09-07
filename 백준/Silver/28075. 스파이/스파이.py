# N = int(input()) - 1
# print(chr(ord('A') + N % 12) + str(N % 10))


N, M = map(int, input().split())
# i 임무를 j 장소에서
lst = [list(map(int, input().split())) for _ in range(2)]

result = 0
def dfs(level, nowj, total):
    global result

    if level == N:
        if total >= M:
            result += 1
        return
    
    # 전날에 임무를 수행한 곳과 같은 장소를 선택하면
    # 그 날은 원래의 절반에 해당하는 진척도만 얻을 수 있다.
    # 이때, 장소가 같다면 임무가 달라도 얻는 진척도는 원래의 절반이 됨
    # 모든 진척도는 0이상 10 이하의 짝수
    for i in range(2):
        for j in range(3):
            if nowj == j:
                dfs(level + 1, j, total + lst[i][j] // 2)
            else:
                dfs(level + 1, j, total + lst[i][j])

dfs(0, -1, 0)
print(result)