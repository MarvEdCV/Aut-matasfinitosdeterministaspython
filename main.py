from Datos import *
from Datos1 import*
op=0
ln=1
ln1=1
nombre = []
nombre1=[]
estados = []
alfabeto = []
estadoAceptacion = []
Transicioness = []
lista_automatas = []
lista_gramaticas=[]
lineas=''
linea_spliteada=''
linea=''
lineas1=''
linea_spliteada1=''
linea1=''
nTerminales=[]
terminales=[]
Producciones=[]


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
    global linea,lineas,linea_spliteada,ln
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

    moduloAfd()

def cargarArchivoGR():
    global linea1, lineas1, linea_spliteada1, ln1
    global nombre1, estados, alfabeto, estadoAceptacion, Transicioness, lista_automatas
    NombreAE = input(
        'Escriba la ruta o el Nombre del archivo gre, debe de ingresar un nombre de la siguiente manera(ejemplo.gre): \n')
    archivoafd = open(NombreAE, 'r', encoding='UTF-8')
    ln1 = 1
    Producciones = []
    for linea1 in archivoafd:
        linea1 = linea1.rstrip("\n")
        if linea1 == "%":
            lista_automatas.append(datosAFD(nom, estados, alfabeto, estados[0], estadoAceptacion, Transicioness))
            lista_gramaticas.append(DatosGR(nam, nTerminales, terminales, nTerminalInicial,Producciones))
            Producciones = []
            Transicioness = []
            ln1 = 0
        if ln1 == 1:
            nam = linea1.rstrip("\n")
            nombre1.append(nam)
            nom = linea1.rstrip("\n")
            nombre.append(nom)
        if ln1 == 2:
            nTerminales = linea1.split(",")
            estados = linea1.split(",")
        if ln1 == 3:
            terminales = linea1.split(",")
            alfabeto = linea1.split(",")
        if ln1 == 4:
            nTerminalInicial = linea1
        if ln1 >= 5 and linea1 != "%":
            inicio = linea1.split(">")
            if inicio[1]!="$":
                caracter_final = inicio[1].split(" ")
                Producciones.append(producciones(inicio[0], inicio[1]))
                Transicioness.append(transiciones(inicio[0], caracter_final[0], caracter_final[1]))
            elif inicio[1]=="$":
                estadoAceptacion = inicio[0]
                Producciones.append(producciones(inicio[0], inicio[1]))
        ln1 += 1
    moduloGR()

def crearAFD():
    global i
    i=1
    x=0
    j=0
    global cadenaestados,cadenaalfabeto,cadenaestadoInicial,cadenaTransiciones
    #global Datos
    while x==0:
        j=0
        nameAFD = input('Por favor digite nombre del nuevo AFD\n ')
        for Datos in lista_automatas:
            if(Datos.nombre == nameAFD):
                print('Este automata ya existe, ponele otro nombre\n')
            else:
                j+=1
        if(j<len(lista_automatas)):
            x=0
        elif(j==len(lista_automatas)):
            x=1


    nestadosAFD = int(input('Ingrese el numero de estados del AFD\n'))

    cadenaestados=''
    listaaux=[]
    i=1
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

    x=0
    while x<=0:
        nestadosacepacionAFD = int(input('Ingrese el numero de estados de aceptacion \n'))
        if(nestadosacepacionAFD<=nestadosAFD):
            nestadosacepacionAFD=nestadosacepacionAFD
            x=1
        elif(nestadosacepacionAFD>nestadosAFD):
            print('Debes ingresar a lo sumo el mismo numero de estados para poder continuar.....')
            x=0

    cadenaestadoAceptacion = ''
    listaaux3 = []

    i = 1
    while i <= nestadosacepacionAFD:
        contadorAuxiliar=0
        estadoaceptacionAFD = input('Por favor ingrese el estado de aceptacion numero ' + str(i) + ': ')
        if(estadoaceptacionAFD not in listaaux3):
            if estadoaceptacionAFD in listaaux:
                contadorAuxiliar=0
            if estadoaceptacionAFD not in listaaux:
                print('El estado de aceptacion que intentas ingresar no pertenece a los estados agregados anteriormente\n')
                i = i
                contadorAuxiliar += 1
            if (contadorAuxiliar == 0):
                if (i < nestadosacepacionAFD):
                    cadenaestadoAceptacion=cadenaestadoAceptacion+estadoaceptacionAFD+","
                    listaaux3.append(estadoaceptacionAFD)
                    i = i + 1
                elif (i == nestadosacepacionAFD):
                    cadenaestadoAceptacion=cadenaestadoAceptacion+estadoaceptacionAFD
                    i = i + 1
                    listaaux3.append(estadoaceptacionAFD)
        elif(estadoaceptacionAFD in listaaux3):
            print('El estado de aceptacion que intentas agregar ya existe')
            i=i

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
            inicio = transiciones1.split(",")
            caracter_final = inicio[1].split(";")
            if inicio[0] in listaaux and caracter_final[0] in listaaux1 and caracter_final[1] in listaaux:
                inicio = transiciones1.split(",")
                caracter_final = inicio[1].split(";")
                Transicioness.append(transiciones(inicio[0], caracter_final[0], caracter_final[1]))
                cn=0
            else:
                print('Uno o mas datos agregados no se encontraron en lo ya guardado')
        elif(transiciones1=='FIN' or transiciones1=='Fin' or transiciones1=='FIn' or transiciones1=='fin' or transiciones1=='fIN'or transiciones1=='fIn'):
            cn=1
            lista_automatas.append(
                datosAFD(nameAFD, cadenaestados.split(","), cadenaalfabeto.split(","), cadenaestadoInicial,
                         cadenaestadoAceptacion.split(","), Transicioness))
            moduloAfd()

