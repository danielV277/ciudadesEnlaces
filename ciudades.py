ciudades = {}
def crearRespuesta(estado,mensaje):
    respuesta = {'estado':bool,'mensaje':str}
    respuesta['estado'] = estado
    respuesta['mensaje'] = mensaje
    return respuesta

            
def agregarCiudad(nombreNuevo):
    if type(nombreNuevo) == str: 
        if  nombreNuevo not in ciudades.keys():
            ciudades[f'{nombreNuevo}'] = {}
            return crearRespuesta(True,'Ciudad Agregada con exito')
        else:
            return crearRespuesta(False, 'No agregada, el nombre de la ciudad ya existe')
    else:
        return crearRespuesta(False,'Nombre no valido')

def agregarEnlace(ciudad1,ciudad2,distancia):
    if ciudad1 not in ciudades.keys():
        return crearRespuesta(False,f'ciudad {ciudad1} no existe')
    elif ciudad2 not in ciudades.keys():
        return crearRespuesta(False,f'ciudad {ciudad2} no existe')
    else:
        ciudades[ciudad1][ciudad2] = distancia
        ciudades[ciudad2][ciudad1] = distancia
        return crearRespuesta(True,'Ciudades enlazadas con exito')

def eliminarCiudad(nombre):
    if nombre not in ciudades.keys():
        return crearRespuesta(False,'Ciudad no existe')
    else:
        for key in ciudades.keys():
            if nombre in ciudades[key].keys():
                del(ciudades[key][nombre])
        del(ciudades[nombre])
        return crearRespuesta(True,'Ciudad eliminada con exito')

def eliminarEnlace(ciudad1,ciudad2):
    try:
        del(ciudades[ciudad1][ciudad2])
        del(ciudades[ciudad2][ciudad1])
        return crearRespuesta(True,'Enlaze elimonado con exito')
    except:
        return crearRespuesta(False,'El enlaze no existe')


def existeEnlace(ciudad1,ciudad2):
    if ciudad1 in ciudades[ciudad2].keys():
        return crearRespuesta(True,ciudades[ciudad1][ciudad2]) 
    else:
        return crearRespuesta(False,'Enlace no existe')
    
def obtenerEnlaces(nombre):
    try:
        return ciudades[nombre]
    except:
        return False 


def mostrarCarreterras(cam = [], cams=[]):

    ciCopia = ciudades.copy()
    camino = cam
    caminos = cams
    for key in ciCopia.keys():
        camino.append(key)
        for subKey in ciCopia[key].keys():
            del(ciCopia[subKey][key])
    
    return ciCopia



agregarCiudad('A')
agregarCiudad('B')
agregarCiudad('C')
agregarCiudad('D')
agregarCiudad('E')
agregarEnlace('A','B',3)
agregarEnlace('B','C',9)
agregarEnlace('A','C',4)
agregarEnlace('A','D',5)
agregarEnlace('C','E',6)

print(ciudades)
print(mostrarCarreterras([],[]))

