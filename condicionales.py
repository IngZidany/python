#Aprendiendo a usar condicionales en python
#Declarando variables 

individuo = "Mateo" #Esto es una variable

amigos = ["Dani","Juan","Melisa"]#Esto es un array
enemigos = ["Pedro","Luis","Carlos"]#Esto es tambien un array

#Condicionales o sentencias de control

''' contexto:
Las condicionales son estructuras de control que nos permiten tomar,
decisiones en base a una condicion de que se cumpla o no.
'''

#ejemplo de condicionales o sentencias de control en python

if "Pedro" in amigos:
    print("Pedro no es tu amigo")
else:
    print("pedro no es amigo de", individuo)

    '''Si Pedro esta en el aaray de amigos, entonces se ejecutara el primer print, 
    de lo contrario se ejecutara el segundo print que indica que, pedro no es amigo de la
    variable individuo en esta caso : "Mateo".'''

print("-------------------------------------------------------------------")

#ejemplo2 de condicionales o sentencias de control

if "Juan" not in amigos:
    print("Juan se filtro en tu lista de amigos")
elif "Juan"  in enemigos:
    print("Juan es tu enemigo")
else:
    print(individuo," no conoce a Juan")

    '''Si Juan no esta en la lista de amigos, entonces se ejecutara el primer print,
    de lo contrario se ejecutara el segundo print, si Juan esta en la lista de enemigos,    
    de lo contrario se ejecutara el tercer print que indica que, la variable individuo no conoce a Juan.'''

print("-------------------------------------------------------------------")

#ejemplo3 de condicionales o sentencias de control| uso de operadores logicos

if "Dani" is  amigos[1]: #comparando si Dani es igual a amigos en la posicion 1 del array
    print("Dani es tu amigo")   #si se cumple la condicion se ejecutara este print
else:
    print("Dani no es tu amigo numero 2")

print("-------------------------------------------------------------------")

#ejemplo4 de condicionales o sentencias de control.
#primer uso de operadores aritmeticos y funciones.

#declarando variables para ejemplo 4
a = 20
b = 10
c = 5

#suma de variables 
suma = a + b 
print("la suma de a y b es:", suma)

#declaramos array
posiblesresultados = [30,20,40,50] 

print("-------------------------------------------------------------------")

if suma in posiblesresultados:#
    def divicion(): #funcion para dividir la suma de a y b
        return suma / c #return es un metodo que nos permite retornar un valor en este caso la divicion de la suma de a y b entre c.
    print("la divicion de la suma de a y b es:", divicion())
else:
    print("division no valida ya que la suma de a + b no se encuentra en posibles resultados")

'''Si el valor de la suma de a +b está en el array se ejecuta la funcion de divicion q retorna la el resultado de la suma,
dividido sobre c , caso sontrario que suma no esté en el array se ejecuta el segunto print'''