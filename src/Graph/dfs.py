#dfs = 깊이 우선 탐색
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())
visited = [[False]*m for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx, dy = (1,-1,0,0), (0,0,1,-1)

def dfs(x,y):
    visited[x][y] = True
    
    #if
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                dfs(nx, ny)
dfs(0,0)