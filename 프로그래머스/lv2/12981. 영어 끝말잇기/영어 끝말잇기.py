def solution(n, words):
    cnt = 1
    people = 2
    flag = 0
    
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            flag = 1
            break
        else:
            people += 1
            if people > n:
                cnt += 1
                people = 1
    
    return [people, cnt] if flag else [0, 0]