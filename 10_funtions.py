### Funciones ###
### ###

def my_funfion():
    print("Esto es un a función")

my_funfion()

def sum_two_values(first_value, second_value):
    print(first_value+second_value)

sum_two_values(10,20)
sum_two_values("10","20")
sum_two_values(10.12,20)
sum_two_values(102323,20234234)

def sum_two_values_with_retun(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_retun(10,5)

print(my_result)

print(sum_two_values_with_retun(10,5))

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Arocha", name = "Francisco")

def print_name_with_default(name, surname, alias="sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Francisco", "Arocha")
print_name_with_default("Francisco", "Arocha","PrOtEoX")

def print_texts(*text):
    print(text)

print_texts("Python","Hola","PrOtEoX")
print_texts("Python")
print_texts("PrOtEoX")

def print_upprt_texts(*texts):
    for text in texts:
        print(text.upper())

print_upprt_texts("Python","Hola","PrOtEoX")
print_upprt_texts("Python")
print_upprt_texts("PrOtEoX")



