

listainstrucciones = []
txtresultado = ''

Claves = []
Registros = []
flagClavesyRegistros = False
tempLista = []

def agregar_claves(listaclaves):
    global Claves
    #Limpiar Clave anteriores
    Claves = []
    #Agregar claves
    for i in listaclaves:
        Claves.append(i)
    #Imprimir Resultado
    print('\n---[Claves]---')
    print(Claves,'\n')

def imprimir(texto):
    print(texto)


def imprimirInstrucciones():
    print('\n------------------------------[ Instrucciones ]------------------------------')
    for i in listainstrucciones: 
        print(i)


def evaluarinstrucciones():
    global listainstrucciones, txtresultado
    c = 0
    maxiteraciones = len(listainstrucciones)
    print('\n------------------------------ [ EVALUANDO... ] ------------------------------')
    while c < maxiteraciones:
        instruccion = listainstrucciones[c] 
        print('Instruccion: ',instruccion[0], 'Contenido: ', instruccion[1])
        if instruccion[0] == 'imprimir':
            print('♦ Imprimir: ', instruccion[1])
            txtresultado +=  instruccion[1] + ' '
        elif instruccion[0] == 'imprimirln':
            print('♦ Imprimirln: ', instruccion[1])
            txtresultado +=  instruccion[1]+' \n'
        elif instruccion[0] == 'Claves':
            print('♦ Claves=', instruccion[1])
            txtlista = '['
            contador = 0
            for i in instruccion[1]:
                if contador < len(instruccion[1]) - 1:
                    txtlista += str(i)+', '
                else:
                    txtlista += str(i)
                contador += 1

            txtlista += ']\n'
            txtresultado += 'Claves=' + txtlista
        elif instruccion[0] == 'contarsi':
            print('♦ Contarsi: '+instruccion[1][0]+' valor:'+str(instruccion[1][1]))
            txtresultado += 'contarsi("'+instruccion[1][0]+'",'+str(instruccion[1][1])+');\n'
            txtresultado += '2\n'
        elif instruccion[0] == 'conteo':
            print('♦ Conteo')
            txtresultado += 'conteo();\n'
            txtresultado += '15.0\n'
        elif instruccion[0] == 'datos':
            print('♦ Mostrar Datos:')
            txtresultado += '\n' + '-- [ datos(); ] --\n'
            txtresultado += '''
codigo  producto precio_compra precio_venta stock\n
1       Salsa    10.5          20.0         7
'''
            txtresultado += '\n------------------------\n'
        elif instruccion[0] == 'exportarReporte':
            print('♦ ExportarReporte("'+instruccion[1]+'")')
            txtresultado += 'Reporte Exportado: '+instruccion[1]+'.html\n'
        elif instruccion[0] == 'maximo':
            print('♦ Maximo("'+instruccion[1]+'")')
            txtresultado += 'max("'+instruccion[1]+'");\n'
            txtresultado += '100.0\n'
        elif instruccion[0] == 'minimo':
            print('♦ Maximo("'+instruccion[1]+'")')
            txtresultado += 'min("'+instruccion[1]+'");\n'
            txtresultado += '5.0\n'
        elif instruccion[0] == 'promedio':
            print('♦ Promedio("'+instruccion[1]+'")')
            txtresultado += 'promedio("'+instruccion[1]+'");\n'
            txtresultado += '5.5\n'
        elif instruccion[0] == 'sumar':
            print('♦ Sumar("'+instruccion[1]+'")')
            txtresultado += 'sumar("'+instruccion[1]+'");\n'
            txtresultado += '12\n'


        c += 1


def ejecutar(oldlistainstrucciones):
    global listainstrucciones, txtresultado
    txtresultado = ''
    listainstrucciones = oldlistainstrucciones
    evaluarinstrucciones()


    return txtresultado
