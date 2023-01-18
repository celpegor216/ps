from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    stack = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if city not in stack:
            if len(stack) == cacheSize:
                stack.popleft()
            stack.append(city)
            answer += 5
        else:
            del stack[stack.index(city)]
            stack.append(city)
            answer += 1
    
    return answer