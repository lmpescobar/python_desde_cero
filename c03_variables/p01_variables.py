# Variables
# Es un contenedor para almecenar valores de datos.
# Este contendor va a tener un nombre.
# Es creada la primera vez que se le asigna un valor

x = 5
X = 6 # caseSensitive (interpreta como distinto una mayúscula de una minúscula)
txt = "Esto es un texto"

# Nombres admitidos de variables 

# 1. Puede empezar con una letra o un guión bajo (underscore)
mivariable = "texto"
_mivariable = 'otro texto'
MiOtraVariable = """
otro texto más
"""
_Miotravariablemás = '''
otro texto con comillas simples triples
'''

print (mivariable)
print (_mivariable)
print (MiOtraVariable)
print (_Miotravariablemás)

# 2. No puede iniciar con número
# 5variable = "texto"
# print(5variable)

# 3. Sólo pueden contener caracteres alfanuméricos y guiones bajos (A-z 0-9 _)
miVariable123_ = "texto"
_miVariable123_ = "texto"

# 4 . CaseSensitive (no solo al comienzo sino en general)
miVariable = "otro texto"
Mivariable = "otro texto mas"

# 5. No se puede utilizar palabras reservadas de Python (keywords)

asd123 = "informacion"

##########################

# Convenciones de escritura de variables

# Camel Case
camelCase = "Comienza con minúscula y cada palabra siguiente comenzará con mayúscula"

# Pascal Case
PascalCase = "Comienza con mayúscula y cada palabra siguiente comenzará con mayúscula"

# Snake Case
snake_case = "Se usan las palabras en minúscula y las palabras son separadas con guiones bajos"

# Multiasignación
x,y,z = 5,7,9
a= b = c = "Hola mundo"

# Desde colecciones
frutas = ["naranja", "banana", "mandarina"]
m,n,o = frutas

print(m)
print(n)
print(o)

# Uso de print y salidas:

txt = "Curso"
txt2 = "de "
txt3 = "Python"

num1 = 2
num2 = 4
num3 = 6

print(txt, num1)

# Variables globales vs Variables de Scope

variableGlobal = "Esta variable va a estar disponible para todo el programa"

def funcion():
    variableDeScope = "Esta variable sólo estará disponible dentro del alcance de la función"
    print(variableGlobal)
    print(variableDeScope)

funcion()

print(variableGlobal)
print(variableDeScope)
