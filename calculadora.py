import math
#Imprime el error generado, o error general
def error(str = ''):
    if len(str):
        print("resultado >> ERROR! Expresión no valida, ", str)
    else:
        print("resultado >> ERROR! Expresión no valida")

#Devuelve 1 si la palabra contiene un caracter
def contiene(str, letra):
    existe = 0
    for caracter in str:
        if caracter == letra:
            existe = 1
            break
    return existe

# Cuenta la cantidad de coincidencias en el caracter que se busca
def contar(str, letra):
    aux = 0
    for caracter in str:
        if caracter == letra:
            aux = aux + 1
    return aux

#Valida si lo recibido es un Numero
def esNumero(str):
    try:        
        valFloat = float(str)
        valInt = int(valFloat)
        if (valFloat - valInt) == 0:
            return valInt
        return valFloat
    except ValueError:
        return 'False'

#Cuenta los espacios que hay entre cada caracter
def espacios(str):
    espacios = 0
    anterior = ''
    espacio = ' '    
    for x in range(len(str)):
        if x == 0:
            anterior = str[x]
            continue
        if anterior == espacio and str[x] == espacio:
            espacios = espacios + 1
        anterior = str[x]
    return (espacios == 0)


#Valida que en la expresion no exita un espacios entre parentesis,  numero u operador
def expresionCorrecta(str):
    return (str[1] != ' ' and str[len(str) - 2]  != ' ')

def posLastChar(str, letra):
    position = 0
    for x in range(len(str)):
        if str[x] == letra:
            position = x
    return position

def posFirstChar(str, letra):
    position = 0
    for x in reversed(range(len(str))):
        if str[x] == letra:
            position = x
    return position

def realizarOperacion(commands):
    resultado = 'A'
    if esNumero(commands[1])  != 'False' and esNumero(commands[2])  != 'False':
        numA = esNumero(commands[1])
        numB = esNumero(commands[2])
        if commands[0] == '-':
            resultado = numA - numB
        elif commands[0] == '+':
            resultado = numA + numB
        elif commands[0] == '*':
            resultado = numA * numB
        elif commands[0] == '/':
            if numB == 0:
                error(' Division entre cero')
            else:
                resultado = numA / numB
    return resultado

def realizarFuncion(commands):
    resultado = 'A'
    if esNumero(commands[1])  != 'False':
        numA = esNumero(commands[1])
        if commands[0] == 'sqr':
            resultado = numA * numA
        elif commands[0] == 'sqroot':
            resultado = math.sqrt(numA)
        elif commands[0] == 'sen':
            resultado = math.sin(numA)
        elif commands[0] == 'cos':
            resultado = math.cos(numA)
        elif commands[0] == 'tan':
            resultado = math.tan(numA)
    return resultado

def analizarCommando(entrada):
    if esNumero(entrada) != 'False':
        print('respuesta >> ', entrada)
    else:
        command = entrada[posLastChar(entrada, '('): len(entrada)]
        command = command[0:posFirstChar(command, ')') + 1]        
        if expresionCorrecta(command):
            strAux = entrada[0:posLastChar(entrada, '(')]
            strAux2 = entrada[posLastChar(entrada, '(') + len(command): len(entrada)]
            resultado = 0
            command = command[1: len(command) - 1]
            commands = command.split(' ')
            if len(commands) == 3:
                resultado = realizarOperacion(commands)
            elif len(commands) == 2:
                resultado = realizarFuncion(commands)
            entrada = strAux + str(resultado) + strAux2
            if resultado == 'A':
                error()
            else:
                analizarCommando(entrada)
        else:
             error('Espacios entre parentesis y argumentos')


#Interfaz con el usuario
def init():
    loop = 1
    while loop:
        command = input("calculaodra >> ").strip()
        if command == "":
            error()
            continue
        elif command == 'quit':
            print("Saliendo...")
            print("Gracias por usar calculadora.")
            break
        elif contiene(command, '('):
            if contar(command, '(') == contar(command, ')'):
                if espacios(command):
                   analizarCommando(command)
                else:
                    error('existen espacios de más, o faltan espacios')
            else:
                error('Faltan parentesis')
            continue
        elif esNumero(command) != 'False':
            analizarCommando(command)
            continue
        else:
            error()
init()

