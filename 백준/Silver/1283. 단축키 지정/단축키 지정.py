N = int(input())
lst = [input().split() for _ in range(N)]

bucket = [0] * 26

for n in range(N):
    flag = 0
    
    # 각 단어의 첫 번째 글자로 단축키 지정 가능한지 확인
    for i in range(len(lst[n])):
        idx = ord(lst[n][i][0].lower()) - ord('a')
        if not bucket[idx]:
            bucket[idx] = 1
            lst[n][i] = '[' + lst[n][i][0] + ']' + lst[n][i][1:]
            flag = 1
            break
    
    # 나머지 글자들로 단축키 지정 가능한지 확인
    if not flag:
        for i in range(len(lst[n])):
            if not flag:
                for j in range(1, len(lst[n][i])):
                    idx = ord(lst[n][i][j].lower()) - ord('a')
                    if not bucket[idx]:
                        bucket[idx] = 1
                        lst[n][i] = lst[n][i][:j] + '[' + lst[n][i][j] + ']' + lst[n][i][j + 1:]
                        flag = 1
                        break

for item in lst:
    for word in item:
        print(''.join(word) + ' ', end ='')
    print()