'''
유니온 파인드(Union-Find) : 그래프 알고리즘으로 두 노드가 같은 그래프에 속하는지
판별하는 알고리즘이다.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

v, e = map(int,input().split()) # 정점, 간선
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i # 자신을 가리키는 초기 노드 생성

def find(a):
    # 경로 압축 O (해당 노드의 부모 노드를 바로 저장시킴) - 시간 복잡도 개선
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

    # 경로 압축 X
    # if a == parent[a]:
    #     return a
    # return find(parent[a])
    
def union(a,b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot == bRoot:
        return False
    parent[bRoot] = aRoot
    return True

edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int,input().split())
    heappush(edges, (cost, a, b))
while edges:
    cost, a, b = heappop(edges)
    if(union(a,b)):
        total_cost += cost
print(total_cost)