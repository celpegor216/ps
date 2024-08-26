N = int(input())

result = 0
for _ in range(N):
    S = input()

    # check[i]: ord('a') + i 번째 글자가 등장했는지 여부
    check = [0] * 26
    # 현재 이전의 글자
    now = ''

    for s in S:
        # 글자가 이전과 달라졌을 경우
        if now != s:
            idx = ord(s) - ord('a')

            # 현재 글자가 이전에 등장한 적이 있는 경우,
            # 모든 문자가 연속해서 나타난 것이 아니므로
            # 이 단어는 그룹 단어가 아님
            if check[idx]:
                break

            now = s
            check[idx] = 1
    else:
        result += 1

print(result)