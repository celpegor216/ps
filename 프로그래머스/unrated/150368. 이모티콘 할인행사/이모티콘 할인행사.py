def solution(users, emoticons):
    # 이모티콘 별 할인율 조합 모두 구하기(전부 다 10%, 하나만 20%, 두 개 20%, ...)
    length = len(emoticons)
    possibles = []
    
    def dfs(level, path):
        nonlocal possibles
        
        if level == length:
            possibles.append(path)
            return
        
        for i in (10, 20, 30, 40):
            dfs(level + 1, path + [i])
    
    dfs(0, [])

    # 각 조합을 돌면서 이모티콘 플러스 가입자 수가 가장 많은지, 최대 이모티콘 플러스 가입자 수와 같다면 판매액이 최대인지 확인
    max_cnt, max_total = 0, 0
    for p in possibles:
        cnt, total = 0, 0
        
        for user in users:
            temp = 0
            
            for i in range(length):
                if p[i] >= user[0]:
                    temp += emoticons[i] * (100 - p[i]) / 100
            
            if temp >= user[1]:
                cnt += 1
            else:
                total += temp
        
        if cnt > max_cnt:
            max_cnt = cnt
            max_total = total
        elif cnt == max_cnt and total > max_total:
            max_total = total
    
    return [max_cnt, max_total]