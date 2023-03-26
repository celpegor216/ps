# 8, 18 해결 못 함
# 해답: https://velog.io/@sewonkim/2022-KAKAO-BLIND-RECRUITMENT-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4

def solution(n, info):
    answer = [-1]
    max_v = 0
    
    def dfs(level, cnt, path):
        nonlocal answer, max_v
        
        if cnt > n:
            return
        
        if level == 11:
            apeach = 0
            lion = 0

            for i in range(11):
                if info[i] == path[i] == 0:
                    continue
                elif info[i] < path[i]:
                    lion += 10 - i
                else:
                    apeach += 10 - i

            if lion - apeach > max_v:
                max_v = lion - apeach
                answer = path[:]
                
                # 남은 화살을 전부 가장 낮은 점수에 넣기
                answer[-1] += n - cnt

            return
        
        # 점수 얻기(어피치보다 많이 쏘기)
        path[10 - level] = info[10 - level] + 1
        dfs(level + 1, cnt + path[10 - level], path)
        
        # 점수 포기(안 쏘기)
        path[10 - level] = 0
        dfs(level + 1, cnt, path)
    
    dfs(0, 0, [0] * 11)
    
    return answer