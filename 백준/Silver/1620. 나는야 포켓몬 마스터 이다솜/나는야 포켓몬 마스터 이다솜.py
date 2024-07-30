# N, M의 최대가 100,000
# 기존: 리스트에 이름을 입력받고 .index()를 써서 이름의 인덱스를 찾음 > 시간 초과
# 변경: 시간을 줄이기 위해 input을 sys.stdin.readline으로 바꾸고 딕셔너리를 사용함
# 주의: sys.stdin.readline의 경우 입력을 받을 때 개행문자(\n)을 포함하므로
#      input에 strip() 메소드로 입력값 좌우의 불필요한 공백이나 개행문자를 삭제함

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_to_idx = dict()
idx_to_name = dict()

for n in range(1, N + 1):
    name = input().strip()
    name_to_idx[name] = n
    idx_to_name[n] = name

for _ in range(M):
    query = input().strip()

    if query.isdigit():    # 문자열이 숫자로만 이루어져있는지 확인
        print(idx_to_name[int(query)])
    else:
        print(name_to_idx[query])