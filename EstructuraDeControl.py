#introduccion a estructuras de control en python
''''
Un código es una secuencia de instrucciones, que por norma general son ejecutadas una tras otra. 
Podemos verlo como una receta de cocina, en la que tenemos unos pasos a seguir. Empezamos por el principio,
 vamos realizando cada tarea, y una vez hemos llegado al final, hemos terminado. Nuestra receta en código podría ser la siguiente:
poner_agua_hervir()
echar_arroz_hervir()
cortar_pollo()
freir_pollo()
mezclar_pollo_arroz()
'''
#Estructuras de control en python
#declarando variables para ejemplo 4
a = 20
b = 10
c = 5

#suma de variables 
suma = a + b 
print("la suma de a y b es:", suma)

if suma == 30:
    print(suma/2)
elif suma == 40:
    print(suma/4)
else:
    print(suma*2)