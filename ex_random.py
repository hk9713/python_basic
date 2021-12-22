import random
students = ['하경', '하은', '공주', '꾸꾸']

# choice - 선택
print(random.choice(students))

# sample() - 여러개의 값을 중복없이 뽑을 수 있다
print(random.sample(students,2))

# randint() - 숫자 범위를 지정해서 그 중에서 선택
print(random.randint(1,10))