import sys
input = sys.stdin.readline

computer = int(input())
graph = [[] for _ in range(computer+1)]
network = int(input())
visited = [False]*(computer+1)
for _ in range(network):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def DFS(v):
    global count
    visited[v] = True
    count += 1
    for i in graph[v]:
        if visited[i]:
            continue

        DFS(i)

count = 0        
DFS(1)
print(count-1)