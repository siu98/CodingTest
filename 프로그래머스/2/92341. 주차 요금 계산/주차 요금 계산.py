import math
def solution(fees, records): 
    answer = []
    car = {} #딕셔너리 생성
    times = {} 
    for i in records:
        time, carNumber, inOut = i.split()
        hour, minute = time.split(":")
        minutes = int(hour)*60 + int(minute)    #분으로 환산
        if inOut == "IN":
            car[carNumber] = minutes # ex) car[5961] = 334
        elif inOut == "OUT":
            time = minutes-car[carNumber]
            if carNumber in times:
                times[carNumber] += time
            else:
                times[carNumber] = time
            del car[carNumber]
    
    # 출차 안한 차량 정산하기
    for key, value in car.items():
        time = 23*60 + 59 - value
        if key in times:
            times[key] += time
        else:
            times[key] = time 
    # 정산하기 
    for key, value in times.items():
        extraTime = max(0, value - fees[0]) # 기본 시간 이하일 때
        money = fees[1] + math.ceil(extraTime/fees[2])*fees[3]
        times[key] = money
    times = sorted(times.items())
    for key, value in times:
        answer.append(value)

    return answer