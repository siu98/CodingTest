#백준1149: RGB 거리 
import sys
input = sys.stdin.readline
N = int(input())
RGB = [0]*N
for i in range(N):
   RGB[i] = list(map(int, input().split()))
for i in range(1, N):
   RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
   RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
   RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

print(min(RGB[i][0], RGB[i][1], RGB[i][2]))