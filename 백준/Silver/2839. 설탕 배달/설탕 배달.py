#백준 2839 : 설탕 배달
import sys
input = sys.stdin.readline

N = int(input())
count = 0

while(N>=0):
    if N%5==0:
        count += int(N/5)
        print(count)
        break
    N -= 3
    count += 1

else:
    print(-1)