def crearGR():
    i = 1
    x = 0
    j = 0
    global cadenaNTerminales,cadenaTerminales, cadenaProducciones
    while x == 0:
        j = 0
        nameGR = input('Por favor digite nombre de la nueva Gramatica\n ')
        for Datos1 in lista_gramaticas:
            if (Datos1.nombre1 == nameGR):
                print('Esta gramática ya existe por favor escriba otro nombre\n')
            else:
                j += 1
        if (j < len(lista_gramaticas)):
            x = 0
        elif (j == len(lista_gramaticas)):
            x = 1

    nestadosAFD = int(input('Ingrese el numero no terminales de la gramática\n'))

    cadenaNTerminales = ''
    listaaux = []
    i = 1
    while i <= nestadosAFD:
        contadorAuxiliar = 0
        estadosAFD = input('Por favor ingrese el no terminal número ' + str(i) + ': ')
        if estadosAFD in listaaux:
            print('El no terminal ya existe, digite otro porfavor\n')
            i = i
            contadorAuxiliar += 1
        elif (contadorAuxiliar == 0):
            if (i < nestadosAFD):
                cadenaNTerminales = cadenaNTerminales + estadosAFD + ','
                listaaux.append(estadosAFD)
                i = i + 1
            elif (i == nestadosAFD):
                cadenaNTerminales = cadenaNTerminales + estadosAFD
                listaaux.append(estadosAFD)
                i = i + 1

    nalfabetoAFD = int(input('Ingrese el numero de Terminales \n'))
    cadenaTerminales = ''
    listaaux1 = []

    i = 1
    while i <= nalfabetoAFD:
        contadorAuxiliar = 0
        alfabetoAFD = input('Por favor ingrese el Terminal numero  ' + str(i) + ': ')
        if alfabetoAFD in listaaux:
            print('\nEl terminal que intentas agregar ya existe en los NO terminales, escribe uno de nuevo\n')
            i = i
            contadorAuxiliar += 1
        if alfabetoAFD in listaaux1:
            print('El terminal que intentas agregar  ya existe, escribe uno nuevo\n')
            i = i
            contadorAuxiliar += 1
        elif (contadorAuxiliar == 0):
            if (i < nalfabetoAFD):
                cadenaTerminales = cadenaTerminales + alfabetoAFD + ','
                listaaux1.append(alfabetoAFD)
                i = i + 1
            elif (i == nalfabetoAFD):
                cadenaTerminales = cadenaTerminales + alfabetoAFD
                listaaux1.append(alfabetoAFD)
                i = i + 1

    x = 0
    cadenanTerminalInicial = ''

    cn = 0
    while cn <= 0:
        estadoInicialAFD = input('Por favor ingrese el NO terminal inicial ')
        if estadoInicialAFD in listaaux:
            cadenanTerminalInicial = estadoInicialAFD
            cn = cn + 1
        else:
            cn = 0
            print('\nEl NO terminal digitado no se encuentra dentro de sus NO terminales, por favor ingrese uno que si este\n')

    cadenaProducciones = ''
    listaaux2 = []
    cn = 0
    while cn <= 0:
        global inicio, caracter_final

        transiciones1 = input(
            '\nPor favor ingrese producciones de la siguiente forma\nNO TERMINAL > EXPRESION\nNOTA** cuando'
            'desee dejar de agregar producciones en vez de la produccion escriba FIN en mayusculas\n')

        if (transiciones1 != 'FIN'):
            inicio = transiciones1.split(">")
            if inicio[0] in listaaux:
                inicio = transiciones1.split(">")
                Producciones.append(producciones(inicio[0], inicio[1]))
                cn = 0
            else:
                print('Uno o mas datos agregados no se encontraron en lo ya guardado')
        elif (
                transiciones1 == 'FIN' or transiciones1 == 'Fin' or transiciones1 == 'FIn' or transiciones1 == 'fin' or transiciones1 == 'fIN' or transiciones1 == 'fIn'):
            cn = 1
            lista_gramaticas.append(
                DatosGR(nameGR, cadenaNTerminales.split(","), cadenaTerminales.split(","), cadenanTerminalInicial,Producciones))
            moduloGR()

