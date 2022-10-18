#덱 : 큐와 스택을 포함
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)

q.popleft() # 맨 앞 꺼내기
q.pop() # 맨 뒤 꺼내기
print(q)

# 결과 : deque([2,3])