### File Handling ###

import os

# .txt file 
txt_file = open("./my_file.txt","w+") #Leer y escribir
txt_file.write("Mi nombre es Francisco \nMi apellido es Arocha\nTengo 46 años\nY mi lenguale de programación favorito es Python") 
txt_file.write("\nAunque también me gusta kotlin")

txt_file.close()

txt_file = open("./my_file.txt","r") #Leer y escribir

#print(txt_file.read())
#print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)
print(txt_file.readline())
txt_file.close()

#os.remove("./my_file.txt")

# .json file 
import json

json_file = open("./my_json.json","w+")

json_test = {"name":"Francisco",
             "surname":"Arocha",
             "age":"46",
             "language":["Python","Swift","Kotlin"],
             "website":"http:\\moure.dev"}

json.dump(json_test,json_file, indent = 2) #indent es el espacio que deja al principio de cada linea 
json_file.close()

with open("./my_json.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./my_json.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# csv file

import csv

csv_file = open("./my_csv.csv","w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language","website"])
csv_writer.writerow(["Brais","Moure","35","Python","https://moure.dev"])
csv_writer.writerow(["Francisco","Arocha","46","Python","http://franciscoarocha.com.ar"])
csv_file.close()
with open("./my_csv.csv") as my_other_file:
    for line in my_other_file:
        print(line)



