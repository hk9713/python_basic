n = int(input())
k = list(map(int,input().split()))

min = k[0]
for num in k:
    if num <= min:
        min = num

print(min)