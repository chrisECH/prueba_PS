# coding=utf-8

def contadorLetras(palabra): #funcion contadorLetras
    contador = {} #lista para guardar la letra y las veces que se repiten

    for letra in palabra: #iniciamos un ciclo for para recorrer la palabra
        if letra in contador: #si la letra esta en la lista
            contador[letra] = contador[letra]+1 #sumamos un 1, es decir que esa letra se repitio otra vez
        else: 
            contador[letra] = 1 #si la letra no esta en la lista, la añadimos y le sumamos 1 automaticamente
    return contador #retornamos el contador

def ordenarPalabra(palabra): #inicio funcion ordenarPalabra
    diccionarioPalabra = [] #iniciamos un arreglo, servira para ordenar las letras
    for letra in palabra: #con el ciclo for recorremos la palabra
        diccionarioPalabra.append(letra) #añadimos letra por letra al arreglo

    palabraOrden = sorted(diccionarioPalabra) #con la funcion sorted, ordenamos el arreglo 
    str1 = '' #nos servira para convertir el arreglo a string

    for item in palabraOrden: #con el ciclo for, recorremos el arreglo letra por letra y lo añadimos a la variable str1
        str1 += item
    return str1 #retornamos la palabra ordenada alfabeticamente



print("¡Bienvenido!\n") #Mensaje de bienvenida
print("Ingrese una palabra: ")
palabra = input()  #Input de la palabra

print(contadorLetras(palabra)) #Llamamos a la funcion contadorLetras
print(ordenarPalabra(palabra)) #Llamamos a la funcion ordenar palabra
