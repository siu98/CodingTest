from collections import deque
def solution(maps):
    n = len(maps)         # 세로 (행)
    m = len(maps[0])      # 가로 (열)
    queue = deque()
    queue.append((0, 0))
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

    answer = maps[n-1][m-1]
    return -1 if answer == 1 else answer