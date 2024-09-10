### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [47,35,24,62,52,30,30]

print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[-1])
print(my_list.count(30))

print("----------------")
my_other_list = [35, 1.77,"Francisco", "Arocha"]
print(my_other_list)
print(type(my_other_list))

"""
age =my_other_list[0]
altura = my_other_list[1]
name = my_other_list[2]
surname = my_other_list[3]

"""

age, altura, name, surname = my_other_list

print(f"Mi nombre es {name} {surname} y mi altura es {altura} y mi edad es de {age}")

existe = "Arocha" in my_other_list
print(existe)

my_other_list.append("Maracaibo")
print(my_other_list[4])

ciudad = my_other_list[4]

print(f"Mi nombre es {name} {surname} y mi altura es {altura} y mi edad es de {age} y vivo en {ciudad}")

print(my_other_list.index("Francisco"))
