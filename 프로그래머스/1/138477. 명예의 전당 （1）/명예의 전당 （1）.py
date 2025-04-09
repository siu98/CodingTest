def solution(k, score):
    answer = []
    award = []
    for i in score:
        if len(award) < k:
            award.append(i)
        else:
            if min(award) < i:
                award.remove(min(award))
                award.append(i)
        answer.append(min(award))
    return answer