# 큐는 deque 라이브러리를 가져와서 구현함 맨 앞 인덱스를 뺌(FIFO)
# pop() : 맨 뒤 뺌
# appendleft(0) : 맨 앞 추가
# 정렬 불가
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
q.popleft()
print(q)
# 결과 : deque([2, 3]) 
