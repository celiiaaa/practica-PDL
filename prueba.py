diccionario = {}

diccionario['Persona1'] = {'nombre': ('str', 'Ana'), 'edad': ('int', 25), "dinero": ('float', 1234.23), 'sexo': ('char', 'f')}

diccionario['Persona2'] = {'nombre': ('str', 'Benito'), 'edad': ('int', 29), "dinero": ('float', 104476545346.24), 'sexo': ('char', 'm')}

print(diccionario)
print("Ana: ", diccionario['Persona1'])
print("Dinero de Ana: ", diccionario['Persona1']['dinero'][1])

print()
print("MODIFICANDO DATOS")
print()

diccionario['Persona1']['dinero'] = ('float', 9999.99)
print(diccionario)

for key in diccionario:
    for prop in diccionario[key]:
        print(f"{prop}: {diccionario[key][prop]}")


print(3 == 3.0000000000)

a = 0
b = 0
if a == b == 0:
    print("si")

var = 0.234
var2 = 12
print(var.is_integer())
print(type(var2))