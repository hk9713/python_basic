# 오른쪽과 아래쪽으로만 움직이는 개미의 최적 경로 구하기

# 미로 상자 만들기
box = []
for i in range(10):
    box.append( list(map(int,input().split())) )

# 개미 이동
x, y = 1,1
while True:
    if (box[x][y] == 0):
        box[x][y] = 9
    elif (box[x][y] == 2):
        box[x][y] = 9
        break

    if ((box[x][y+1] == 1 and box[x+1][y] == 1)):
        break

    if (box[x][y+1]!= 1):
        y = y+1
    elif (box[x+1][y] != 1):
        x = x+1

# 결과
for i in range(10):
    for j in range(10):
        print(box[i][j], end=' ')
    print()
