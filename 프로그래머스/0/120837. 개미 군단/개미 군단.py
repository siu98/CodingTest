def solution(hp):
    ant1 = 0    #장군개미
    ant2 = 0    #병정개미
    ant1 = hp // 5
    hp = hp % 5
    ant2 = hp // 3
    hp = hp % 3
    return ant1 + ant2 + hp