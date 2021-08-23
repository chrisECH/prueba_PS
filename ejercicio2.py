# coding=utf-8


def separador(palabra,separa): #metodo separador
    palabra = palabra.lower() #asignamos a minuscula la palabra en caso de que haya mayusculas
    palabra +='_' #signo que indica el final de la cadena
    vocales = ['a','e','i','o','u','á','é','í','ó','ú'] #arreglo de vocales 
    consonantes = ['b','c','ch','d','f','g','h','j','k','l','ll','m','n','ñ','p','q','r','rr','s','t','v','w','x','y','z'] #arreglo de consonantes
    especiales = ['pr','pl','br','bl','fr','fl','tr','tl','dr','dl','cr','cl','gr'] #combinaciones especiales
    i = 0 #variable que sirve como contador del ciclo while
    letras = '' #variable que sirve para guardar las silabar temporalmente
    silabas = [] #arreglo para guardar todas las silabas que se vayan encontrando
    tamanio = len(palabra)

    while i < tamanio: #se ejecuta el bucle mientras el contador sea menor a la cantedad de letras en la palabra
        if palabra[i] == '_': #llega al final de la cadena y se caba 
            
                
            break

        elif palabra[i] in vocales: #si la palabra es vocal
            letras = letras + palabra[i] #asignamos la letra a la vairable donde guarda las silabas temporales
            if  palabra[i+1] != '_':
                if palabra[i+1] in vocales:
                    letras = letras  + palabra[i+1]
                    silabas.append(letras)
                    silabas.append(separa)
                    letras =''
                    i+=2
                    continue
         
            
            j=i+1 #contador que sirve para ubicar las consonantes
            auxiliar = [] #arreglo que sirve para guardar las consonantes

            if j < tamanio:
                while palabra[j] in consonantes: #buscamos las consonantes que hay despues de la ultima vocal encontrada
                    auxiliar.append(palabra[j]) #la guardamos en el arreglo
                    j+=1 #aumentamos 1 en el contador
                #se termina hasta que encuentra una vocal
                #como se termino el ciclo, significa que la ultima posicion guardada de j es una vocal

                if len(auxiliar) == 0:
                    silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                    silabas.append(separa) #añadimos un - para separar las silabas
                    letras = '' #reiniciamos la ariable letras para guardar las ultimas letras que encontramos para formar una silaba
                    i+=1


                if len(auxiliar) == 1: #si solo encontró una consonante, esa consonante le pretenece a la segunda vocal
                    if palabra[j] == '_':
                        letras = letras + auxiliar[0]
                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        break
        
                    silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                    silabas.append(separa) #añadimos un - para separar las silabas
                    letras = '' #reiniciamos la ariable letras para guardar las ultimas letras que encontramos para formar una silaba
                    i = j  #hacemos un cambio de variable donde ahora el contador de i (de la palabra) tmara el valor de j, que fue donde
                    #se encontro la ultima vocal
                    
                    letras = auxiliar[0] + palabra[i]

                    if palabra[i+1] == '_':
                       
                        if palabra[i] in consonantes:
                            letras = letras + palabra[i]
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            letras = '' #reiniciamos la ariable letras para guardar las ultimas letras que encontramos para formar una silaba
                            i+=2 #aumentamos el contador de i
                            continue 


                    elif palabra[i+2] == '_':
                        if palabra[i+1] in vocales :
                            letras = letras + palabra[i+1]
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            letras = '' #reiniciamos la ariable letras para guardar las ultimas letras que encontramos para formar una silaba
                            i+=2 #aumentamos el contador de i
                            continue 
                        elif palabra[i+1] in consonantes:
                            letras = letras + palabra[i+1]
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            letras = '' #reiniciamos la ariable letras para guardar las ultimas letras que encontramos para formar una silaba
                            i+=2 #aumentamos el contador de i
                            continue 

                    silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                    silabas.append(separa) #añadimos un - para separar las silabas
                    letras = '' #reiniciamos la ariable letras para guardar las ultimas letras que encontramos para formar una silaba
                    i+=1 #aumentamos el contador de i

                elif len(auxiliar) == 2:
                    aux = ''
                    for item in auxiliar:
                        aux += item

                    
                    if aux in consonantes:
                        if palabra[j] == '_':
                            letras = letras + aux
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            break

                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        letras = '' #reiniciamos la ariable letras para guardar las ultimas letras que encontramos para formar una silaba
                        i = j  #hacemos un cambio de variable donde ahora el contador de i (de la palabra) tmara el valor de j, que fue donde
                        #se encontro la ultima vocal
                        letras = aux + palabra[i]
                        i+=0

                        silabas.append(letras)
                        silabas.append(separa)
                        letras=''
                    elif aux in especiales:
                        if palabra[j] == '_':
                            letras = letras + aux
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            break

                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        letras = '' #reiniciamos la ariable letras para guardar las ultimas letras que encontramos para formar una silaba
                        i = j  #hacemos un cambio de variable donde ahora el contador de i (de la palabra) tmara el valor de j, que fue donde
                        #se encontro la ultima vocal
                        letras = aux + palabra[i]
                        i+=1

                        silabas.append(letras)
                        silabas.append(separa)
                        letras=''

                    else:
                        if palabra[j] == '_':
                            letras = letras + aux
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            break

                        letras = letras + aux[0]
                        i+=3

                        silabas.append(letras)
                        silabas.append(separa)
                        letras= aux[1]
                elif len(auxiliar) == 3:
                    aux = ''
                    for item in auxiliar:
                        aux += item
                    combina1 = aux[0] + aux[1]
                    combina2 = aux[1] + aux[2]

                    if combina1 in consonantes:
                        if palabra[j] == '_':
                            letras = letras + aux
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            break

                    
                        i = j  #hacemos un cambio de variable donde ahora el contador de i (de la palabra) tmara el valor de j, que fue donde
                        #se encontro la ultima vocal
                        letras =  letras + combina1
                        i+=1

                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        letras = ''
                        letras = aux[2]
                        continue
                    elif combina1 in especiales:
                        if palabra[j] == '_':
                            letras = letras + aux
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            break

                    
                        i = j  #hacemos un cambio de variable donde ahora el contador de i (de la palabra) tmara el valor de j, que fue donde
                        #se encontro la ultima vocal
                        letras =  letras + combina1
                        i+=1

                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        letras = ''
                        letras = aux[2]
                        continue

                    elif combina2 in consonantes:
                        if palabra[j] == '_':
                            letras = letras + aux
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            break

                    
                        i = j  #hacemos un cambio de variable donde ahora el contador de i (de la palabra) tmara el valor de j, que fue donde
                        #se encontro la ultima vocal
                        letras =  letras + aux[0]
                        i+=1

                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        letras = ''
                        letras = combina2
                    elif combina2 in especiales:
                        if palabra[j] == '_':
                            letras = letras + aux
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            break

                    
                        i = j  #hacemos un cambio de variable donde ahora el contador de i (de la palabra) tmara el valor de j, que fue donde
                        #se encontro la ultima vocal
                        letras =  letras + aux[0]
                        i+=0

                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        letras = ''
                        letras = combina2
                        continue
                    else:
                        if palabra[j] == '_':
                            letras = letras + aux
                            silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                            silabas.append(separa) #añadimos un - para separar las silabas
                            break

                        i = j  #hacemos un cambio de variable donde ahora el contador de i (de la palabra) tmara el valor de j, que fue donde
                        #se encontro la ultima vocal
                        letras =  letras + combina1
                        i+=0
                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        letras = ''
                        letras = aux[2]
                        continue
                elif len(auxiliar) == 4:
                    aux = ''
                    for item in auxiliar:
                        aux += item
                    
                    if palabra[j] == '_':
                        letras = letras + aux
                        silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                        silabas.append(separa) #añadimos un - para separar las silabas
                        break
                    
                    letras = letras + aux[0] + aux[1]
                    i=j
                    i+=0
                    silabas.append(letras) #guardamos en el arreglo de silabas las ultimas letras que se hayan guardado en la variable letras
                    silabas.append(separa) #añadimos un - para separar las silabas
                    letras = ''
                    letras = aux[2] + aux[3]
                    continue



        elif palabra[i] in consonantes:
            letras = letras + palabra[i]
            i+=1
            continue

    str1 = ''
    for item in silabas:
        str1 += item
    print(str1)



print('¡BIENVENIDO!') #Mensaje de bienvenida
print('Ingrese una palabra: ') #input de bienvenida
palabra = input() #Guardamos la palabra
separa = '-' #Operador para separar las silabas
separador(palabra, separa) #Llammamos al metodo separador, este separa las palabras en silabas