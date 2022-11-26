N = int(input())    # 이동하려는 채널
M = int(input())    # 고장난 버튼 수
if M != 0:
    disable = list(map(int, input().split()))    # 고장난 버튼 배열
    able = [x for x in range(10) if x not in disable]  # 가능한 버튼 배열
else:
    able = [x for x in range(10)]

length = len(str(N))    # 이동하려는 채널의 글자 수
prox = 100

def dfs(level, num):
    global prox

    # 이동하려는 채널과 차이가 더 적은 수를 prox에 저장
    if abs(num - N) + level < abs(prox - N) + len(str(prox)):
        prox = num

    if level == length:
        return

    if not(level == 0 and num == 0):
        for n in able:
            dfs(level + 1, num * 10 + n)

# 숫자 버튼을 눌러서 숫자를 새로 만드는 경우
for item in able:
    dfs(0, item)

# +, -를 눌러서 이동만 하는 경우
move = abs(N - 100)

print(min(move, abs(prox - N) + len(str(prox))))