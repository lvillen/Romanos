simbolos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
tipo_5 =('V', 'L', 'D')
restas = ('CM', 'CD', 'XC', 'XL', 'IX', 'IV')

#DE ROMANO A ENTERO
def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"Símbolo {simbolo} no permitido.")
    else: 
        raise ValueError(f"Parámetro {simbolo} debe ser un string.")

def orden_magnitud(caracter):
    valor = simbolo_a_entero(caracter)
    return len(str(valor))

def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"Parámetro {romano} debe ser un string.")
    
    suma = 0
    c_repes = 0
    valor_anterior = ""
    orden_magnitud_global = 0
    orden_magnitud_letra = 0
    ha_habido_resta = False

    for letra in romano:
        orden_magnitud_letra = orden_magnitud(letra)
        if letra == valor_anterior:
            orden_magnitud_global = orden_magnitud_letra
            if letra in tipo_5:
                raise ValueError("No es romano")
            elif c_repes >= 2:
                raise ValueError("Demasiadas repeticiones")
            elif ha_habido_resta:
                raise ValueError("Demasiadas restas")
            c_repes += 1
        elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior):
            if valor_anterior + letra not in restas:
                raise ValueError("Resta no permitida")
            elif c_repes > 0:
                raise ValueError("Resta tras repetición no permitida")
            elif ha_habido_resta:

                raise ValueError("Demasiadas restas")
            ha_habido_resta = True
            suma -= 2 * simbolo_a_entero(valor_anterior)
            c_repes = 0
        else:    
            if orden_magnitud_global > orden_magnitud_letra:
                ha_habido_resta = False
            if ha_habido_resta:
                raise ValueError("Demasiadas restas")

            orden_magnitud_global = orden_magnitud_letra
            c_repes = 0

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra
    return suma

#DE ENTERO A ROMANO
def descomponer(numero):
    # vvv return[int(d) for d in str(numero)] | ESTA OPERACIÓN ES LA MISMA QUE AQUÍ ABAJO, CON LISTCOMPREHENSION
    if not isinstance(numero, int):
        raise SyntaxError(f'{numero} no es un número natural.')

    l = []
    for d in str(numero):
        l.append(int(d))
    return l

'''
Versión de descomponer con potencias y proceso matemático, sin convertir el número a 'str'
def descomponer(numero):
    l = []
    for pot in (1000, 100, 10):
        l.append(numero//pot) # // == división entera
        numero %= pot
    l.append(numero)
    return l
'''
unidades = ('I', 'V', 'X')
decenas = ('X', 'L', 'C')
centenas = ('C', 'D', 'M')
millares = ('M')

lista_ordenes = [unidades, decenas, centenas, millares]

def numero_a_romano(numero):
    if numero > 3999 or numero <1:
        raise OverflowError('Debe estar entre 1 y 3999')
    
def convertir(ordenes_magnitud):
    contador = 0
    for orden in ordenes_magnitud[::-1]:
        procesar_simbolo(orden, lista_ordenes[contador])
        contar += 1

def procesar_simbolo(s, clave):
'''    
    #Caso 1
    return clave[s]
    #Caso 2
    return clave[s-1]
'''

    #Caso 3 'Mon'
    if s == 9:
        return clave[0] + clave[2]
    elif s >= 5:
        return clave[1] + clave[0] * s-5 #clave = elemento de las tuplas que tenemos arriba | Revisar esta operación matemática 
    elif s == 4:
        return clave[0] + clave[1]
    else:
        return clave[0] * s