def validarcadenaAFD():
    global op
    op = 0
    # Menu principal y validacion de seleccion de opcion
    while op < 1 or op > 3:
        print('\n*-*-*-*-*-*-*-*-*-*-        EVALUAR CADENA         *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-1)Validar una cadena             *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-2)Ruta en AFD *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-3)regresar                       *-*-*-*-*-*-*-*-*-*-\n')
        op = int(input('Seleccione la opcion deseada: '))
        opcionErronea(op, 1, 3)
        if op is 1:
            print('A CONTINUACION SE MOSTRARA UNA LISTA CON LOS AFD EXISTENTES')
            for lA in lista_automatas:
                print(lA.nombre)
            nameAFD = input("Por favor ingrese AFD para validar una cadena:\n")
            cadena=input('Ingrese cadena para validar')
        elif op is 2:
            cadena = input('Ingrese cadena para validar')
        elif op is 3:
            moduloAfd()

def guardarAFD():
    print('A CONTINUACION SE MOSTRARA UNA LISTA CON LOS AFD EXISTENTES')
    for lA in lista_automatas:
        print(lA.nombre)
    nameAFd=input('Por favor escriba nombre de AFD para generar archivo')
    for Datos in lista_automatas:
        if(Datos.nombre==nameAFd):
            archivo = open(str(nameAFd)+".afd",'w')
            archivo.write(Datos.nombre+"\n")
            x = 1
            for estados in Datos.estados:
                if(x<len(Datos.estados)):
                    archivo.write(estados+",")
                    x+=1
                elif(x==len(Datos.estados)):
                    archivo.write(estados)
                    x+=1
            archivo.write("\n")
            x=1
            for alfabetos in Datos.alfabeto:
                if(x<len(Datos.alfabeto)):
                    archivo.write(alfabetos+",")
                    x+=1
                elif(x==len(Datos.alfabeto)):
                    archivo.write(alfabetos)
                    x+=1
            archivo.write("\n")
            archivo.write(Datos.EstadoInicial + "\n")
            x = 1
            for aceptacion in Datos.EstadoAceptacion:
                if (x < len(Datos.EstadoAceptacion)):
                    archivo.write(aceptacion + ",")
                    x += 1
                elif (x == len(Datos.EstadoAceptacion)):
                    archivo.write(aceptacion+"\n")
                    x += 1
            x = 1
            for tr in Datos.Transicioness:
                if (x < len(Datos.Transicioness)):
                    archivo.write(tr.inicio + "," + tr.dato + ";" + tr.final)
                    archivo.write("\n")
                    x += 1
                elif (x == len(Datos.Transicioness)):
                    archivo.write(tr.inicio + "," + tr.dato + ";" + tr.final+"\n")
                    archivo.write("%")
                    x += 1
            archivo.close()

