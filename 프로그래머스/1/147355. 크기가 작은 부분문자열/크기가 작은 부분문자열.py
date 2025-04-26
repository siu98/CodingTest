def solution(t, p):
    answer = 0
    pLen = len(p)
    tLen = len(t)
    p = int(p)
    for i in range(0, tLen+1-pLen):
        if int(t[i:i+pLen]) <= p:
            answer += 1
    return answer