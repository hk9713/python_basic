numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []

for number in numbers:
    if number % 2 ==1:
        odd_numbers.append(number)

print(odd_numbers)

# 같은 결과를 훨씬 짧은 코드로!
odd_numbers2 = [number for number in numbers if number % 2==1]
print(odd_numbers2)

