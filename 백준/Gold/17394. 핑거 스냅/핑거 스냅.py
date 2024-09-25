# 어디서 틀렸는지 전혀 모르겠는데,,,
# 해답: https://blog.thecloer.com/99


MAX = 10 ** 5
primes = [1] * (MAX + 1)

for i in range(2, MAX // 2 + 1):
    if not primes[i]:
        continue

    j = i * 2
    while j <= MAX:
        primes[j] = 0
        j += i


def find():
    N, A, B = map(int, input().split())

    if not sum(primes[A:B + 1]):
        return -1

    used = set()
    used.add(N)

    q = [N]

    result = 0
    while q:
        nq = []

        for now in q:
            if A <= now <= B and primes[now]:
                return result

            for nxt in (now // 2, now // 3, now + 1, now - 1):
                if nxt < 0 or nxt in used:
                    continue

                used.add(nxt)
                nq.append(nxt)

        q = nq
        result += 1


T = int(input())

for _ in range(T):
    print(find())
