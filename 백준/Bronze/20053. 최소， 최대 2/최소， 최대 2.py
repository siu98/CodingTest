#백준20053: 최소, 최대 2
import sys
input = sys.stdin.readline

T = int(input())    #테스트케이스

num = []
for i in range(T):
    N = int(input())    # 개수
    number = list(map(int, input().split()))
    
    
    print(min(number), max(number))