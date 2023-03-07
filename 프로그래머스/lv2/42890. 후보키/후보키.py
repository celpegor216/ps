# 해답: https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%ED%9B%84%EB%B3%B4%ED%82%A4-Python

from itertools import combinations

def solution(relation):
    rows = len(relation)
    cols = len(relation[0])
    
    # 가능한 모든 컬럼 조합
    cols_lst = []
    for i in range(1, cols + 1):
        cols_lst += combinations(range(cols), i)
    
    # 유일성 검사
    unique = []
    for col in cols_lst:
        temp = [tuple([r[key] for key in col]) for r in relation]
        
        # 유일성 만족한 경우
        if len(set(temp)) == rows:
            flag = 0
            
            # 최소성 검사
            for u in unique:
                if set(u).issubset(set(col)):
                    flag = 1
                    break
            
            # 최소성 만족한 경우 정답에 넣기
            if not flag:
                unique.append(col)
                
    return len(unique)