#순열 : 서로 다른 n 개 중 r 개를 골라 순서를 정해 나열하는 가짓수
#nPr = n! / (n-r)!
from itertools import permutations as pt

array = ['A', 'B', 'C']
for i in list(pt(array, len(array))):
    print(i)

''' 
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
'''