###  Tuples ###
### Es un conjunto de valores como list pero no se pueden modificar los valores ###

my_tuple = tuple()
my_other_tuple = tuple()

my_tuple = (35, 1.77, "Brais", "Moure")
my_other_tuple = (35, 60, 45)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4])  IndexError comienza en  0
#print(my_tuple[-6]) IndexError No llega a ese posición 

print(my_tuple.count("Moure"))
print(my_tuple.index("Moure"))

print(my_tuple + my_other_tuple)

my_sum_tuble = my_tuple + my_other_tuple

print(my_sum_tuble)

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple = tuple(my_tuple)

print(type(my_tuple))

del my_tuple

# print(my_tuple) ya la borramos 

