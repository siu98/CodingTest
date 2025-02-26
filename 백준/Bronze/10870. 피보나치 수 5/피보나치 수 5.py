#백준10870: 피보나치수5
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    fibo = dp[i-1] + dp[i-2]
    dp.append(fibo)
print(dp[n])