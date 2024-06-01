def suma(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):

    try:
        return a/b 
    except ZeroDivisionError:
        return f'Error,{ZeroDivisionError}'

def res(a,b):
    return a-b


while(True):
    try:
        op = int(input("""
        Elija una opcion:
            1. suma
            2. resta
            3.division
            4.multuplicacion
            5. salir
        """))
        if op == 5:
            break
        else:
            a = int(input('Ingrese el primer valor: '))
            b = int(input('Ingrese el segudno valor: '))
            if op == 1:
                print(f'resultado = {suma(a,b)}')
            elif op == 2:
                print(f'resultado = {res(a,b)}')
            elif op == 3:
                print(f'resultado = {div(a,b)}')
            elif op == 4:
                print(f'resultado = {mul(a,b)}')
    except ValueError:
        print(f'Valor ingresado no valido {ValueError}')
    finally:
        print('Operacion Terminada')
    

    
