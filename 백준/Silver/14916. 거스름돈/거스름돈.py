#백준14916: 거스름돈 
import sys
input = sys.stdin.readline

n = int(input())
answer = 0

while True:
    if n%5 == 0: #금액이 5원으로 나누어 떨어질 때
        answer += n//5
        break
    else:
        n -= 2
        answer += 1

if n<0:
    print(-1)
else:
    print(answer)