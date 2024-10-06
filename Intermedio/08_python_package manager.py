### 08_python_package manager ###

# pip https://pypi.org/

import numpy

print(numpy.version.version)
numpy_array = numpy.array([47,35,24,62,52,30,30])
print(type(numpy_array))
print(numpy_array * 2)

import pandas # python3 -m pip install pandas

# Comandos de consola de pip:
# python3 -m pip list
# python3 -m pip uninstall pandas
# python3 -m pip show numpy

import requests # python3 -m pip install requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')


print(response)
print(response.status_code)
print(response.json())

# Arithmetics Pakage

from mypakage import arithmetics

print(arithmetics.sum_two_values(1,4))


