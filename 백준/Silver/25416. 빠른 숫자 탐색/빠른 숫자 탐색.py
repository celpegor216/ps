from collections import deque


N = 5
#  -1이 적혀 있는 칸으로는 이동할 수 없고 0, 1이 적혀 있는 칸으로는 이동할 수 있다
lst = [list(map(int, input().split())) for _ in range(N)]
sy, sx = map(int, input().split())

# 학생이 현재 위치 (r, c)에서 시작하여 1이 적혀 있는 칸에 도착하기 위한 최소 이동 횟수
# 이동할 수 없는 경우 –1을 출력
def find():
    q = deque()
    q.append((sy, sx))

    used = [[0] * N for _ in range(N)]
    used[sy][sx] = 1

    result = 0
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()

            if lst[y][x] == 1:
                return result

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx

                if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] != -1:
                    used[ny][nx] = 1
                    q.append((ny, nx))

        result += 1
    
    return -1

print(find())