# Sintaxis, indentación y comentarios

En Python, la sintaxis, la indentación y los comentarios son fundamentales para escribir código limpio, legible y funcional.

### 1. **Sintaxis de Python**
   - **Simplicidad**: Python es conocido por su sintaxis simple y clara, diseñada para ser fácil de leer y escribir.
   - **Bloques de Código**: En Python, no se utilizan llaves `{}` para definir bloques de código como en otros lenguajes de programación. En su lugar, la indentación es lo que define el comienzo y el final de un bloque de código.
   - **Declaración de Variables**: No es necesario declarar explícitamente el tipo de una variable. Python asigna el tipo de dato dinámicamente en el momento de la asignación.
     ```python
     nombre = "María"  # Una cadena de texto
     edad = 25         # Un número entero
     ```

   - **Estructuras de Control**: Python utiliza palabras clave como `if`, `else`, `elif`, `for`, `while`, etc., para crear estructuras de control de flujo.
     ```python
     if edad > 18:
         print("Eres mayor de edad")
     else:
         print("Eres menor de edad")
     ```

### 2. **Indentación en Python**
   - **Propósito**: La indentación en Python no es solo una cuestión de estilo, es una parte integral de la sintaxis del lenguaje. Define la estructura y los bloques de código.
   - **Reglas de Indentación**:
     - Todos los bloques de código dentro de una estructura (como un `if`, `for`, `while`, funciones, clases, etc.) deben estar indentados con el mismo número de espacios.
     - Por convención, se utilizan 4 espacios por nivel de indentación. No se recomienda utilizar tabulaciones (tabs) para evitar errores de mezcla entre tabs y espacios.
     - La consistencia es clave. Todo el código dentro de un mismo bloque debe estar alineado uniformemente.
   - **Ejemplo**:
     ```python
     def saludar(nombre):
         if nombre:
             print(f"Hola, {nombre}!")
         else:
             print("Hola, extraño!")
     ```

   - **Error Común**: Si el código no está correctamente indentado, Python generará un error de sintaxis.
     ```python
     def sumar(a, b):
     resultado = a + b  # Esto dará un error porque no está correctamente indentado
         return resultado
     ```

### 3. **Comentarios en Python**
   - **Propósito**: Los comentarios se utilizan para explicar el código, hacer anotaciones o desactivar temporalmente líneas de código. Los comentarios no se ejecutan.
   - **Comentarios en Línea**: Se utiliza el símbolo `#` para añadir comentarios en línea. Todo lo que sigue al `#` en esa línea será ignorado por el intérprete.
     ```python
     # Esto es un comentario en Python
     nombre = "María"  # Asignación de una cadena de texto a la variable nombre
     ```

   - **Comentarios Multilínea**: No hay una sintaxis específica para comentarios multilínea. Sin embargo, es común usar `#` en cada línea.
     ```python
     # Este es un comentario
     # que abarca varias líneas
     ```

   - **Docstrings**: Para comentarios más largos, como descripciones de funciones o módulos, se pueden usar *docstrings* (cadenas de documentación) utilizando triples comillas (`"""` o `'''`). Aunque técnicamente no son comentarios, pueden ser utilizados para documentar el código.
     ```python
     def saludar(nombre):
         """
         Esta función imprime un saludo personalizado.
         :param nombre: El nombre de la persona a saludar.
         """
         print(f"Hola, {nombre}!")
     ```

### Ejemplo Completo
Aquí tienes un pequeño ejemplo que combina sintaxis, indentación y comentarios:
```python
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: El radio del círculo.
    :return: El área del círculo.
    """
    # Constante pi
    pi = 3.1416
    
    # Fórmula para el área de un círculo
    area = pi * (radio ** 2)
    
    return area

# Llamando a la función con un radio de 5
resultado = calcular_area_circulo(5)
print(f"El área del círculo es: {resultado}")
```

En este ejemplo:
- Se define una función con un docstring que explica su propósito.
- Se usa la indentación para definir el bloque de código dentro de la función.
- Se utilizan comentarios en línea para explicar partes específicas del código.

Mantener una buena práctica en la sintaxis, indentación y comentarios hace que el código en Python sea más legible, fácil de mantener y entender por otros desarrolladores (o por ti mismo en el futuro).