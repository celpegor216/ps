# 와이어를 하나씩 없애고 union-find

def solution(n, wires):
    answer = n
    
    for i in range(n - 1):
        result = [j for j in range(n + 1)]
        
        def find(a):
            if result[a] != a:
                result[a] = find(result[a])
            return result[a]
        
        def union(x, y):
            boss_x, boss_y = find(x), find(y)

            if boss_y > boss_x:
                result[boss_y] = boss_x
            else:
                result[boss_x] = boss_y
        
        for k in range(n - 1):
            if i != k:
                union(*wires[k])
        
        for a, b in wires:
            result[a] = find(a)
            result[b] = find(b)
        
        cnt_1, cnt_2 = 0, 0
        
        for l in range(1, n + 1):
            if result[l] == result[1]:
                cnt_1 += 1
            else:
                cnt_2 += 1
                
        print(result)
        
        if abs(cnt_1 - cnt_2) < answer:
            answer = abs(cnt_1 - cnt_2)
        
    return answer