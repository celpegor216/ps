# 연결 리스트로 풀었지만 시간초과
# 해답: https://welog.tistory.com/332

import heapq
import sys
input = sys.stdin.readline

class ByLevel():
    def __init__(self, level):
        self.level = level
        self.min_heap = []
        self.max_heap = []
    
    def insert(self, p):
        heapq.heappush(self.min_heap, p)
        heapq.heappush(self.max_heap, -p)

    def find(self, flag):
        if flag > 0:
            while self.max_heap and (problems[-self.max_heap[0]][1] != self.level):
                heapq.heappop(self.max_heap)
            if self.max_heap:
                return -self.max_heap[0]
        else:
            while self.min_heap and (problems[self.min_heap[0]][1] != self.level):
                heapq.heappop(self.min_heap)
            if self.min_heap:
                return self.min_heap[0]
        if not self.max_heap or not self.min_heap:
            levels[self.level] = None
        return 0

class ByCategory():
    def __init__(self, category):
        self.category = category
        self.min_heap = []
        self.max_heap = []
    
    def insert(self, p, l):
        heapq.heappush(self.min_heap, (l, p))
        heapq.heappush(self.max_heap, (-l, -p))
    
    def find(self, flag):
        if flag > 0:
            while self.max_heap and (problems[-self.max_heap[0][1]][0] != self.category or problems[-self.max_heap[0][1]][1] != -self.max_heap[0][0]):
                heapq.heappop(self.max_heap)
            if self.max_heap:
                return -self.max_heap[0][1]
        else:
            while self.min_heap and (problems[self.min_heap[0][1]][0] != self.category or problems[self.min_heap[0][1]][1] != self.min_heap[0][0]):
                heapq.heappop(self.min_heap)
            if self.min_heap:
                return self.min_heap[0][1]
        if not self.max_heap or not self.min_heap:
            categories[self.category] = None
        return 0

def add(p, l, g):
    if not levels[l]:
        levels[l] = ByLevel(l)
    if not categories[g]:
        categories[g] = ByCategory(g)
    problems[p] = [g, l]
    levels[l].insert(p)
    categories[g].insert(p, l)

N = int(input())

problems = [[0] * 2 for _ in range(100001)]
levels = [None] * 101
categories = [None] * 101

for _ in range(N):
    p, l, g = map(int, input().split())
    add(p, l, g)

M = int(input())

for _ in range(M):
    command, *args = input().split()

    if command == 'recommend':
        G, x = map(int, args)
        print(categories[G].find(x))
    elif command == 'recommend2':
        x = int(args[0])

        if x == 1:
            for l in range(100, 0, -1):
                if levels[l]:
                    result = levels[l].find(x)
                    if result:
                        print(result)
                        break
        else:
            for l in range(1, 101):
                if levels[l]:
                    result = levels[l].find(x)
                    if result:
                        print(result)
                        break
    elif command == 'recommend3':
        x, L = map(int, args)
        result = -1
        
        if x == 1:
            for l in range(L, 101):
                if levels[l]:
                    res = levels[l].find(-x)
                    if res:
                        result = res
                        break
        else:
            for l in range(L - 1, 0, -1):
                if levels[l]:
                    res = levels[l].find(-x)
                    if res:
                        result = res
                        break
        
        print(result)
    elif command == 'add':
        p, l, g = map(int, args)
        add(p, l, g)
    elif command == 'solved':
        p = int(args[0])
        problems[p] = [0, 0]