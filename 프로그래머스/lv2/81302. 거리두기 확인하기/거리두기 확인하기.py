# 조건: 맨해튼 거리가 2 이상이거나, 2여도 파티션이 사이에 있으면 가능

# 입력값: 5*5 사이즈의 대기실 5개, P는 응시자, O는 빈 테이블, X는 파티션
# 출력값: 대기실 순서대로 거리두기 준수 여부 O / X

def solution(places):
    answer = [1] * 5
    
    def check_partition(n, a, b, position):
        if position == (-2, 0):
            if places[n][a[0] + 1][a[1]] == 'O':
                return 0
        elif position == (0, -2):
            if places[n][a[0]][a[1] + 1] == 'O':
                return 0
        elif position == (-1, -1):
            if places[n][a[0] + 1][a[1]] == 'O' or places[n][a[0]][a[1] + 1] == 'O':
                return 0
        elif position == (-1, 1):
            if places[n][a[0] + 1][a[1]] == 'O' or places[n][a[0]][a[1] - 1] == 'O':
                return 0
        return 1
    
    def check(n):
        # 응시자들의 위치를 배열에 정리
        people = []
        
        for i in range(5):
            for j in range(5):
                if places[n][i][j] == 'P':
                    people.append((i, j))
        
        # 응시자들 사이 거리 확인
        p = len(people)
        
        for i in range(p):
            for j in range(i + 1, p):
                vertical = people[i][0] - people[j][0]
                horizontal = people[i][1] - people[j][1]
                distance = abs(vertical) + abs(horizontal)
                
                # 1이면 즉시 종료
                if distance == 1:
                    return 0
                # 2면 사이에 파티션이 있는지 확인
                elif distance == 2:
                    res = check_partition(n, people[i], people[j], (vertical, horizontal))
                    
                    if not res:
                        return 0
        return 1
        
    # 각 대기실 확인
    for n in range(5):
        answer[n] = check(n)
    
    return answer