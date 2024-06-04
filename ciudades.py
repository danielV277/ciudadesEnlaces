#diccionario donde se van a guardar las ciudades como clave, y su valor sera otro diccionario
#donde cada clave sera el nombre de la ciudad con la que tiene enlace y su valor sera el valor del enlace 
ciudades = {}

#funcion para crear un tipo de respuesta, recibe un estado y un mensaje
def crearRespuesta(estado,mensaje):
    respuesta = {'estado':bool,'mensaje':str}
    respuesta['estado'] = estado
    respuesta['mensaje'] = mensaje
    return respuesta

#agrega una ciudad a las ciudades con el nombre si este no existe ya  
def agregarCiudad(nombreNuevo):
    if type(nombreNuevo) == str: 
        if  nombreNuevo not in ciudades.keys():
            ciudades[f'{nombreNuevo}'] = {}
            return crearRespuesta(True,'Ciudad Agregada con exito')
        else:
            return crearRespuesta(False, 'No agregada, el nombre de la ciudad ya existe')
    else:
        return crearRespuesta(False,'Nombre no valido')

#estable un relacion entre dos ciudades si estas existen
def agregarEnlace(ciudad1,ciudad2,distancia):
    if ciudad1 not in ciudades.keys():
        return crearRespuesta(False,f'ciudad {ciudad1} no existe')
    elif ciudad2 not in ciudades.keys():
        return crearRespuesta(False,f'ciudad {ciudad2} no existe')
    else:
        ciudades[ciudad1][ciudad2] = distancia
        ciudades[ciudad2][ciudad1] = distancia
        return crearRespuesta(True,'Ciudades enlazadas con exito')

#elimina una ciudad y todos los enlaces que este tenga
def eliminarCiudad(nombre):
    if nombre not in ciudades.keys():
        return crearRespuesta(False,'Ciudad no existe')
    else:
        for key in ciudades.keys():
            if nombre in ciudades[key].keys():
                del(ciudades[key][nombre])
        del(ciudades[nombre])
        return crearRespuesta(True,'Ciudad eliminada con exito')

#eliminar un enlace entre dos ciudades siempre que este exista
def eliminarEnlace(ciudad1,ciudad2):
    try:
        del(ciudades[ciudad1][ciudad2])
        del(ciudades[ciudad2][ciudad1])
        return crearRespuesta(True,'Enlaze elimonado con exito')
    except:
        return crearRespuesta(False,'El enlaze no existe')

#verifica si una relacion existe, si este exite retonar un objeto 
#con un estado de True y la distancia 
def existeEnlace(ciudad1,ciudad2):
    if ciudad1 in ciudades[ciudad2].keys():
        return crearRespuesta(True,ciudades[ciudad1][ciudad2]) 
    else:
        return crearRespuesta(False,'Enlace no existe')
    
#retorna todos los enlaces de una ciudad
def obtenerEnlaces(nombre):
    try:
        return ciudades[nombre]
    except:
        return False 

#retornar el diccionario donde se muestra cada ciudad y las ciudades con quienes tiene
#una carretera con el respectivo valor de esta
def obtenerCarreteras():
    return ciudades

def menor(vector):
    menor = float('inf')
    indice = -1
    for i,ele in enumerate(vector):
        if ele != 0 and ele < menor:
            menor = ele
            indice = i
    
    
    return {'indice':indice,'valor':menor}
         

def caminoMasCorto(ciudad1,ciudad2):
    tabla = [list(ciudades.keys()),[float('inf') for ciudad in ciudades.keys()],[float('inf') for ciudad in ciudades.keys()]]
    tabla[1][tabla[0].index(ciudad1)] = 0
    tabla[2][tabla[0].index(ciudad1)] = 0
    
    for subKey in ciudades[ciudad1].keys():
        indice = tabla[0].index(subKey)
        tabla[2][indice] = ciudades[ciudad1][subKey]   
            
    men = menor(tabla[2])
    
    while men['indice'] != -1:
        tabla[1][men['indice']] = men['valor']
        tabla[2][men['indice']] = 0 
        
        ciudad = tabla[0][men['indice']]
        print(f'Estoy en la ciudad {ciudad}')
        print(tabla)
        for subKey in ciudades[ciudad].keys():
            unionCarreteras = men['valor'] + ciudades[ciudad][subKey]
            indiceSubKey = tabla[0].index(subKey)
            
            if unionCarreteras < tabla[2][indiceSubKey]:
                print('hice un cambio')
                tabla[2][indiceSubKey] = unionCarreteras
                print(tabla)
                
        men = menor(tabla[2])
        
    return tabla
    

agregarCiudad('A')
agregarCiudad('B')
agregarCiudad('C')
agregarCiudad('D')
agregarCiudad('E')
agregarCiudad('F')
agregarEnlace('A','B',3)
agregarEnlace('B','C',9)
agregarEnlace('A','C',4)
agregarEnlace('A','D',5)
agregarEnlace('C','E',6)
agregarEnlace('C','F',9)

print(ciudades)
print(caminoMasCorto('C','B'))

