### Funciones de orden superior ###
from functools import reduce

def sum_one(value):
    return value + 1 

def sum_five(value):
    return value + 5 

def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_one(5,2, sum_one)) 
print(sum_two_values_and_add_one(5,2, sum_five))

### Closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(1))

### Built-in Higher Order Funtions ###

numbers = [2,5,10,21,30]

# Map

def multiply_two(numbre):
    return numbre * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda numbre:numbre * 2, numbers)))


# Filter
def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_that_ten,numbers)))

print(list(filter(lambda number : number > 10, numbers)))

# Reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))

