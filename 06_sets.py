### Sets  ####
###  Es como las list pero no es ordenada  ####
###  No adminte repetidos ####

my_set =set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Francisco", "Arocha", 46}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("PrOtOx")
print(my_other_set)


print("Francisco" in my_other_set)
print("Franci" in my_other_set)
my_other_set.remove("Francisco")

print(my_other_set)

my_other_set.clear()

print(my_other_set)

del my_other_set

# print(my_other_set) ameError: name 'my_other_set' is not defined

my_set ={"Francisco", "Arocha", 46}
my_list = list(my_set)

print(my_list)

print(type(my_list))
 
my_other_set ={"Kotlin","Swift","Python"}

my_new_set = my_set.union(my_other_set)

print(my_new_set.union(my_other_set).union(my_set).union({"JavaScript","C#"}))

print(my_new_set.difference(my_set))


