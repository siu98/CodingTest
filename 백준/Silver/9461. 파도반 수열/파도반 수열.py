#백준 9461: 파도반 수열
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * (N + 2)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, N + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    print(dp[N - 1])  
