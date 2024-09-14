N = int(input())
# lst[i]: i번 집을 배정받은 사람
home_to_person = [0] + list(map(int, input().split()))
person_to_home = [0] * (N + 1)

for n in range(1, N + 1):
    person_to_home[n] = home_to_person.index(n)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    new_person_to_home = person_to_home[:l] + sorted(person_to_home[l:r + 1]) + person_to_home[r + 1:]

    print(*[new_person_to_home.index(n) for n in range(1, N + 1)])