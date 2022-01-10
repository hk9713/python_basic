# 격자판을 채운 막대의 모양을 출력하는 프로그램

# 격자판의 세로(h), 가로(w) 입력
h, w = map(int,input().split())

board = []
for i in range(h+1):
    board.append([])
    for j in range(w+1):
        board[i].append(0) 

# 막대 개수(n)
n = int(input())

# 각 막대의 길이(l), 방향(d), 좌표(x,y) 입력
for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        for j in range(l):
            board[x][y+j] = 1
    else:
        for j in range(l):
            board[x+j][y] = 1

for i in range(1,h+1):
    for j in range(1,w+1):
        print(board[i][j], end=' ')
    print()




