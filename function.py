# function_basic 
def add(num1, num2):
    return num1+num2

print(add(1,2))


# function_return
def add_mul(num1, num2):
    return num1+num2, num1*num2

print(add_mul(1,2))

# unpacking
my_add, my_mul = add_mul(1,2)
print(my_add)
print(my_mul)
