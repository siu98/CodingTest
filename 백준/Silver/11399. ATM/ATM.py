#백준11399: ATM
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()
res = 0
for i in range(1, N+1):
    res += sum(P[0:i])
print(res) 