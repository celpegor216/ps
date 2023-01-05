# N     | 1 | 2  | 3 | 4 | 5 | 6 |
# // 3  | 0 | -1 | 1 | 0 | 0 | 2 |
# // 2  | 0 | 1  | -1 | 2 | 0 | 3 |
# - 1   | 0 | 1  | 2 | 3 | 4 | 5 |
# total | 0 | 1  | 1 | 2 | 3 | 2 |

import sys
input = sys.stdin.readline

N = int(input())

dp = [[0, 0] for _ in range(4)]

for i in range(2, N + 1):
    min_lst = []

    if not i % 3:
        dp[0].append(i // 3)
        min_lst.append(dp[3][i // 3])
    else:
        dp[0].append(-1)

    if not i % 2:
        dp[1].append(i // 2)
        min_lst.append(dp[3][i // 2])
    else:
        dp[1].append(-1)

    dp[2].append(i - 1)
    min_lst.append(dp[3][i - 1])

    dp[3].append(min(min_lst) + 1)

print(dp[3][N])