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
    if not i % 3:
        dp[0].append(i // 3)
    else:
        dp[0].append(-1)

    if not i % 2:
        dp[1].append(i // 2)
    else:
        dp[1].append(-1)

    dp[2].append(i - 1)

    div_3, div_2, min_1 = dp[3][dp[0][i]], dp[3][dp[1][i]], dp[3][dp[2][i]]
    min_lst = []
    if div_3 > -1:
        min_lst.append(div_3)
    if div_2 > -1:
        min_lst.append(div_2)
    if min_1 > -1:
        min_lst.append(min_1)
    dp[3].append(min(min_lst) + 1)

print(dp[3][N])
