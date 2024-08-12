# **1. ¿Qué es una Variable?**

En programación, una **variable** es un contenedor que almacena valores de datos. Es como una "caja" con un nombre que puede contener diferentes tipos de datos, como números, texto, listas, y más. 

### **Características de las Variables:**
- **Nombre:** Cada variable tiene un nombre que la identifica dentro del programa.
- **Valor:** El valor es lo que se almacena dentro de la variable.
- **Asignación:** Una variable se crea cuando se le asigna un valor por primera vez.

### **Ejemplo Básico:**
```python
x = 5
X = 6  # Python distingue entre mayúsculas y minúsculas (case-sensitive).
txt = "Esto es un texto"
```

En este ejemplo:
- `x` es una variable que almacena el número `5`.
- `X` es otra variable (distinta de `x` debido a la sensibilidad de mayúsculas) que almacena el número `6`.
- `txt` es una variable que almacena la cadena de texto `"Esto es un texto"`.

## **2. Nombres Admitidos de Variables**

Los nombres de las variables en Python deben seguir ciertas reglas y convenciones para ser válidos. Es fundamental conocer estas reglas para evitar errores de sintaxis y mejorar la legibilidad del código.

### **a) Reglas para Nombrar Variables:**

1. **Debe comenzar con una letra o un guion bajo (_):**
   ```python
   mivariable = "texto"
   _mivariable = 'otro texto'
   MiOtraVariable = """
   otro texto más
   """
   _MiOtraVariableMás = '''
   otro texto con comillas simples triples
   '''
   ```

2. **No puede comenzar con un número:**
   ```python
   # 5variable = "texto"  # Esto es inválido y causará un error de sintaxis.
   ```

3. **Solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9, _):**
   ```python
   miVariable123_ = "texto"
   _miVariable123_ = "texto"
   ```

4. **Python es case-sensitive:** 
   ```python
   miVariable = "otro texto"
   Mivariable = "otro texto más"
   ```
   En este ejemplo, `miVariable` y `Mivariable` son dos variables diferentes debido a la distinción entre mayúsculas y minúsculas.

5. **No se puede usar palabras reservadas de Python (keywords):**
   ```python
   # if = "condicional"  # Esto es inválido porque 'if' es una palabra reservada.
   ```

### **b) Ejemplos de Nombres Válidos:**
```python
nombre_usuario = "Carlos"
_nombre_usuario = "Carlos"
NombreUsuario = "Carlos"
nombreUsuario = "Carlos"
nombre_usuario123 = "Carlos"
```

Estos nombres son válidos y siguen las reglas mencionadas.

### **c) Convenciones de Nomenclatura:**

Aunque Python permite flexibilidad en los nombres de variables, existen convenciones comunes que ayudan a mejorar la legibilidad del código:

1. **Camel Case:**
   - Comienza con minúscula y cada palabra siguiente inicia con mayúscula.
   ```python
   nombreUsuario = "Carlos"
   miVariableLocal = "Valor"
   ```

2. **Pascal Case:**
   - Cada palabra comienza con mayúscula, incluyendo la primera.
   ```python
   NombreUsuario = "Carlos"
   MiVariableLocal = "Valor"
   ```

3. **Snake Case:**
   - Todas las palabras están en minúscula y se separan por guiones bajos.
   ```python
   nombre_usuario = "Carlos"
   mi_variable_local = "Valor"
   ```

### **d) Uso de `print` para Visualizar Variables:**

El comando `print` se usa para mostrar el valor de una variable en la consola:
```python
print(mivariable)  # Imprime el valor de 'mivariable'
print(_mivariable)  # Imprime el valor de '_mivariable'
print(MiOtraVariable)  # Imprime el valor de 'MiOtraVariable'
print(_MiOtraVariableMás)  # Imprime el valor de '_MiOtraVariableMás'
```

## **3. Asignación de Valores y Multiasignación**

En Python, es posible asignar valores a múltiples variables en una sola línea. Esto puede ser útil para simplificar el código y mejorar la legibilidad.

### **a) Asignación Simple:**
```python
x = 5
y = 7
z = 9
```

### **b) Multiasignación en una sola línea:**
```python
x, y, z = 5, 7, 9
a = b = c = "Hola mundo"
```

### **c) Asignación desde Colecciones:**
Python permite "desempaquetar" una colección (como una lista o tupla) y asignar sus elementos a variables individuales:
```python
frutas = ["naranja", "banana", "mandarina"]
m, n, o = frutas

print(m)  # Imprime "naranja"
print(n)  # Imprime "banana"
print(o)  # Imprime "mandarina"
```

## **4. Variables Globales vs Variables Locales (Scope)**

Las variables pueden tener diferente "scope" o alcance, lo que determina dónde pueden ser utilizadas dentro del programa.

### **a) Variables Globales:**
Son aquellas que se definen fuera de cualquier función y están disponibles en todo el programa.
```python
variableGlobal = "Esta variable es global y accesible en cualquier parte del código"

def funcion():
    print(variableGlobal)  # Accede a la variable global

funcion()
```

