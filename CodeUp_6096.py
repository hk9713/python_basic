# 바둑알이 깔려 있는 상황이 19*19 크기의 정수값으로 입력된다
# 십자 뒤집기 횟수(n)이 입력됐을 때
# 십자 뒤집기 결과를 출력한다


board = []

for i in range(19):
    board.append([])
    for j in range(19):
        board[i].append(0) 

for i in range(19):
    board[i] = list(map(int,input().split()))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        if board[x-1][j] == 0:
            board[x-1][j] = 1
        else:
            board[x-1][j] = 0

        if board[j][y-1] == 0:
            board[j][y-1] = 1
        else:
            board[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(board[i][j], end=" ")
    print()