N, M, Q = map(int, input().split())

# groups[i]: i번째 그룹에 속한 회사들의 인덱스
groups = [[] for _ in range(101)]
name_to_idx = dict()
companies = []

for n in range(N):
    G, H, P = input().split()
    G, P = int(G), int(P)
    name_to_idx[H] = n
    groups[G].append(n)
    companies.append(P)

stocks = [0] * N

for _ in range(Q):
    cmd = input().split()

    if cmd[0] == '1':
        company_idx = name_to_idx[cmd[1]]
        amount = int(cmd[2])

        cost = companies[company_idx] * amount
        if M >= cost:
            M -= cost
            stocks[company_idx] += amount
    elif cmd[0] == '2':
        company_idx = name_to_idx[cmd[1]]
        amount = min(int(cmd[2]), stocks[company_idx])

        cost = companies[company_idx] * amount
        M += cost
        stocks[company_idx] -= amount
    elif cmd[0] == '3':
        company_idx = name_to_idx[cmd[1]]
        amount = int(cmd[2])

        companies[company_idx] += amount
    elif cmd[0] == '4':
        group_idx = int(cmd[1])
        amount = int(cmd[2])

        for company_idx in groups[group_idx]:
            companies[company_idx] += amount
    elif cmd[0] == '5':
        group_idx = int(cmd[1])
        amount = 100 + int(cmd[2])

        for company_idx in groups[group_idx]:
            companies[company_idx] = (int(companies[company_idx] * amount / 100) // 10) * 10
    elif cmd[0] == '6':
        print(M)
    elif cmd[0] == '7':
        total = M
        for i in range(N):
            total += companies[i] * stocks[i]
        print(total)