#LIFO(Last In First Out)
a = []
a.append(1) # a = [1]
a.append(2) # a = [1,2]
a.append(3) # a = [1,2,3]

a.pop() # a = [1,2]

print(a) # a = [1,2]

#슬라이싱
slice = [1,2,3,4,5,6,7,8,9] # index 0~8
print(slice[:]) # 전체 그대로 복사
print(slice[3:5]) # (3)인덱스 부터 (5-1)인덱스까지 [4,5]
print(slice[-1]) # 맨 뒤 출력 [9]