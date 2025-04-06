def solution(storey):
    answer = 0
    while storey:
        elevator = storey % 10
        if elevator > 5:
            answer += (10-elevator)
            storey += 10
        elif elevator < 5:
            answer += elevator
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += elevator
        storey //= 10
            
    return answer