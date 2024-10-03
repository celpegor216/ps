# 보드의 크기 N, 시작 시 가지는 돈 S, 시작점을 지나면 받게 되는 월급 W, 황금 열쇠 카드의 개수 G
N, S, W, G = map(int, input().split())
N -= 1
size = 4 * N

# 황금 열쇠 리스트
# 1, 2, 3, 4 순서대로 은행에서 돈 받기 / 은행에 돈 주기 / 사회복지기금에 기부 / 특정 칸만큼 이동
golden_keys = [list(map(int, input().split())) for _ in range(G)]

# 보드판 정보
# -1: 시작 칸
# -2: 무인도 칸
# -3: 사회복지기금 칸
# -4: 우주여행 칸
# 0: 황금 열쇠 칸
# P: 도시 칸 가격
board = [0] * size
cities = 0

# N의 배수는 특수칸
for n in range(size):
    if not n % N:
        board[n] = -(n // N + 1)
    else:
        tmp = input()
        if tmp[0] == 'L':
            board[n] = int(tmp[2:])
            cities += 1

D = int(input())
dices = [list(map(int, input().split())) for _ in range(D)]


# 현재 위치, 현재 가지고 있는 돈
now_idx, now_cash = 0, S
# 뽑을 황금 열쇠 번호
goldne_keys_idx = 0
# 무인도에서 얼마나 있어야 하나?
waiting = 0
# 사회복지기금에 모인 돈
fund = 0
# 지금까지 산 땅, sum이 cities와 같다면 모든 땅을 산 것
used = [0] * size


def check():
    global now_idx, now_cash, waiting, fund, goldne_keys_idx

    # 시작 칸(1번째 칸): 이 칸에 정확히 멈추거나 지나가게 되면, 월급을 받게 된다.
    if now_idx >= size:
        now_cash += W * (now_idx // size)
    
    now_idx %= size

    if board[now_idx] == -2:
        waiting = 3
    
    # 사회복지기금 칸(2n - 1번째 칸): 이 칸에 정확히 멈추게 되면, 지금까지 모인 사회복지기금을 받게 된다. 
    #   사회복지기금을 받고 나면, 기부금은 0원이 된다.
    elif board[now_idx] == -3:
        now_cash += fund
        fund = 0

    # 우주여행 칸(3n - 1번째 칸): 이 칸에 정확히 멈추게 되면, 다음 턴에 시작 칸으로 이동한 뒤 주사위를 굴린다.
    elif board[now_idx] == -4:
        now_cash += W
        now_idx = 0

    # 황금 열쇠 칸: 특정한 효과가 있는 카드가 발동되는 칸
    #   은행에서 돈 받기 / 은행에 돈 주기 / 사회복지기금에 돈 기부하기 / 특정 칸으로 이동
    #   은행에 돈 주기나 사회복지기금에 돈 기부하기의 경우, 돈이 부족하면 땅을 다 사도 패배
    #   특정 칸으로 이동하는 경우, 무조건 정방향(+)
    #   이동하는 동안 지나치는 칸에서는 아무 일도 일어나지 않음(시작 칸 제외)
    #   도착한 칸에서는 일어나야 할 일이 일어남(도착한 칸이 황금 열쇠 칸인 경우는 없음)
    #   황금 열쇠 리스트를 끝까지 다 뽑으면 다시 리스트의 처음으로 돌아감
    elif board[now_idx] == 0:
        t, x = golden_keys[goldne_keys_idx]
        goldne_keys_idx = (goldne_keys_idx + 1) % G

        if t == 1:
            now_cash += x
        
        elif t == 2:
            now_cash -= x
        
        elif t == 3:
            now_cash -= x
            fund += x
        
        elif t == 4:
            now_idx += x
            check()

    # 도시 칸: 돈을 내고 땅을 사야 하는 칸
    #   도시 칸에 도착했을 때 가지고 있는 돈이 땅의 가격보다 많거나 같다면, 반드시 땅을 구매해야 한다
    #   도시 칸의 땅을 이미 구매했거나 현금이 부족해서 땅을 구매할 수 없는 경우에는 아무것도 구매하지 않은 것으로 간주하고 게임을 계속 진행한다
    elif board[now_idx] > 0:
        if not used[now_idx] and now_cash >= board[now_idx]:
            used[now_idx] = 1
            now_cash -= board[now_idx]



# 두 주사위 던지기
# 두 주사위의 눈만큼 이동하기
# 도착한 칸에 따른 행동 수행하기
for a, b in dices:
    # 무인도 칸(n번째 칸): 이 칸에 정확히 멈추게 되면, 다음 세 턴 동안 갇히게 된다.
    #    갇혀 있는 동안, 두 주사위를 던졌을 때 눈이 같은 수로 나오면
    #    무인도를 탈출하게 되며 두 주사위를 한 번 더 던져서 나온 수만큼 이동한다.
    if waiting:
        if a != b:
            waiting -= 1
        else:
            waiting = 0
        continue
    
    now_idx += (a + b)

    check()

    if now_cash < 0:
        break



# 모든 턴을 지났을 때 모든 땅을 다 샀다면 승리, 아니면 패배
if now_cash >= 0 and sum(used) == cities:
    print('WIN')
else:
    print('LOSE')