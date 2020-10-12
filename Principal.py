from Datos import *

op=0
ln=1
i=1
nombre = []
estados = []
alfabeto = []
estadoAceptacion = []
Transicioness = []
lista_automatas = []
lineas=''
linea_spliteada=''
lista_cursos=''
linea=''

def opcionErronea(op, limI, limS):
    if limI > op or op > limS:
        print("\nSu opcion esta fuera de los parametros, intente ingresar una opcion correcta\n")
    else:
        print("Opcion valida\n")

def infoDess():
    print('\n*-*-*-*-*-*-*-*-*-*-Lenguajes Formales de Programacion Seccion E*-*-*-*-*-*-*-*-*-*-\n'
          '*-*-*-*-*-*-*-*-*-*-           201905554                        *-*-*-*-*-*-*-*-*-*-\n'
          '*-*-*-*-*-*-*-*-*-*-     Marvin Eduardo Catalan Veliz           *-*-*-*-*-*-*-*-*-*-')
    input("\nPresione enter para continuar:")

infoDess()



def cargarArchivoAFD():
    global linea,lineas,linea_spliteada,lista_cursos,ln
    global nombre,estados,alfabeto,estadoAceptacion,Transicioness,lista_automatas
    NombreAE = input('Escriba la ruta o el Nombre del archivo afd, debe de ingresar un nombre de la siguiente manera(ejemplo.afd): \n')
    archivoafd = open(NombreAE, 'r',encoding='UTF-8')
    ln = 1
    Transicioness = []
    for linea in archivoafd:
        linea = linea.rstrip("\n")
        if linea == "%":
            lista_automatas.append(datosAFD(nom,estados, alfabeto, estadoInicial, estadoAceptacion, Transicioness))
            Transicioness=[]
            ln = 0
        if ln == 1:
            nom = linea.rstrip("\n")
            nombre.append(nom)
        if ln == 2:
            estados = linea.split(",")
        if ln == 3:
            alfabeto = linea.split(",")
        if ln == 4:
            estadoInicial = linea
        if ln == 5:
            estadoAceptacion = linea.split(",")
        if ln >= 6 and linea != "%":
            inicio = linea.split(",")
            caracter_final = inicio[1].split(";")
            Transicioness.append(transiciones(inicio[0], caracter_final[0], caracter_final[1]))

        ln += 1

    for lA in lista_automatas:
        print(lA.nombre)
        print(lA.estados)
        print(lA.alfabeto)
        print(lA.EstadoInicial)
        print(lA.EstadoAceptacion)
        for tr in lA.Transicioness:
            print("Inicio: " + tr.inicio + " Caracter: " + tr.dato + "final: " + tr.final)
    moduloAfd()

