# 바둑판(19*19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

"""
d = [] #대괄호[]를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20):
    d.append([]) #리스트 안에 다른 리스트 추가해 넣기
    for j in range(20):
        d[i].append(0) #리스트 안에 들어있는 리스트 안에 0 추가해 넣기
"""

d = [[0 for j in range(20)]for i in range(20)] #List Comprehensions

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    d[a][b]=1

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ') #공백을 두고 한줄로 출력
    print() #줄바꿈