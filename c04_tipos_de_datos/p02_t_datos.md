# Tipos de datos Python

### **1. Cadenas de Texto (`str`)**
Las cadenas de texto en Python son secuencias de caracteres y se pueden definir utilizando comillas simples, dobles o triples.

```python
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """Este es un texto"""
comillasTriplesSimples = '''Este es un texto'''
```

- **Comillas Simples y Dobles:** No hay diferencia funcional entre usar comillas simples (`'`) o dobles (`"`). La elección depende de tu preferencia o del contenido de la cadena.
- **Comillas Triples:** Se usan principalmente para cadenas multilínea o para comentarios tipo docstring. También permiten que la cadena contenga tanto comillas simples como dobles sin necesidad de escapar.

### **2. Enteros (`int`)**
Los enteros son números sin decimales.

```python
numero_entero = 1
```

- **Uso Común:** Para contar, hacer operaciones matemáticas que no requieren decimales, índices en listas, etc.

### **3. Números Decimales (`float`)**
Los números flotantes son números con parte decimal.

```python
numero_decimal = 3.14
```

- **Uso Común:** Para representar mediciones o cálculos que requieren precisión decimal, como en finanzas, física, etc.

### **4. Números Complejos (`complex`)**
Los números complejos tienen una parte real y una parte imaginaria.

```python
numero_complejo = 5 + 2j
```

- **Parte Real:** `5`
- **Parte Imaginaria:** `2j`
- **Uso Común:** En matemáticas avanzadas, ingeniería, física, donde se necesita representar números con parte imaginaria.

### **5. Listas (`list`)**
Las listas son colecciones ordenadas y mutables.

```python
lista = [9, 1, 2, 3, 4, 5]
```

- **Índices:** Cada elemento tiene un índice, comenzando desde `0` para el primer elemento.
- **Mutable:** Puedes cambiar, agregar o eliminar elementos después de crear la lista.

### **6. Tuplas (`tuple`)**
Las tuplas son similares a las listas, pero son inmutables.

```python
tupla = ("a", "b", "c")
```

- **Índices:** Igual que las listas, los elementos están indexados.
- **Inmutabilidad:** Una vez creada, no puedes cambiar, agregar o eliminar elementos.

### **7. Rangos (`range`)**
Los rangos representan una secuencia de números generada dentro de un rango específico.

```python
rango = range(1, 10)
```

- **Uso Común:** Utilizado frecuentemente en bucles `for` para iterar sobre un rango de números.
- **Nota:** El `range(1, 10)` generará números desde `1` hasta `9` (el límite superior es excluyente).

### **8. Diccionarios (`dict`)**
Los diccionarios son colecciones de pares clave-valor.

```python
diccionario = {"nombre": "Sergio Code"}
```

- **Claves Únicas:** Cada clave debe ser única dentro del diccionario.
- **Acceso por Clave:** Puedes acceder a los valores usando las claves correspondientes.

### **9. Conjuntos (`set`)**
Los conjuntos son colecciones desordenadas de elementos únicos.

```python
conjunto = {1, 1, 2, 2, 3}
```

- **Elementos Únicos:** No permite elementos duplicados; en el ejemplo, el conjunto solo contendrá `{1, 2, 3}`.
- **Uso Común:** Para realizar operaciones de teoría de conjuntos como intersección, unión, diferencia, etc.

### **10. Conjuntos Inmutables (`frozenset`)**
Los conjuntos inmutables son similares a los conjuntos, pero no pueden ser modificados después de su creación.

```python
conjunto_inmutable = frozenset([1, 2, 3, 3, 1])
```

- **Uso Común:** Cuando necesitas un conjunto que no pueda ser alterado, por ejemplo, como clave en un diccionario.

### **11. Booleanos (`bool`)**
Los booleanos representan valores de verdad.

```python
booleanoVerdadero = True
booleanoFalso = False
```

- **Operadores Lógicos:** Los booleanos son usados en condiciones y expresiones lógicas (`and`, `or`, `not`).
- **Uso Común:** Control de flujo en decisiones (`if`), bucles, y para evaluar expresiones.

## **Ejemplos de Uso en un Programa:**
Vamos a ver cómo podrían interactuar estos tipos de datos en un programa simple.

```python
# Definiendo varias variables
nombre = "Sergio Code"
edad = 30
altura = 1.75
es_estudiante = True

# Creando una lista de habilidades
habilidades = ["Python", "Java", "SQL"]

# Creando un diccionario que combine todo
perfil = {
    "nombre": nombre,
    "edad": edad,
    "altura": altura,
    "es_estudiante": es_estudiante,
    "habilidades": habilidades
}

# Imprimiendo información
print(f"Perfil de {perfil['nombre']}:")
print(f"Edad: {perfil['edad']}")
print(f"Altura: {perfil['altura']} metros")
print(f"Estudiante: {'Sí' si perfil['es_estudiante'] else 'No'}")
print("Habilidades:", ", ".join(perfil['habilidades']))

# Trabajando con un conjunto
conjunto_numeros = {1, 2, 3, 4, 5}
print("Conjunto original:", conjunto_numeros)

# Añadir un nuevo elemento al conjunto
conjunto_numeros.add(6)
print("Conjunto después de añadir un elemento:", conjunto_numeros)

# Creando un rango y usando en un bucle
for i in range(1, 5):
    print(f"Número en el rango: {i}")
```

Este ejemplo muestra cómo diferentes tipos de datos pueden ser combinados y utilizados en un programa real. La comprensión de estos tipos de datos es fundamental para escribir código eficiente y efectivo en Python.