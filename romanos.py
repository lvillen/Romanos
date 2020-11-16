simbolos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
tipo_5 =('V', 'L', 'D')
tipo_1 =('I', 'X', 'C', 'M')


#En dos funciones

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"Símbolo {simbolo} no permitido.")
    else: 
        raise ValueError(f"Parámetro {simbolo} debe ser un string.")

def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"Parámetro {romano} debe ser un string.")
    
    suma = 0
    c_repes = 0
    valor_anterior = ""

    for letra in romano:
        if letra == valor_anterior and letra in tipo_5:
            raise OverflowError(f'Demasiados tipos de {letra}.')
        if letra == valor_anterior:
            c_repes += 1
            if c_repes > 2:
                raise OverflowError(f"Demasiados símbolos de tipo {letra}.")    

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra
    
    return suma



'''
EN UNA FUNCIÓN TODA LA OPERACIÓN

def romano_a_entero(romano):
    suma = 0

    if not isinstance(romano, str):
        raise ValueError(f"Parámetro {romano} debe ser un string.")

    for letra in romano:    
        if isinstance(letra, str) and letra.upper() in simbolos:
            suma = suma + simbolos[letra.upper()]
        elif isinstance(letra, str):
            raise ValueError(f"Símbolo {letra} no permitido.")
        else: 
            raise ValueError(f"Parámetro {letra} debe ser un string.")
    
    return suma
'''