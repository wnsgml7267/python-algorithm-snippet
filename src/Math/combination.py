# 조합 : n개의 값 중에서 r 개의 숫자를 순서를 고려하지 않고 나열한 경우의 수
'''
nCr
= nPr / r!
= n! / ((n-r)! * r!)
'''
from itertools import combinations as cb
array = [1,2,3,4,5]
for i in list(cb(array, 3)):
    print(i)

'''
(1, 2, 3)
(1, 2, 4)
(1, 2, 5)
(1, 3, 4)
(1, 3, 5)
(1, 4, 5)
(2, 3, 4)
(2, 3, 5)
(2, 4, 5)
(3, 4, 5)
'''