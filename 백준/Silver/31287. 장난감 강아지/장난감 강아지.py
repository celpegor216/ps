N, K = map(int, input().split())
S = input()


def find():
    y = x = 0

    used = [set() for _ in range(N)]
    for _ in range(K):
        for n in range(N):
            s = S[n]
            if s == 'U':
                y -= 1
            elif s == 'D':
                y += 1
            elif s == 'L':
                x -= 1
            elif s == 'R':
                x += 1

            if y == x == 0:
                return 'YES'

            if (y, x) in used[n] or abs(y) > N or abs(x) > N:
                return 'NO'
        
            used[n].add((y, x))

    return 'NO'


print(find())