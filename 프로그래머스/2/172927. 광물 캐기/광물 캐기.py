def solution(picks, minerals):
    sum = 0
    # 곡괭이 수 계산 
    for x in picks:
        sum += x
    
    num_minerals = sum * 5  # 총 광물을 자를 수 있는 수 
    if len(minerals) > num_minerals: # 광물을 자를 수 있는 수보다 광물이 많으면 
        minerals = minerals[:num_minerals] # 자를 수 있을 때까지만 

    cnt_minerals = [[0, 0, 0]for x in range(10)] 
    # 5개씩 묶기 
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_minerals[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_minerals[i//5][1] += 1
        else : 
            cnt_minerals[i//5][2] += 1

    # 피로도 높은 순대로 정렬
    sorted_cnt_min = sorted(cnt_minerals, key = lambda x: (-x[0], -x[1], -x[2]))
    
    # 곡괭이 배정 및 피로도 계산
    answer = 0
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0:
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: 
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: 
                picks[p]-=1
                answer += 25*d + 5*i + s
                break
    return answer