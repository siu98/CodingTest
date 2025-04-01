from heapq import *
def solution(n, k, enemy):
    answer = 0
    sum = 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        sum += e
        if sum > n:
            if k ==0:
                break
            sum += heappop(heap) 
            k -= 1
        answer += 1
    return answer