#BFS : 너비 우선 탐색 - 루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법
from collections import deque

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
visited = [[0] * m for _ in range(n)]
dx, dy = (1,-1,0,0), (0,0,1,-1)

q = deque()

q.append((0,0))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))

print(visited[n-1][m-1])