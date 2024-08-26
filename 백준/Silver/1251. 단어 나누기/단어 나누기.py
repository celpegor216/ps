# 파이썬에서는 연산자를 사용해서 문자열이 사전순으로 앞서는지 비교할 수 있음

S = input()
N = len(S)

# 어떻게 글자를 나누어서 뒤집더라도 그것보다 사전순으로 뒤에 나오는 글자로 초기화
result = 'z' * N

# 첫 번재 나누는 지점
for i in range(1, N - 1):
    # 두 번째 나누는 지점
    for j in range(i + 1, N):
        tmp = S[:i][::-1] + S[i:j][::-1] + S[j:][::-1]

        if result > tmp:
            result = tmp

print(result)