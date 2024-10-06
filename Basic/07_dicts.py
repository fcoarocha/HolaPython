### Diccionarios ###

my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Francisco","Apellido":"Arocha","Edad":"46",1:"Python"}

my_dict = {
    "Nombre":"Francisco",
    "Apellido":"Arocha",
    "Edad":"46",
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.77
}

print(my_other_dict)
print(my_dict)
print(len(my_other_dict))
print(len(my_dict))

print(my_other_dict.get("Nombre"))
print(my_other_dict["Nombre"])

my_dict["Nombre"] = "Jose"

print(my_dict)

my_dict["Calle"]= "Calle Wenceslao de tata"

print(my_dict["Calle"])

del my_dict["Calle"]

print(my_dict)

print("Francisco" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
# print(my_dict.fromkeys)()

my_new_dict = my_other_dict.fromkeys(("Nombre","Apellido"))
print(my_new_dict)

print(list(my_dict))

