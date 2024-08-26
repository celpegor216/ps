N = 8    # 입력값의 길이
A = input()
B = input()

# A와 B를 하나씩 번갈아서 나열
now = ''
for i in range(N):
    now += A[i] + B[i]

# 마지막에 남는 숫자 2개로 궁합률을 구함
while len(now) > 2:
    nxt = ''

    for i in range(len(now) - 1):
        # 인접한 두 숫자끼리 더한 값이 두 자리 정수가 될 경우 일의 자리 숫자만 적어야 함
        # -> % 10 사용
        nxt += str((int(now[i]) + int(now[i + 1])) % 10)

    now = nxt

print(nxt)