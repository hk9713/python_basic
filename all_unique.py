# 리스트 안의 모든 값이 유니크하면 True, 아니면 False 반환
# set() - 중복값을 허용하지 않는다

def all_unique(lst):
    return len(lst) == len(set(lst))

# Sample
x = [1,2,3,4,5,6]
y = [1,2,2,3,4,5]

all_unique(x)
print(all_unique(y))