def crearAFD():
    global i
    #global Datos

    nameAFD = input('Por favor digite nombre del nuevo AFD\n ')

    for Datos in lista_automatas:

        if(Datos.nombre == nameAFD):
            print('Este automata ya existe, ponele otro nombre\n')
        else:
            i=i+1
        if (i >= len(lista_automatas)):
            print('Nombre agregado Correctamente\n')

    nestadosAFD = int(input('Ingrese el numero de estados del AFD\n'))

    cadenaestados=''
    listaaux=[]

    while i<=nestadosAFD:
        contadorAuxiliar = 0
        estadosAFD = input('Por favor ingrese el estado número '+str(i)+': ')
        if estadosAFD in listaaux:
            print('El estado ya existe, digite otro porfavor\n')
            i=i
            contadorAuxiliar+=1
        elif(contadorAuxiliar==0):
            if(i < nestadosAFD):
                cadenaestados = cadenaestados + estadosAFD + ','
                listaaux.append(estadosAFD)
                i=i+1
            elif(i == nestadosAFD):
                cadenaestados = cadenaestados + estadosAFD
                listaaux.append(estadosAFD)
                i =i+1
    nalfabetoAFD = int(input('Ingrese el numero de simbolos para el alfabeto del AFD \n'))

    cadenaalfabeto = ''
    listaaux1 = []

    i=1
    while i <= nalfabetoAFD:
        contadorAuxiliar = 0
        alfabetoAFD = input('Por favor ingrese el simbolo del alfabeto numero ' + str(i) + ': ')
        if alfabetoAFD in listaaux:
            print('\nEl simbolo que intentas agregar al alfabeto ya existe en los estados, escribe uno de nuevo\n')
            i = i
            contadorAuxiliar += 1
        if alfabetoAFD in listaaux1:
            print('El simbolo que intentas agregar al alfabeto ya existe, escribe uno nuevo\n')
            i = i
            contadorAuxiliar += 1
        elif (contadorAuxiliar == 0):
            if (i < nalfabetoAFD):
                cadenaalfabeto = cadenaalfabeto + alfabetoAFD + ','
                listaaux1.append(alfabetoAFD)
                i = i + 1
            elif (i == nalfabetoAFD):
                cadenaalfabeto = cadenaalfabeto + alfabetoAFD
                listaaux1.append(alfabetoAFD)
                i = i + 1
    cadenaestadoInicial=''

    cn=0
    while cn<=0:
        estadoInicialAFD = input('Por favor ingrese el estado inicial  ')
        if estadoInicialAFD in listaaux:
            cadenaestadoInicial=estadoInicialAFD
            cn=cn+1
        else:
            cn=0
            print('\nEl estado digitado no se encuentra dentro de sus estados, por favor ingrese uno que si este\n')

    cadenaTransiciones = ''
    listaaux2 = []
    cn=0
    while cn<=0:
        global inicio,caracter_final
        transiciones1 = input('\nPor favor ingrese transiciones de la siguiente forma\nEstado origen, simbolo entrada, Estado destino\nNOTA** cuando'
                              'desee dejar de agregar transiciones en vez de la transicion escriba FIN en mayusculas\n')

        if(transiciones1!='FIN'):
            print('que hago aqui')
            inicio = transiciones1.split(",")
            caracter_final = inicio[1].split(";")
            if inicio in listaaux and caracter_final[0] in listaaux1 and caracter_final[1] in listaaux:
                cadenaTransiciones = inicio[0]+','+caracter_final[0]+','+caracter_final[1] + "\n"
                listaaux2.append(inicio[0]+','+caracter_final[0]+','+caracter_final[1])
                cn=0
        elif(transiciones1=='FIN' or transiciones1=='Fin' or transiciones1=='FIn' or transiciones1=='fin' or transiciones1=='fIN'or transiciones1=='fIn'):
            cn=1
            moduloAfd()



    print(nameAFD)
    print(cadenaestados)
    print(listaaux)
    print(cadenaalfabeto)
    print(listaaux1)
    print(cadenaestadoInicial)
    print(cadenaTransiciones)






def moduloAfd():
    global op
    op = 0
    # Menu principal y validacion de seleccion de opcion
    while op < 1 or op > 7:
        print('\n*-*-*-*-*-*-*-*-*-*-        MODULO AFD          *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-1)Crear AFD                   *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-2)Cargar archivo              *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-3)Evaluar cadena              *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-4)Guardar AFD en archivo      *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-5)Generar reporte AFD         *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-6)Generar gramatica regular   *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-7)Regrear a menu principal    *-*-*-*-*-*-*-*-*-*-\n')
        op = int(input('Seleccione la opcion deseada: '))
        opcionErronea(op, 1, 7)
        if op is 1:
            crearAFD()
        elif op is 2:
            cargarArchivoAFD()
        elif op is 3:
            print('holahola')
        elif op is 4:
            print('adios')
        elif op is 5:
            print('holahola')
        elif op is 6:
            print('holahola')
        elif op is 7:
            menuPrincipal()

def moduloGR():
    global op
    op = 0
    # Menu principal y validacion de seleccion de opcion
    while op < 1 or op > 7:
        print('\n*-*-*-*-*-*-*-*-*-*-         MODULO GRAMATICAS REGULARES      *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-1)Crear gramatica                            *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-2)Cargar archivo de entrada                  *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-3)Evaluar cadenas                            *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-4)Eliminar recursividad por la izquierda     *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-5)Guardar AFD en arcivo                      *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-6)Generar reporte gramatica regular          *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-7)Regrear a menu principal                   *-*-*-*-*-*-*-*-*-*-\n')
        op = int(input('Seleccione la opcion deseada: '))
        opcionErronea(op, 1, 7)
        if op is 1:
            print('hola')
        elif op is 2:
            print('adios')
        elif op is 3:
            print('holahola')
        elif op is 4:
            print('adios')
        elif op is 5:
            print('holahola')
        elif op is 6:
            print('holahola')
        elif op is 7:
            menuPrincipal()

def menuPrincipal():
    global op
    op=0
    # Menu principal y validacion de seleccion de opcion
    while op < 1 or op > 3:
        print('\n*-*-*-*-*-*-*-*-*-*-        MENU PRINCIPAL         *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-1)Modulo AFD                     *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-2)Modulo de gramaticas regulares *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-3)Acerca de                      *-*-*-*-*-*-*-*-*-*-\n')
        op = int(input('Seleccione la opcion deseada: '))
        opcionErronea(op, 1, 3)
        if op is 1:
            moduloAfd()
        elif op is 2:
            moduloGR()
        elif op is 3:
            print('holahola')

menuPrincipal()
