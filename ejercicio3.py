# coding=utf-8

def checkUpercase(password): #inicio funcion checkUpercase
    check = [] #arreglo que nos servira para validar la contraseña
    for c in password: #recorremos la palabra con el cilvo for
        if c.isupper(): #verificamos si la letra es mayuscula
            check.append(c) #si sì es mayuscula, la añadimos al arreglo check
    if len(check) >= 2: #si el arreglo tiene al menos dos letras mayusculas
        return True #retornamos true
    else: #sino tiene almenos dos letras mayusculas
        print('Debe contener al menos 2 letras mayúsculas') #mandamos un mensaje al usuario
        return False #retornamos False

def checkNumbers(password): #inicio funcion checkNumbers
    numbers = [] #arreglo que nos servira para validar los numeros

    for item in password: #recorremos la palabra con un ciclo for
        if item.isdigit(): #verificamos si el caracter es un digito
            numbers.append(item) #si es un digito lo añadimos al arreglo numbers
    
    if len(numbers) < 3: #si el tamaño del arreglo es menor que 3
        print('Debe contener al menos 3 numeros') #mandamos un mensaje de error al usuario
        return False #retornamos falso
    else: #si tiene al menos 3 digitos
        for item in numbers: #recorremos el arreglo para verificar que los numero no esten repetido
            if numbers.count(item) > 1: #verificamos que los numeros no se repitan
                print('Debe contener 3 números no repetidos') #si hay algun numero repetido mandamos un mensaje de error
                return False #retornamos false
        return True #si no hay numero repetido retornamos true

def checkCharacter(password): #inicio checkCharacter
    character = ['*','_','¿','¡','?','#','$'] #arreglo de los caracteres que debe de contener

    for item in password: #recorremos la palabra con un for
        if item in character: #si tiene al menos un caracter del arreglo character
            return True #retornamos true
    
    print('Debe contener alguno de estos carácteres (* _ - ¿ ¡ ? # $)') #si no tiene, mostramos un mensaje de error
    return False #retornamos false

def checkSpace(password): #inicio funcion checkSpace
    if " " in password: #verificamos que no haya un espacio en blando en la contraseña
        print("No debe contener espacios en blanco") #si hay alguno, mostramos un mensaje de error
        return False #retornamos false
    else: #sino hay espacios en blanco
        return True #retornamos true

def checkLenght(password): #inicio funcion checkLenght
    if len(password) < 8: #verificamos que la longitud de la cadena no sea menor a 8 caracteres
        print('La contraseña debe de ser mayor a 8 caracteres.') #si es menor, mostramos un mensaje de error
        return False #retornamos false
    else: #si no es menor a 8 caracteres
        if len(password) > 15: #verificamos que tampoco sea mayor a  15 caracteres
            print('La contraseña debe de ser menor a 15 caracteres.') #mostramo un mensaje de error
            return False #retornamos false
        else: #si no es mayor a 15 caracteres
            return True #retornamos true
              

def validador(password): #inicio validador
    if checkUpercase(password): #mandamos llamar a la funcion checkUpercase para verificar la primera regla
        if checkNumbers(password): #mandamos llamar a la funcion checkNumbers para verificar la segunda regla
            if checkCharacter(password): #mandamos llamar a la funcion checkCharacter para verificar la tercera regla
                if checkSpace(password): #mandamos llamar a la funcion checkSpace para verificar que la cuarta regla
                    if checkLenght(password): #mandamos llamar a la funcion checkLenght para verificar la quinta regla
                        print('¡Contraseña valida!') #si todo paso correctamente, mostramos mensaje de confirmacion
        
            
    
print("¡Bienvenido! Su contraseña debe de contener estas reglas: \n") #mensaje de bienvenida

#mostramos las reglas que debe de contener la contraseña del usuario
print(' 1. Debe contener al menos 2 letras mayúsculas.\n 2. Debe contener al menos 3 números no repetidos.\n 3. Debe contener al menos 1 carácter de esta lista (* _ - ¿ ¡ ? # $)\n 4. No debe contener espacios en blanco. \n 5. Debe tener entre 8 y 15 caracteres, no más, no menos.\n')
#pedimos la contraseña
print("Ingrese una contraseña:")
password = input()
validador(password) #mandamos llamar a la funcion validador y le pasamos la contraseña que se acaba de ingresar