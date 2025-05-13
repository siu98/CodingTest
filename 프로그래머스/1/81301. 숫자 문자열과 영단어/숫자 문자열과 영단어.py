def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tmp = ""
    res = ""
    for i in range(len(s)):
        number = s[i]
        if(number.isnumeric()):
            res += number
        else:
            tmp += number
            if tmp in num:
                res += str(num.index(tmp))
                tmp = ''
    return int(res)