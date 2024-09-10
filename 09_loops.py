### Looks ### 
### Ciclos, bucles ###

# While 

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:   
    print(f"""-----------------------------------------------------------
        Se detiene el while    
        Ya que la condición es que my_condition < 10
        El Valo de my_condition = {my_condition}
-----------------------------------------------------------""")

print(f"""
----------------
Inicio del Bucle 
my_condition = {my_condition}
----------------
""")    
while my_condition < 20:
        my_condition += 1
        if my_condition == 15:
            print("""
                La Variable my_condition = 15
                Se detiene la ejecución
                """)
            break
        print(my_condition)

print("""
------------------------------
        Fin del Bucle
------------------------------
""")

print(f"""
----------------
Inicio del FOR 
----------------
""")    

my_list = [35,24,62,52,30,30,17]

for element in my_list:
     print(f"{element}")

print("""
------------------------------
        Fin del Bucle
------------------------------
""")

print(f"""
----------------
Inicio del FOR 
----------------
""")    

my_dict = {"Nombre":"Francisco","Apellido":"Arocha","Edad":"46",1:"Python"}

for element in my_dict.values():
     print(f"{element}")

print("""
------------------------------
        Fin del Bucle
------------------------------
""")



print(f"""
----------------
Inicio del FOR 
----------------
""")    

my_dict = {"Nombre":"Francisco","Apellido":"Arocha","Edad":"46",1:"Python"}

for element in my_dict:
     print(f"{element}")
     if element == "Edad":
        print("""
        ------------------------------
               Break del Bucle
        ------------------------------
        """)
        break


print("""
------------------------------
        Fin del Bucle
------------------------------
""")
print("""
------------------------------
Se continual con el programa
------------------------------
""")


print(f"""
----------------
Inicio del FOR 
----------------
""")    

my_dict = {"Nombre":"Francisco","Apellido":"Arocha","Edad":"46",1:"Python"}

for element in my_dict:
     print(f"{element}")
     if element == "Edad":
        print("""
        ------------------------------
               Se consigui Edad
               Vamos a continuar
        ------------------------------
        """)
        continue


print("""
------------------------------
        Fin del Bucle
------------------------------
""")
print("""
------------------------------
Se continual con el programa
------------------------------
""")


