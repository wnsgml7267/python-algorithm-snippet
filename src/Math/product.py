# 중복 순열 : 선택한 것을 다시 제자리에 놓고(중복) 배열하는 것. n^r
from itertools import product as pd
array = ['a','b','c']

for i in list(pd(array,repeat=2)): #2개를 뽑는데, 같은 값 중복 가능
    print(i)
''' 
('a', 'a')
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'b')
('b', 'c')
('c', 'a')
('c', 'b')
('c', 'c')
'''