def guardarGR():
    print('A CONTINUACION SE MOSTRARA UNA LISTA CON LAS GRAMATICAS EXISTENTES')
    for lA in lista_gramaticas:
        print(lA.nombre1)
    nameGR = input('Por favor escriba nombre de la gramatica para generar archivo')
    for Datos1 in lista_gramaticas:
        if (Datos1.nombre1 == nameGR):
            archivo = open(str(nameGR) + ".gre", 'w')
            archivo.write(Datos1.nombre1 + "\n")
            x = 1
            for nterminales in Datos1.nTerminales:
                if (x < len(Datos1.nTerminales)):
                    archivo.write(nterminales + ",")
                    x += 1
                elif (x == len(Datos1.nTerminales)):
                    archivo.write(nterminales)
                    x += 1
            archivo.write("\n")
            x = 1
            for alfabetos in Datos1.terminales:
                if (x < len(Datos1.terminales)):
                    archivo.write(alfabetos + ",")
                    x += 1
                elif (x == len(Datos1.terminales)):
                    archivo.write(alfabetos)
                    x += 1
            archivo.write("\n")
            archivo.write(Datos1.nTerminalInicial + "\n")
            x = 1
            for tr in Datos1.Producciones:
                if (x < len(Datos1.Producciones)):
                    archivo.write(tr.inicio + "," +tr.final)
                    archivo.write("\n")
                    x += 1
                elif (x == len(Datos1.Producciones)):
                    archivo.write(tr.inicio + ","+ tr.final + "\n")
                    archivo.write("%")
                    x += 1
            archivo.close()
def reporteAFD():
    global lista_automatas
    name = ""
    estatus=''
    alph=''
    EstInicial=''
    EstAceptac=''
    trr=''

    print('A CONTINUACION SE MOSTRARA UNA LISTA CON LOS AFD EXISTENTES')
    for lA in lista_automatas:
        print(lA.nombre)
    nameAFD = input("Por favor ingrese AFD para crear un Reporte:\n")
    for Datos in lista_automatas:
        if (Datos.nombre == nameAFD):
            name = Datos.nombre
            estatus = Datos.estados
            alph = Datos.alfabeto
            EstInicial = Datos.EstadoInicial
            EstAceptac = Datos.EstadoAceptacion
            for tr in Datos.Transicioness:
                trr = trr + "\n" + tr.inicio + "," + tr.dato + ";" + tr.final

    from graphviz import Digraph
    dot = Digraph(name='automata', encoding='UTF-8', format='pdf')
    dot.attr(rankdir='LR', layout='dot', shape='circle')
    for datosAFD in lista_automatas:
        if datosAFD.nombre == nameAFD:
            for estados in datosAFD.estados:
                if estados in datosAFD.EstadoAceptacion:
                    dot.node(name=estados, shape='doublecircle')
                else:
                    dot.node(name=estados)
    dot.node('inicio', shape='plaintext')
    dot.edge('inicio', '' + EstInicial)
    for Datos in lista_automatas:
        if Datos.nombre == nameAFD:
            for tr in Datos.Transicioness:
                dot.edge('' + tr.inicio, '' + tr.final, label=tr.dato)
    dot.node("Nombre:  " + str(name) + "\n" + " Estados:  " + ', '.join(estatus) + "\n" + " Alfabeto:  " + ', '.join(
        alph) + "\n" + " Estado Inicial:  " + str(EstInicial) + "\n"
             + " Estado de Aceptacion:  " + ', '.join(EstAceptac) + "\n" + " Trasiciones:  " + str(trr) + "\n", shape='box')
    dot.render('' + nameAFD, format='pdf', view=True)
    print("Creado")
    moduloAfd()

def reporteGR():
    global lista_gramaticas
    name = ""
    estatus = ''
    alph = ''
    EstInicial = ''
    EstAceptac = ''
    trr = ''

    print('A CONTINUACION SE MOSTRARA UNA LISTA CON LAS GRAMATICAS EXISTENTES')
    for lA in lista_gramaticas:
        print(lA.nombre1)
    nameAFD = input("Por favor ingrese Gramatica para crear un Reporte:\n")
    for Datos1 in lista_gramaticas:
        if (Datos1.nombre1 == nameAFD):
            name = Datos1.nombre1
            estatus = Datos1.nTerminales
            alph = Datos1.terminales
            EstInicial = Datos1.nTerminalInicial
            for tr in Datos1.Producciones:
                trr = trr + "\n" + tr.inicio + ">"+ tr.final
    print(estatus)
    from graphviz import Digraph
    dot = Digraph(name='automata', encoding='UTF-8', format='pdf')
    dot.attr(rankdir='LR', layout='dot', shape='circle')
    for datosAFD in lista_automatas:
        if datosAFD.nombre == nameAFD:
            for estados in datosAFD.estados:
                if estados in datosAFD.EstadoAceptacion:
                    dot.node(name=estados, shape='doublecircle')
                else:
                    dot.node(name=estados)
    dot.node('inicio', shape='plaintext')
    dot.edge('inicio', '' + EstInicial)
    for Datos in lista_automatas:
        if Datos.nombre == nameAFD:
            for tr in Datos.Transicioness:
                dot.edge('' + tr.inicio, '' + tr.final, label=tr.dato)
    dot.node("Nombre:  " + str(name) + "\n" + " No terminales:  " + ', '.join(estatus) + "\n" + " Terminales:  " + ', '.join(
        alph) + "\n" + " Terminal Inicial:  " + str(EstInicial) + "\n"+ "\n" + " Producciones:  " + str(trr) + "\n",
             shape='box')
    dot.render('' + nameAFD, format='pdf', view=True)
    print("Creado")
    moduloGR()

