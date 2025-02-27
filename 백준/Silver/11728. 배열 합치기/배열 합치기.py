#백준11728: 배열합치기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = A+B
res.sort()
print(*res)