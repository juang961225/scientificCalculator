# crear una calculadora cientifica que vaya dentro de un while y tenga las cuatro operaciones basicas (+.-,/,*) y las trigonometricas de cualquier numero (sen,cos,tan) tambien radicacion y potenciacion
import math
condition = True
arrayNumber = []

def askNumber():
    ask = float(input('ingrese por favor un número para operar: '))
    return ask

def askOperation():
    ask = input('por favor ingrese la operacion deseada  \n "+" si es para suma \n "-" si es para resta \n "*" si es para multiplicacion \n "/" si es para division \n "sen" si es para seno \n "cos" si es para coseno \n "tan" si es para tangente \n "^" si es para potenciacion \n "RAIZ" si es para raiz cuadrada \n : ')
    return ask

def askSum(values):
    result = values[0] + values[1]
    return result

def askSubtraction(values):
    result = values[0] - values[1]
    return result

def askMultiply(values):
    result = values[0] * values[1]
    return result

def askDividir(values):
    result = values[0] / values[1]
    return result

def askExponent(values):
    result = values[0] ** values[1]
    return result

def askRoot(values):
    result = values[0] ** 0.5
    return result

def askSen(values):
    radians = math.radians(values[0])
    result = math.sin(radians)
    return result

def askCos(values):
    radians = math.radians(values[0])
    result = math.cos(radians)
    return result

def askTan(values):
    radians = math.radians(values[0])
    result = math.tan(radians)
    return result

def askWhile():
    while condition:
        # parte principal
        arrayNumber.append(askNumber())
        ope = askOperation()
        #operacione suma
        if ope == '+':
            arrayNumber.append(askNumber())
            value = askSum(arrayNumber)
            print('el valor de la suma',arrayNumber[0],' + ', arrayNumber[1],' = ' ,value)
            condition = False
        #operacion resta
        elif ope == '-':
            arrayNumber.append(askNumber())
            value = askSubtraction(arrayNumber)
            print('el valor de la resta',arrayNumber[0],' - ', arrayNumber[1],' = ' ,value)
        #operacion multi
        elif ope == '*':
            arrayNumber.append(askNumber())
            value = askMultiply(arrayNumber)
            print('el valor de la multiplicación',arrayNumber[0],' * ', arrayNumber[1],' = ' ,value)

        elif ope == '/':
            arrayNumber.append(askNumber())
            value = askDividir(arrayNumber)
            print('el valor de la división',arrayNumber[0],' / ', arrayNumber[1],' = ' ,value)

        elif ope == '^':
            print('coloque el valor al cual desea elevar el dato ya ingresado')
            arrayNumber.append(askNumber())
            value = askExponent(arrayNumber)
            print('el valor de',arrayNumber[0],' a la ^ ', arrayNumber[1],' = ' ,value)

        elif ope == 'RAIZ':
            value = askRoot(arrayNumber)
            print('el valor de la raiz cuadrada de',arrayNumber[0],' es ',' = ' ,value)

        elif ope == 'raiz':
            value = askRoot(arrayNumber)
            print('el valor de la raiz cuadrada de',arrayNumber[0],' es ',' = ' ,value)

        elif ope == 'Raiz':
            value = askRoot(arrayNumber)
            print('el valor de la raiz cuadrada de',arrayNumber[0],' es ',' = ' ,value)

        elif ope == 'sen':
            value = askSen(arrayNumber)
            print('el valor del seno de',arrayNumber[0],' = ' ,value)

        elif ope == 'SEN':
            value = askSen(arrayNumber)
            print('el valor del seno de',arrayNumber[0],' = ' ,value)

        elif ope == 'Sen':
            value = askSen(arrayNumber)
            print('el valor del seno de',arrayNumber[0],' = ' ,value)

        elif ope == 'cos':
            value = askCos(arrayNumber)
            print('el valor del coseno de',arrayNumber[0],' = ' ,value)

        elif ope == 'COS':
            value = askCos(arrayNumber)
            print('el valor del coseno de',arrayNumber[0],' = ' ,value)

        elif ope == 'Cos':
            value = askCos(arrayNumber)
            print('el valor del coseno de',arrayNumber[0],' = ' ,value)

        elif ope == 'tan':
            value = askCos(arrayNumber)
            print('el valor de la tangente de',arrayNumber[0],' = ' ,value)

        elif ope == 'Tan':
            value = askCos(arrayNumber)
            print('el valor de la tangente de',arrayNumber[0],' = ' ,value)

        elif ope == 'TAN':
            value = askCos(arrayNumber)
            print('el valor de la tangente de',arrayNumber[0],' = ' ,value)

        else:
            print('por favor ingrese una de las operaciones sugeridas por el programa')
            condition = True

askWhile()