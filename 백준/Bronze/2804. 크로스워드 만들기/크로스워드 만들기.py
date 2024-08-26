A, B = input().split()
N, M = len(A), len(B)

# A와 B가 공유하는 글자의 A에서 인덱스, B에서 인덱스
def find():
    # A의 인덱스를 기준으로 B를 한 글자씩 탐색
    # 겹치는 부분이 있으면 바로 종료하고자 함수 사용
    for a in range(N):
        for b in range(M):
            if A[a] == B[b]:
                return (a, b)

crossed_point = find()

# 출력은 총 M줄, 각 줄에 N개의 문자가 있어야 함
result = [''] * M

for i in range(M):
    if i == crossed_point[1]:
        result[i] = A
    else:
        result[i] = '.' * crossed_point[0] + B[i] + '.' * (N - crossed_point[0] - 1)

for line in result:
    print(line)