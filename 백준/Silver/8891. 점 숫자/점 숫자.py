# 인덱스 에러 발생함 > 두 숫자의 합이 num_MAX보다 클 수 있음
# > 1 부터 9999까지 모든 점 숫자의 2개 조합을 만들어서 최대 x, y를 구해봤더니 282가 나옴
# > 안전한 크기인 300으로 배열 크기 늘렸음
# > num_to_pos 기준으로 pos_to_num 배열을 채웠었는데 반대로 채움
num_to_pos = [[]]    # 점 숫자 > 위치 배열
pos_MAX = 300    # 위치 > 점 숫자 배열
pos_to_num = [[0] * pos_MAX for _ in range(pos_MAX)]

x = y = 1
cnt = 1
num = 1
while cnt < pos_MAX:
    num_to_pos.append((x, y))
    pos_to_num[x][y] = num
    num += 1

    if x == cnt:
        cnt += 1
        y = cnt
        x = 1
    else:
        y -= 1
        x += 1

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    x = num_to_pos[A][0] + num_to_pos[B][0]
    y = num_to_pos[A][1] + num_to_pos[B][1]
    print(pos_to_num[x][y])