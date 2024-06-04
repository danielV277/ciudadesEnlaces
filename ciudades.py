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
    elif distancia <= 0:
        return crearRespuesta(False,'No agregada, la distancia debe ser mayor a 0')
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
#con un estado de True, un mensaje y la distancia 
def existeEnlace(ciudad1,ciudad2):
    if ciudad1 in ciudades[ciudad2].keys():
        respuesta = crearRespuesta(True,'Carretera encontrada')
        respuesta['distancia'] = ciudades[ciudad1][ciudad2]
        return  
    else:
        return crearRespuesta(False,'Enlace no existe')
    
#retorna todos los enlaces de una ciudad si esta exite sino retorna false
def obtenerEnlaces(nombre):
    try:
        return ciudades[nombre]
    except:
        return False 

#retornar el diccionario donde se muestra cada ciudad y las ciudades con quienes tiene
#una carretera con el respectivo valor de esta
def obtenerCarreteras():
    return ciudades

#funcion creada para el algoritmo de  Dijkstra
def menor(vector):
    menor = float('inf')
    indice = -1
    for i,ele in enumerate(vector):
        #en la seleccion se exeptua el 0 ya se usa como una marca
        if ele != 0 and ele < menor:
            menor = ele
            indice = i
    
    #retonar un diccionario con el indice del menor valor y el valor
    return {'indice':indice,'valor':menor}
         

#fucnion creada para encontrar el camino mas corto usando el algoritmo de Dijkstra
def caminoMasCorto(ciudad1,ciudad2):
    #se verifica si las ciudades existen
    if ciudad1 not in ciudades.keys():
        return crearRespuesta(False,f'ciudad {ciudad1} no existe')
    elif ciudad2 not in ciudades.keys():
        return crearRespuesta(False,f'ciudad {ciudad2} no existe')
    
    #se genera un matriz con 3 columnas, la primera columna tendra el nombre de todas las ciudad la segunda tendra la ruta mas
    #corte desde ciudad1 hasta ciudad de al que le corresponda la fila, y la tercera se iterara para conseguir la ruta mas corta
    tabla = [list(ciudades.keys()),[float('inf') for ciudad in ciudades.keys()],[float('inf') for ciudad in ciudades.keys()]]
    tabla[1][tabla[0].index(ciudad1)] = 0
    tabla[2][tabla[0].index(ciudad1)] = 0

    #a la ciudad origen se le asigna el valorde 0 en las dos tablas
    for subKey in ciudades[ciudad1].keys():
        indice = tabla[0].index(subKey)
        tabla[2][indice] = ciudades[ciudad1][subKey]   
            
    #se usa la funcion menor para encontrar
    men = menor(tabla[2])

    #se genera la segunda columna de la tabla encontrada las menores rutas posibles de ciudad a ciudad
    while men['indice'] != -1:
        tabla[1][men['indice']] = men['valor']
        tabla[2][men['indice']] = 0 
        
        ciudad = tabla[0][men['indice']]
        for subKey in ciudades[ciudad].keys():
            unionCarreteras = men['valor'] + ciudades[ciudad][subKey]
            indiceSubKey = tabla[0].index(subKey)
            
            if unionCarreteras < tabla[2][indiceSubKey]:      
                tabla[2][indiceSubKey] = unionCarreteras
        men = menor(tabla[2])

    #de la tabla se obtine  el valor optimo minimo para llegar ala ciudad 2 y su indice
    indiceCiudadDestino = tabla[0].index(ciudad2)
    valorOptio = tabla[1][indiceCiudadDestino]

    #caminoOptimo contrendra la ruta
    caminoOptimo = [ciudad2]
    x = 0

    #se aplica el algoritmo para llegar de la ciudad2 a ciudad1 con el valorOptimo
    while x < len(caminoOptimo):
        for ciu in ciudades[caminoOptimo[x]].keys():
            if valorOptio - ciudades[caminoOptimo[x]][ciu] == tabla[1][tabla[0].index(ciu)]:
                valorOptio = valorOptio - ciudades[caminoOptimo[x]][ciu]
                caminoOptimo.append(ciu)
        
        x += 1
    
    #se invierte el caminoOptimo para que sea de la ciudad1 a ciudad2
    caminoOptimo = list(reversed(caminoOptimo))

    #se verifica si ciudad2 es acesible
    if ciudad1 not in caminoOptimo:
        return crearRespuesta(False,f'{ciudad2} es inaccessible a {ciudad1}')

    #se retonar un dict con un estado True, un mensaje, el vector caminoOptimo, y la distancia de este camino
    respuesta = crearRespuesta(True,'Camino encontrado')
    respuesta['camino'] = caminoOptimo
    respuesta['distancia'] = tabla[1][indiceCiudadDestino]
    return respuesta 
    

# PRUEBAS
# agregarCiudad('A')
# agregarCiudad('B')
# agregarCiudad('C')
# agregarCiudad('D')
# agregarCiudad('E')
# agregarCiudad('F')
# agregarEnlace('A','B',9)
# agregarEnlace('B','C',5)
# agregarEnlace('C','D',1)
# agregarEnlace('D','B',4)
# agregarEnlace('D','A',2)
# agregarEnlace('A','E',1)
# agregarEnlace('E','F',2)

# print(ciudades)
# print(caminoMasCorto('B','F'))

