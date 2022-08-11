"""
Ejercicio nivel 2: Agenda de peliculas.
Modulo de interacci0n por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2
"""
import modulo_peliculas as mod


def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    print("Nombre: " + nombre + " - Anio: " + str(anio) +
          " - Duracion: " + str(duracion) + "  mins")
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)

    if (hora//100 < 10):
        hora_formato = "0" + str(hora//100)
    else:
        hora_formato = str(hora//100)

    if (hora % 100 < 10):
        min_formato = "0" + str(hora % 100)
    else:
        min_formato = str(hora % 100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)


def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    print('La pelicula más larga es: ', pelicula_mas_larga)


def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    duracion_promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("\nLa duración promedio de las peliculas es de: \n", duracion_promedio)


def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    anio = int(
        input("Ingrese el año de estreno las peliculas que quiera buscar: "))
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    print("\nLas peliculas a estrenarse son: ", estrenos)


def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    peliculas_mayores_de_dieciocho = mod.cuantas_peliculas_18_mas(
        p1, p2, p3, p4, p5)

    print("Las peliculas para mayores de 18 años son: ",
          peliculas_mayores_de_dieciocho)


def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de reagendar una pelicula
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Reagendar una pelicula de la agenda")

    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    nueva_hora = int(input("\nIngrese una nueva hora: "))
    nuevo_dia = input("\nIngrese un nuevo día: ")
    respuesta = input(
        "\nDesea establecer un control de horario: \n🕣 Ingrese (y) si desea establecer un control de horario\n🕣 Ingrese (n) si no desea establecer un control de horario \n")
    control_horario = respuesta.lower() == 'y'
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)
    reagendado = False
    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        reagendado = mod.reagendar_pelicula(pelicula, nueva_hora,
                                            nuevo_dia, control_horario, p1, p2, p3, p4, p5)

    if (reagendado):
        print("La pelicula fue reagendada con exito")
    else:
        print("La pelicula no pudo ser reagendada")


def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula o no.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Decidir si se puede invitar a alguien a ver una pelicula")

    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    # TODO: Completar


def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    pelicula1 = mod.crear_pelicula(
        "Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula(
        "Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")
    pelicula3 = mod.crear_pelicula(
        "Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula(
        "Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula(
        "The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")

    ejecutando = True
    while ejecutando:
        print("\n\nMi agenda de peliculas para la semana de receso" + "\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)

        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)

        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)

        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)

        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5)
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5)
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")

    return continuar_ejecutando


iniciar_aplicacion()
