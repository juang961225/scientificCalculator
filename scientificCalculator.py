# crear una calculadora cientifica que vaya dentro de un while y tenga las cuatro operaciones basicas (+.-,/,*) y las trigonometricas de cualquier numero (sen,cos,tan) tambien radicacion y potenciacion
# variables
import math
arrayNumber = []
#funcion de dato de entrada para las operaciones
def askNumber():
    ask = float(input('ingrese por favor un número para operar: '))
    return ask

def askOperation():
    ask = input('por favor ingrese la operacion deseada  \n "+" si es para suma \n "-" si es para resta \n "*" si es para multiplicacion \n "/" si es para division \n "sen" si es para seno \n "cos" si es para coseno \n "tan" si es para tangente \n "^" si es para potenciacion \n "RAIZ" si es para raiz cuadrada \n : ')
    return ask
#@param:values es el valor con el que se realizara dicha operacion 
#funcion para realizar sumas
def askSum(value1, value2):
    number1 = valueTry(value1)
    number2 = valueTry(value2)
    result = number1 + number2
    return result
#@param:values es el valor con el que se realizara dicha operacion
#funcion par realizar restas
def askSubtraction(value1, value2):
    number1 = valueTry(value1)
    number2 = valueTry(value2)
    result = number1 - number2
    return result
#@param:values es el valor con el que se realizara dicha operacion
#funcion para realizar multiplicacion
def askMultiply(value1, value2):
    number1 = valueTry(value1)
    number2 = valueTry(value2)
    result = number1 * number2
    return result
#@param:values es el valor con el que se realizara dicha operacion
#funcion para realizar divisiones
def askDividir(value1, value2):
    number1 = valueTry(value1)
    number2 = valueTry(value2)
    result = number1 / number2
    return result
#@param:values es el valor con el que se realizara dicha operacion
#funcion para realizar operaciones de potenciacion
def askEnhancement(value1, value2):
    number1 = valueTry(value1)
    number2 = valueTry(value2)
    result = number1 ** number2
    return result
#@param:values es el valor con el que se realizara dicha operacion
#funcion para realizar operaciones de radicacion
def askRoot(value1):
    number1 = valueTry(value1)
    result = number1 ** 0.5
    return result
#@param:values es el valor con el que se realizara dicha operacion
#funcion para realizar operaciones trigonometrica del seno
def askSen(value1):
    number1 = valueTry(value1)
    radians = math.radians(number1)
    result = math.sin(radians)
    return result
#@param:values es el valor con el que se realizara dicha operacion
#funcion para realizar operaciones trigonometrica del coseno
def askCos(value1):
    number1 = valueTry(value1)
    radians = math.radians(number1)
    result = math.cos(radians)
    return result
#@param:values es el valor con el que se realizara dicha operacion
#funcion para realizar operaciones trigonometrica de la tangente
def askTan(value1):
    number1 = valueTry(value1)
    radians = math.radians(number1)
    result = math.tan(radians)
    return result
#esta funcion realiza el dato de entrada para saber si el usuario desea continuar operando 
def askDecition():
    answer = input('desea realizar otra operacion Y/N: ')
    return answer
#esta funcion permite evaluar la operacion de usuario para continiar con el programa o finalizarlo
def askAnswer(ask):
    if ask == 'y' or ask == 'Y':
        return True
    else:
        return False

#esta funcion realiza la validacion si es un nùmero o no
def valueTry(number):
    try:
        if float == number:
            valueNumber = float(number)
            return valueNumber
        elif int == number:
            valueNumber = int(number)
            return valueNumber
    except ValueError:
        print("por favor ingrese un número para continuar con la operacion")
        return None


def askWhile():
    condition = True
    while condition:
        # parte principal
        arrayNumber.append(askNumber())
        ope = askOperation()
        #operacione suma
        if ope == '+':
            arrayNumber.append(askNumber())
            value = askSum(arrayNumber[0],arrayNumber[1])
            print('el valor de la suma',arrayNumber[0],' + ', arrayNumber[1],' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)

        #operacion resta
        elif ope == '-':
            arrayNumber.append(askNumber())
            value = askSubtraction(arrayNumber[0], arrayNumber[1])
            print('el valor de la resta',arrayNumber[0],' - ', arrayNumber[1],' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)
        #operacion multi
        elif ope == '*':
            arrayNumber.append(askNumber())
            value = askMultiply(arrayNumber[0], arrayNumber[1])
            print('el valor de la multiplicación',arrayNumber[0],' * ', arrayNumber[1],' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)

        elif ope == '/':
            arrayNumber.append(askNumber())
            value = askDividir(arrayNumber[0], arrayNumber[1])
            print('el valor de la división',arrayNumber[0],' / ', arrayNumber[1],' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)

        elif ope == '^':
            print('coloque el valor al cual desea elevar el dato ya ingresado')
            arrayNumber.append(askNumber())
            value = askEnhancement(arrayNumber[0], arrayNumber[1])
            print('el valor de',arrayNumber[0],' a la ^ ', arrayNumber[1],' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)

        elif ope == 'RAIZ' or ope == 'raiz' or ope == 'Raiz':
            value = askRoot(arrayNumber[0])
            print('el valor de la raiz cuadrada de',arrayNumber[0],' es ',' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)

        elif ope == 'sen' or ope == 'SEN' or ope == 'Sen':
            value = askSen(arrayNumber[0])
            print('el valor del seno de',arrayNumber[0],' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)

        elif ope == 'cos' or ope == 'COS' or ope == 'Cos':
            value = askCos(arrayNumber[0])
            print('el valor del coseno de',arrayNumber[0],' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)

        elif ope == 'tan' or ope == 'Tan' or ope == 'TAN':
            value = askCos(arrayNumber[0])
            print('el valor de la tangente de',arrayNumber[0],' = ' ,value)
            answer = askDecition()
            condition = askAnswer(answer)

        else:
            print('por favor ingrese una de las operaciones sugeridas por el programa')
            condition = True

askWhile()