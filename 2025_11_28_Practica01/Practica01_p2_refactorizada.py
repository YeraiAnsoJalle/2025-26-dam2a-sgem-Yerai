MENSAJE_FILTRAR = "Desea filtrar por calificacion (S/N) (Una opcion no valida mostrara todo)"
MENSAJE_INTRODUCIR_VALORES = "Introduce uno de los siguientes valores"
MENSAJE_OPCIONES = '"Sobresaliente", "Notable", "Bien", "Suficiente", "Necesita mejorar", "Mostrar todo"'
MENSAJE_NO_VALIDO = "No valido. Valores validos: "
OPCIONES_VALIDAS = ["Sobresaliente", "Notable", "Bien", "Suficiente", "Necesita mejorar", "Mostrar todo"]
OPCION_MOSTRAR_TODO = "Mostrar todo"

def crear_datos_alumnos():
    bruce = { 'nombre': 'Bruce Banner',
        'trabajos': [80, 50, 40, 20],
        'test' : [75, 75],
        'practicas' : [78.20, 77.20]
    }

    harry = {'nombre':'Harry Potter',
        'trabajos' : [82, 56, 44, 30],
        'test' : [80, 80],
        'practicas' : [67.90, 78.72]
    }

    hermione = {'nombre':'Hermione Ranger',
        'trabajos' : [95, 100, 100, 100],
        'test' : [99, 100],
        'practicas' : [95.0, 80.5]
    }

    peter = {'nombre':'Peter Parker',
        'trabajos' : [30, 10, 100, 100],
        'test' : [90, 10],
        'practicas' : [50.0, 50.0]
    }

    mario = {'nombre':'Super Mario',
        'trabajos' : [77, 82, 23, 39],
        'test' : [18, 60],
        'practicas' : [80.6, 59.3]
    }

    return [bruce, harry, hermione, peter, mario]


def calcular_media(notas):
    suma = 0
    for nota in notas:
        suma = suma + nota
    return suma / len(notas)


def calcular_nota_final(alumno):
    media_trabajos = calcular_media(alumno['trabajos'])
    media_test = calcular_media(alumno['test'])
    media_practicas = calcular_media(alumno['practicas'])
    
    nota_final = (media_trabajos * 0.10) + (media_test * 0.50) + (media_practicas * 0.40)
    return nota_final


def obtener_calificacion(nota_final):
    if nota_final >= 90:
        return "Sobresaliente"
    elif nota_final >= 70:
        return "Notable"
    elif nota_final >= 60:
        return "Bien"
    elif nota_final >= 50:
        return "Suficiente"
    else:
        return "Necesita mejorar"


def obtener_filtro():
    filtrar = input(MENSAJE_FILTRAR)
    
    filtro = OPCION_MOSTRAR_TODO
    if filtrar == "S" or filtrar == "s":
        print(MENSAJE_INTRODUCIR_VALORES)
        filtro = input(MENSAJE_OPCIONES)

        valido = False
        while not valido:
            if filtro in OPCIONES_VALIDAS:
                valido = True
            else:
                print(MENSAJE_NO_VALIDO)
                filtro = input(MENSAJE_OPCIONES)
    
    return filtro


def mostrar_resultado_alumno(alumno, nota_final, calificacion):
    print(alumno['nombre'])
    print("====================================")
    print(f"Nota media final para {alumno['nombre']}: {round(nota_final,2)}")
    print(f"Calificacion final de {alumno['nombre']}: {calificacion}")


def procesar_alumnos(alumnos, filtro):
    for alumno in alumnos:
        nota_final = calcular_nota_final(alumno)
        calificacion = obtener_calificacion(nota_final)
        
        if filtro == OPCION_MOSTRAR_TODO:
            mostrar_resultado_alumno(alumno, nota_final, calificacion)
        else:
            if calificacion == filtro:
                mostrar_resultado_alumno(alumno, nota_final, calificacion)


def main():
    alumnos = crear_datos_alumnos()
    filtro = obtener_filtro()
    procesar_alumnos(alumnos, filtro)