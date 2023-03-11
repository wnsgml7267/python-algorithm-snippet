'''
위상 정렬 : 비순환 방향 그래프(DAG = 싸이클이 존재하지 않는 방향성이 있는 그래프)에서 정점을 선형으로 정렬하는 것.

-특징
    - 정렬의 순서는 유향 그래프의 구조에 따라 여러 개의 종류가 나올 수 있다.
    - 그래프의 순환이 존재하지 않아야 한다.
    - 순서가 정해진 작업들을 차례대로 수행해야할 때, 그 순서를 결정하는 알고리즘이다.
    - 정점들을 변의 방향을 거스르지 않도록 나열하는 것을 의미한다.
    - 무향 그래프가 안되는 이유 : 순서가 없어서(양방향이라 선후관계가 없음. 또한, 양방향은 싸이클이 발생)

-위상 정렬 가능 여부로 알아볼 수 있는 것.
    - 사이클 발생 여부를 확인 가능하다.
    - 가능하다면 정렬된 결과를 얻을 수 있다.

-위상 정렬 구현 방식
    1. BFS(이해가 더 쉬움)
    2. DFS
'''

# 위상정렬 알고리즘을 이용한 문제 (선수과목)
# https://www.acmicpc.net/problem/14567 
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
level = [0 for _ in range(n+1)] # 진입 차수 : 1 ~ n번의 진입차수 결정
grade = [0 for _ in range(n+1)] # 학기
graph = [[] for _ in range(n+1)] # 노드 연결한 트리
q = deque()

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b) # a과목이 b의 선수 과목이다.
    level[b] += 1 # 선수 과목 a부터 수강해야하므로 b 진입 차수 증가

for i in range(1, n+1):
    if level[i] == 0: # 진입 차수 0은 큐에 삽입
        q.append((i, 1)) 
        grade[i] = 1 # 1학기에 수강

# 진입 차수 0부터 시작
while q:
    x, cnt = q.popleft()
    for i in graph[x]:
        level[i] -= 1
        if level[i] == 0: # 연결 끊기
            q.append((i, cnt + 1))
            grade[i] = cnt + 1 # 다음 학기
print(*grade[1:])
