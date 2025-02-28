# Introducción a funciones en Python

# Una función es un bloque de código que realiza una tarea específica. 
# Las funciones nos permiten reutilizar código y hacer que nuestro programa sea más modular y fácil de mantener.

# Definición de una función simple
def saludar():
    print("Hola, bienvenido a la introducción de funciones en Python!")

'''
Una función se define con la palabra clave def, seguida del nombre de la función y paréntesis.
Si la función recibe parámetros, estos se colocan dentro de los paréntesis.
La definición de la función termina con dos puntos (:).
El código que forma parte de la función se escribe con sangría.
'''

# Llamada a la función
saludar()

# Funciones con parámetros
def saludar_persona(nombre):#nombre es un parametro de la funcion saludar_persona 
    print(f"Hola, {nombre}, bienvenido a la introducción de funciones en Python!")#esta funcion recibe un parametro y lo imprime

# Llamada a la función con un argumento
saludar_persona("Juan")

# Funciones con valores de retorno
def sumar(a, b):
    return a + b

# Llamada a la función y uso del valor retornado
resultado = sumar(5, 3)
print(f"La suma de 5 y 3 es: {resultado}")

print("-------------------------------------------------------------------")

#ejemplo5 de condicionales o sentencias de control| uso de operadores logicos

'''Se pide desarollar un programa que imprima una receta ,
de cocina si el usuario come carne o es vegano'''

#desarrollo del programa del ejemplo 5

#declarando funcion
def imprimir_receta():
    tipo_de_comida = input("Eres vegano o comes carne?").strip().lower()#input es un metodo que nos permite pedir un valor al usuario
    
    if tipo_de_comida == "vegano":
        print("Receta sugerida para veganos: \n")
        print("1. Arroz integral \n")
        print("2. Lentejas con verduras \n")
        print("3. Ensalada de frutas \n")
        #si el usuario es vegano se imprime la receta para veganos
    elif tipo_de_comida == "carne":
        print("Receta sugerida para carnivoros: \n")
        print("1. Pollo a la plancha \n")
        print("2. Arroz con coco \n")
        print("3. Ensalada de lechuga \n")
        #si el usuario come carne se imprime la receta para carnivoros
    else:
        print("Opción no válida. Ingresa 'vegano' o 'carne'.")
        #si el usuario no es vegano ni come carne se imprime este mensaje
#llamamos la funcion
imprimir_receta()
