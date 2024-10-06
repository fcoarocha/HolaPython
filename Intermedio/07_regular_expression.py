### regular expression ###

import re

#match 

my_string = "Esta es la lección número 7: Expresiones Regulares Lección"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

 
match = re.match("Esta es la lección", my_string)
print(match.span()) # esto es una tupla y la podemos utilizar para inicio y final de los caracters que encontro 
strat, end =match.span()
print(strat, end)
print(my_string[strat:end])


match = re.match("Esta no es la lección", my_other_string)

if match  != None:
    print(match)
    start, end =match.span()
    print(my_other_string[start:end])


# search 

search =re.search("lección", my_string,re.I )
print(search)
star, end = search.span()
print(my_string[star:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

print(re.split(":",my_string))

# sub 

print(re.sub("Expresiones Regulares","RegEx", my_string))
print(re.sub("[L|l]ección","LECCIÓN", my_string))


### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com


pattern = r"[Ll]ección"
print(re.findall(pattern, my_string))

pattern = r"[Ll]ección|[Ee]xpresiones"
print(re.findall(pattern, my_string))


pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"[\D]"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

email ="mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email ="mouredev@mouredev.com.es"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))