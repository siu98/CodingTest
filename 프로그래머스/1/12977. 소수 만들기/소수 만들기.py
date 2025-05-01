from itertools import combinations
def solution(nums):
    answer = 0
    
    comList = list(combinations(nums, 3))
    sumList = [sum(n) for n in comList]
    
    n = max(sumList)
    primeNum = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in primeNum:
            primeNum -= set(range(2*i, n+1, i))
            
    for n in sumList:
        if n in primeNum:
            answer += 1

    return answer