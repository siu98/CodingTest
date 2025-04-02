def solution(n, m, section):
    paint = section[0]
    answer = 1
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
    return answer