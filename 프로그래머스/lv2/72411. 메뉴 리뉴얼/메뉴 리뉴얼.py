# 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return
# -> 2명 이상의 손님으로부터 주문되었다고 해서 다 추가하는 게 아님!!!! 

def solution(orders, course):
    answer = []
    
    # 가능한 코스요리 조합
    possibles = set()
    
    def dfs(level, next, path):
        if level in course:
            possibles.add(''.join(sorted(path)))
        
        if level == max_length:
            return
        
        for i in range(next + 1, max_length):
            dfs(level + 1, i, path + [order[i]])
    
    for order in orders:
        max_length = len(order)
        dfs(0, -1, [])
    
    results = [[] for _ in range(max(course) + 1)]
        
    # 코스 별로 주문 이력이 2회 이상인지 확인
    for p in possibles:
        length = len(p)
        cnt = 0
        for order in orders:
            flag = 0
            for m in p:
                if m not in order:
                    flag = 1
                    break
            if not flag:
                cnt += 1
        if (not results[length] and cnt > 1) or (results[length] and results[length][0] < cnt):
            results[length] = [cnt, p]
        elif results[length] and results[length][0] == cnt:
            results[length].append(p)
    
    for result in results:
        if result:
            answer += result[1:]
    
    return sorted(answer)