### **b) Variables Locales:**
Son aquellas que se definen dentro de una función y solo existen dentro de esa función.
```python
def funcion():
    variableLocal = "Esta variable es local a la función"
    print(variableLocal)

funcion()
# print(variableLocal)  # Esto dará un error porque variableLocal no existe fuera de la función.
```

### **c) Modificación de Variables Globales dentro de una Función:**
Si necesitas modificar una variable global dentro de una función, puedes usar la palabra clave `global`:
```python
contador = 0  # Variable global

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # Imprime 1, porque la función incrementó el valor de la variable global.
```

## **5. Convenciones de Escritura de Variables**

Las convenciones de escritura de variables son importantes para mantener la coherencia y legibilidad del código. A continuación, revisamos las principales:

### **a) Camel Case:**
- Utilizado comúnmente en nombres de variables y funciones.
- Ejemplo: `miVariable`, `nombreCompleto`.

### **b) Pascal Case:**
- Frecuentemente utilizado en nombres de clases.
- Ejemplo: `MiClase`, `NombreUsuario`.

### **c) Snake Case:**
- Utilizado para nombres de variables en proyectos de código abierto.
- Ejemplo: `nombre_usuario`, `mi_variable`.

### **d) Kebab Case:**
- Usado a veces en nombres de archivos y URLs.
- Ejemplo: `mi-variable`, `nombre-usuario`.

## **6. Comentarios en el Código**

Los comentarios son una parte esencial de cualquier código, ya que permiten explicar qué hace el código o por qué se hizo de una cierta manera. En Python, los comentarios se indican con el símbolo `#`.

### **a) Comentarios de Línea:**
Se utilizan para explicar una línea específica de código.
```python
# Esta es una variable que almacena el nombre del usuario
nombre = "Carlos"
```

### **b) Comentarios Multilínea:**
Para comentarios más largos que abarcan varias líneas, puedes usar varias líneas con `#`, o un bloque de comentario con triples comillas (`'''` o `"""`).
```python
"""
Este es un bloque de comentario
que puede usarse para explicar
una sección más extensa del código.
"""
```

## **7. Buenas Prácticas para Nombres de Variables**

### **a) Nombres Descriptivos:**
- Utiliza nombres de variables que describan claramente su propósito.
- Ejemplo: `precio_producto`, `cantidad_total`, `nombre_cliente`.

### **b) Evita Nombres de una Sola Letra (excepto en loops):**
- A menos que estés escribiendo un loop o una función matemática, evita usar nombres de una sola letra.
- Ejemplo: Evita `a`, `b`, `c`, y prefiere `producto`, `cliente`, `total`.

### **c) No Abreviar Innecesariamente:**
- Aunque puede ser tentador abreviar nombres de variables, es mejor ser claro.
- Ejemplo: Evita `prc` en lugar de `precio`.

## **8. Tipos de Variables y Conversión**

Python es un lenguaje de tipado dinámico,

 lo que significa que no necesitas declarar el tipo de una variable antes de asignarle un valor.

### **a) Tipos de Variables:**
- **Enteros (`int`)**: Números enteros, sin decimales.
- **Flotantes (`float`)**: Números con decimales.
- **Cadenas (`str`)**: Texto o caracteres.
- **Booleanos (`bool`)**: Verdadero (`True`) o Falso (`False`).
- **Listas (`list`)**: Secuencia ordenada de elementos.
- **Tuplas (`tuple`)**: Secuencia ordenada e inmutable de elementos.
- **Diccionarios (`dict`)**: Colección de pares clave-valor.

### **b) Conversión entre Tipos:**
- Puedes convertir entre tipos usando funciones como `int()`, `float()`, `str()`, etc.
- Ejemplo:
  ```python
  x = "10"
  y = int(x)  # Convierte el string "10" en un entero 10.
  ```

## **9. Variables Constantes**

Aunque Python no tiene un concepto de constantes como otros lenguajes, se acostumbra a usar variables en mayúsculas para indicar que su valor no debe cambiar.

### **Ejemplo:**
```python
PI = 3.1416
VELOCIDAD_DE_LA_LUZ = 299792458  # en metros por segundo
```
Esto es solo una convención; Python no impide que cambies el valor de estas variables, pero es una forma de indicar que no deberían modificarse.

## **10. Eliminación de Variables**

Puedes eliminar una variable usando la palabra clave `del`:
```python
x = 10
del x  # Ahora, x ya no está definida
```

## **Conclusión**

Las variables son la piedra angular de cualquier programa en Python. Comprender cómo se crean, nombran, y gestionan es crucial para escribir código efectivo y eficiente. Además, seguir las convenciones y buenas prácticas te ayudará a mantener un código legible y mantenible, tanto para ti como para otros desarrolladores que puedan trabajar con tu código en el futuro.