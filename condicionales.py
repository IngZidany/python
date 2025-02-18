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

#ejemplo de condicionales o sentencias de control

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
    print("Juan no es tu amigo")
elif "Juan" in amigos:
    print("Juan es tu amigo")
else:
    print(individuo," no conoce a Juan")

''' En este caso si Juan no esta en el array de amigos, entonces se ejecutara el primer print,
si Juan esta en el array de amigos entonces se ejecutara el segundo print, de lo contrario se ejecutara
el tercer print que indica que la variable individuo no conoce a Juan.'''