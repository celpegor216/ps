# union find로 하는 건 맞췄는데 구현에서 틀림

def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x: x[2])
    group = [i for i in range(n)]
    
    def find(a):
        if group[a] == a:
            return a
        group[a] = find(group[a])
        return group[a]
    
    def union(x, y, c):
        nonlocal answer
        
        boss_x, boss_y = find(x), find(y)
        
        if boss_x != boss_y:
            group[boss_y] = boss_x    # 이 부분을 group[y] = boss_x라고 해서 틀렸네,,,
            answer += c
    
    for cost in costs:
        x, y, c = cost
        
        if x > y:
            x, y = y, x
        
        union(x, y, c)
    
    return answer