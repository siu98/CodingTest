#백준1110: 더하기 사이클
N = int(input())
cnt = 0
num = N
while True:
    a = N//10
    b = N%10
    c = (a+b)%10
    N = (b*10)+c 

    cnt += 1
    if (N == num):
        break
print(cnt)