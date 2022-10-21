#딕셔너리 key, value값으로 정렬하기, 참조 문제 : https://www.acmicpc.net/problem/2456
#value값이 리스트여도 가능
dic = {1: [13, 3, 1], 2: [10, 1, 2], 3: [13, 2, 3]}
d = sorted(dic.items(), key=lambda x:x[1], reverse=True) # value값 기준으로 정렬
#d = sorted(dic.items(), key=lambda x:x[0], reverse=True) key값 기준으로 정렬
print(d) #[(1, [13, 3, 1]), (3, [13, 2, 3]), (2, [10, 1, 2])]

#딕셔너리의 키, 값 추출하여 리스트 만들기
dictionary = {'b': 4, 1: 8, 'a': 2}
print(list(dictionary)) # 키 리스트 ['b', 1, 'a']
print(list(dictionary.keys())) # 키 리스트 ['b', 1, 'a']
print(list(dictionary.values())) # 값 리스트 [4, 8, 2]

#딕셔너리 dfaultdict() 딕셔너리 키의 초기값 세팅해줌.
from collections import defaultdict
dt = defaultdict(list)
dt2 = defaultdict(int)
print(dt[1]) # value = [] 
print(dt2[1]) # value = 0