def crearGramatica():
    print('A CONTINUACION SE MOSTRARA UNA LISTA CON LOS AFD EXISTENTES')
    for lA in lista_automatas:
        print(lA.nombre)
    nameAFd = input('Por favor escriba nombre de AFD para generar gramatica regular \n')
    listatr = []
    for Datos in lista_automatas:
        if (Datos.nombre == nameAFd):
            for tr in Datos.Transicioness:
                if (tr.inicio not in listatr):
                    print(tr.inicio + "> " + tr.dato + " " + tr.final)
                    listatr.append(tr.inicio)
                elif(tr.inicio in listatr):
                    print("| " + tr.dato + " " + tr.final)
    REPORTAR = input('Desea generar reporte de la gramatica regular? digite SI o NO en mayuscula:  ')
    if(REPORTAR=="SI"):
        archivo = open("REPORTEGRDE"+str(nameAFd) + ".txt", 'w')
        listatr = []
        for Datos in lista_automatas:
            if (Datos.nombre == nameAFd):
                for tr in Datos.Transicioness:
                    if (tr.inicio not in listatr):
                        archivo.write(tr.inicio + "> " + tr.dato + " " + tr.final+"\n")
                        listatr.append(tr.inicio)
                    elif (tr.inicio in listatr):
                        archivo.write("| " + tr.dato + " " + tr.final+"\n")
        print(':::::Reporte creado:::::')
        archivo.close()
    if(REPORTAR=="NO"):
        moduloAfd()

def pruebamostrar():
    for lA in lista_automatas:
        print("Nombre--->"+lA.nombre)
        print("ESTADOS:")
        print(lA.estados)
        print("Alfabeto:")
        print(lA.alfabeto)
        print("Estado inicial:")
        print(lA.EstadoInicial)
        print("Estados de aceptacion:")
        print(lA.EstadoAceptacion)
        print("::::TRANSICIONES::::")
        for tr in Transicioness:
            print("Inicio: " + tr.inicio + " simbolo: " + tr.dato + " Final: " + tr.final)

    for lA in lista_gramaticas:
        print("Nombre--->"+lA.nombre1)
        print("nTerminales:")
        print(lA.nTerminales)
        print("Alfabeto:")
        print(lA.terminales)
        print("Estado inicial:")
        print(lA.nTerminalInicial)
        print("::::TRANSICIONES::::")
        for tr in Producciones:
            print("Inicio: " + tr.inicio +" Final: " + tr.final)

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
            validarcadenaAFD()
        elif op is 4:
            guardarAFD()
        elif op is 5:
            reporteAFD()
        elif op is 6:
            crearGramatica()
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
              '*-*-*-*-*-*-*-*-*-*-5)Guardar gramática en arcivo                *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-6)Generar reporte gramatica regular          *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-7)Regrear a menu principal                   *-*-*-*-*-*-*-*-*-*-\n')
        op = int(input('Seleccione la opcion deseada: '))
        opcionErronea(op, 1, 7)
        if op is 1:
            crearGR()
        elif op is 2:
            cargarArchivoGR()
        elif op is 3:
            print('holahola')
        elif op is 4:
            print('adios')
        elif op is 5:
            guardarGR()
        elif op is 6:
            reporteGR()
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
            print('\n*-*-*-*-*-*-*-*-*-*-Lenguajes Formales de Programacion Seccion E*-*-*-*-*-*-*-*-*-*-\n')
            menuPrincipal()
menuPrincipal()
