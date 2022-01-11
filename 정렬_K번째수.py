"""
# 내 코드

def solution(array, commands):
    answer = []
    n = len(commands)
    for i in range(n):
        re_array = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(re_array[commands[i][2]-1])
    return answer    

"""
# 한줄 코드
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1],commands))

solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])