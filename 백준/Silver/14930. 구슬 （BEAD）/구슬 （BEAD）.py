# 해답: 팀원 해설 참조
# 핵심은 "완전탄성충돌", 이동하는 것은 구슬이 아닌 에너지
# 처음 위치에서 빨간 구슬의 인덱스를 찾음
# 각 구슬에 부여된 위치 + 속도의 T초 후 위치를 찾음
# T초 후 위치를 정렬
# 구슬이 움직이는 게 아닌 위치 + 속도가 움직이는 것이므로 정렬된 위치에서 빨간 구슬의 인덱스 값을 출력

N, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

red = lst[0]
lst.sort()
red_idx = lst.index(red)

lst_t = sorted([x + T * v for x, v in lst])

print(lst_t[red_idx])