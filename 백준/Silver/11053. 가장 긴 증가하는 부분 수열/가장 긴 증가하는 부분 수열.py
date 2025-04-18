#백준11053: 가장 긴 증가하는 수열
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))