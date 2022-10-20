# 중복 조합 : 순서 상관없이, 같은 값을 소유 가능
from itertools import combinations_with_replacement as cwr
array = ['a','b','c']

for i in list(cwr(array,2)): # 2개를 뽑는데, 같은 값 중복 가능, 순서 상관X
    print(i)
''' 
('a', 'a')
('a', 'b')
('a', 'c')
('b', 'b')
('b', 'c')
('c', 'c')
'''