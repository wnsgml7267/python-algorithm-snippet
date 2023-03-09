'''
-다익스트라(dp 기반)
가중치(양수)가 있으며, 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 알고리즘.

-특징 및 주의할 점
1. 가중치는 무조건 양수여야 적용 가능.
2. 방문 배열(visited) 생성X. (최단 거리를 기록하는 조건문으로 방문 체크를 해줌)
3. 가중치를 우선으로 오름차순 정렬.
'''
from heapq import heappop, heappush # 최소의 가중치를 먼저 뽑아내기 위해 우선순위큐를 주로 사용.
'''
heapq 사용법.
hq = [] # heapq를 적용할 리스트 생성.
heappush(hq, (cost, x, y)) # hq 리스트에 (비용 , x좌표, y좌표) 추가.
cost, x, y = heappop(hq) # hq에서 최소 가중치를 가진 원소를 우선으로 꺼냄.
'''

'''
다익스트라 알고리즘을 이용한 기본 예제 2 가지
1. 4485 녹색 옷입은 애가 젤다지? (입력값 : 인접행렬)
2. 10282 해킹 (입력값 : 인접리스트)
# 소스 코드 주석에 !! 표시 => 다익스트라 핵심 개념
'''

# 1. https://www.acmicpc.net/problem/4485
# 문제 해석 : (0,0)좌표에서 출발하여 (n-1,n-1)에 도착하는 데까지 잃은 최소 금액(양의 가중치) 구하기.
from heapq import heappop, heappush
t, dx, dy = 1, (1,-1,0,0), (0,0,1,-1)
while True:
  n = int(input()) # n x n 좌표
  if n == 0: break
  graph = [list(map(int,input().split())) for _ in range(n)]
  
  
  def dijkstra():
    min_graph = [[10**9 for _ in range(n)] for _ in range(n)] # !! 최소 비용을 구하기 위한 최댓값 설정.
    min_graph[0][0] = graph[0][0] # !!출발점 비용 체크
    hq = [] 
    heappush(hq, (min_graph[0][0], 0, 0)) # !! 출발점의 cost, x, y
    while hq:
      cost, x, y = heappop(hq)
      
      if x == n-1 and y == n-1: # 도착시 기록한 최소 금액 출력
        return min_graph[x][y]
      
      for i in range(4):
        nx, ny = dx[i] + x, dy[i] +y
        # !! 다음 좌표의 금액이 기존에 기록한 최소 금액보다 더 적을 경우에만 값 초기화
        if 0 <= nx < n and 0 <= ny < n and min_graph[nx][ny] > cost + graph[nx][ny]:
          min_graph[nx][ny] = cost + graph[nx][ny]
          heappush(hq, (min_graph[nx][ny], nx, ny))
  
  print("Problem %d:" % t, dijkstra())
  t += 1

# 2. https://www.acmicpc.net/problem/10282
# 문제 해석 : 의존하는 컴퓨터 수와 감염 시간을 보고 감염된 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간 구하기.
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
t = int(input())
for _ in range(t):
    n, d, c = map(int,input().split()) # 컴퓨터 수, 감염 진행 수, 첫 감염
    graph = [[] for _ in range(n+1)] # 컴퓨터 수 + 1 
    min_graph = [10**9] * (n+1) # !! 최단 감염 시간을 구하기 위한 배열
    hq = [] # 최단 감염 시간을 구하기 위한 우선순위큐
    for _ in range(d):
        a, b, time = map(int,input().split()) # b에서 a로 감염되는 시간
        graph[b].append((a,time)) # b를 의존하는 a와 감염 시간을 b 인덱스에 기록

    heappush(hq, (0, c)) # !! 힙에 (감염 누적 시간, 감염 번호) 추가
    min_graph[c] = 0 # !! 첫 컴퓨터에 감염 시간 0 초기화
    while hq:
        vr, num = heappop(hq) # 감염 누적 시간, 컴퓨터 번호
        for k in graph[num]: # num번 컴퓨터를 의존하고 있는 컴퓨터 탐색
            # k[0] : 의존 번호, k[1] : 바이러스 시간
            if k[1] + vr < min_graph[k[0]]: # !! 이전의 최단 감염 시간보다 더 적으면 
                min_graph[k[0]] = k[1] + vr # !! 해당 컴퓨터까지 감염 시간을 초기화
                heappush(hq, (min_graph[k[0]], k[0])) # !! 해당 컴퓨터까지 감염 시간과 컴퓨터 번호 힙에 넣기

    computer_cnt = 0 # 감염된 컴퓨터 수
    virus = 0 # 바이러스 다 퍼진 시간
    for l in min_graph: # 기록한 최단 감염 시간들 하나씩 꺼냄
        if l != 10**9: # 감염 되었을 때
            computer_cnt += 1 # 감염된 컴퓨터 대수 증가
            virus = max(virus, l) # 최단 감염 시간들 중 최댓값
    print(computer_cnt, virus) # 정답 출력