
listaSintactico = []
listaErroresSintactico = []
listatokens = []
listasimbolos = ['{','}',':','[',']',',','(',')',';','=','"',"'",'#','_','-']
listaletras = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','Ñ','ñ']



def imprimirErrores():
    print('\n############[ Errores | Sintactico]#################\n')
    for i in listaErroresSintactico: 
        print(i)


def imprimirlistaSintactico():
    print('\n############[ Lista Sintactico | Instrucciones]#################\n')
    for i in listaSintactico:
        print(i)


def obtenertexto(a):
    global listatokens
    inicio = a
    texto = ''
    #-----
    maxiteraciones = len(listatokens)
    while a < maxiteraciones:
        token = listatokens[a][1]
        if token == '"' or token == "'":
            a += 1
            return [texto,a]
        else:
            texto += token
            a += 1


def fininstruccion(a,tokenesperado):
    global listatokens, listaErroresSintactico
    inicio = a
    maxiteraciones = len(listatokens)
    while a < maxiteraciones:
        token = listatokens[a][1]
        if token == ';' or token == '\n':
            a += 1
            #Agregar a errores
            listaErroresSintactico.append([listatokens[inicio][1],str(tokenesperado),listatokens[inicio][1],listatokens[inicio][2],'error Sintactico',listatokens[inicio][1],listatokens[a-1][2]])
            return a
        else:
            a += 1


def ErrorAFDTextoentrecomillas(a,tokenesperado):
    global listatokens, listaErroresSintactico
    inicio = a
    maxiteraciones = len(listatokens)
    while a < maxiteraciones:
        token = listatokens[a][1]
        if token == ')' or token == ';' or token == '\n':
            a += 1
            #Agregar a errores
            listaErroresSintactico.append([listatokens[a-1][1],str(tokenesperado),listatokens[a-1][1],listatokens[a-2][2],'error Sintactico',listatokens[a-1][1],listatokens[a-1][2]])
            return a
        else:
            a += 1



def AFDTextoentrecomillas(c):
    global listatokens
    #iterador
    maxiteraciones = len(listatokens)
    #TEXTO
    texto = ''
    #Estados
    #q1,q2,q3,q4,q5
    inicio = 0
    final = 5
    estado = inicio

    if listatokens[c][1] == '"':
        estado = 1
        c+=1
        while c < maxiteraciones:
            #Token
            token = listatokens[c][1]
            if token == ')' or token == ';' or token == '\n':
                return False
            elif token == '"':
                estado = 5
                c+=1
                return True
            elif token in listaletras:
                estado = 2
                c+=1
            elif token in listasimbolos:
                estado = 3
                c+=1
            elif token.isdigit():
                estado = 4
                c+=1
            else:
                c+=1
        
        return False

def getTextoentrecomillas(c):
    global listatokens
    #iterador
    maxiteraciones = len(listatokens)
    #TEXTO
    texto = ''
    if listatokens[c][1] == '"':
        c+=1
        while c < maxiteraciones:
            #Token
            token = listatokens[c][1]
            if token == '"':
                c+=1
                return texto, c
            elif token in listaletras or token in listasimbolos:
                #Añadir token
                texto += token
                c+=1
            else:
                c+=1



def evaluartokens(tokens):
    global listaSintactico, listatokens
    listatokens = tokens
    print('\n####### [ EVALUAR TOKENS ] #######')
    #Iterador
    c = 0
    maxiteraciones = len(tokens)
    while c < maxiteraciones:
        Token = tokens[c][1]
        #Ignorar Comentarios
        if tokens[c][4] == 'Comentario_multilinea' or tokens[c][3] == 'Comentario_simple':
            c += 1    
        elif Token == 'i':
            if tokens[c+1][1] == 'm':
                if tokens[c+2][1] == 'p':
                    if tokens[c+3][1] == 'r':
                        if tokens[c+4][1] == 'i':
                            if tokens[c+5][1] == 'm':
                                if tokens[c+6][1] == 'i':
                                    if tokens[c+7][1] == 'r':
                                        if tokens[c+8][1] == '(':
                                            if tokens[c+9][1] == '"':
                                                AFDTexto = AFDTextoentrecomillas(c+9)
                                                print("AFD:", AFDTexto)
                                                if AFDTexto == True:
                                                    # texto, a =getTextoentrecomillas(c+9)
                                                    #ObtenerTexto
                                                    texto, a = obtenertexto(c+10)
                                                    print('TEXTO: ', texto, ' A:',a)
                                                    #cambiar numero iteracion
                                                    c = a 
                                                    if tokens[c][1] == ')':
                                                        if tokens[c+1][1] == ';':
                                                            c += 2
                                                            listaSintactico.append(['imprimir',texto])
                                                        else:
                                                            c = fininstruccion(c+1,';')
                                                    else:
                                                        c = fininstruccion(c,')')
                                                else:
                                                    c = ErrorAFDTextoentrecomillas(c+10,'"')
                                                    c = fininstruccion(c,')')
                                            else:
                                                c = fininstruccion(c+9,'"')
                                        else:
                                            if tokens[c+8][1] == 'l':
                                                if tokens[c+9][1] == 'n':
                                                    if tokens[c+10][1] == '(':
                                                        if tokens[c+11][1] == '"':
                                                            AFDTexto = AFDTextoentrecomillas(c+11)
                                                            print("AFD:", AFDTexto)
                                                            if AFDTexto == True:
                                                                #ObtenerTexto
                                                                texto, a = obtenertexto(c+12)
                                                                print('TEXTO: ', texto, ' A:',a)
                                                                c = a
                                                                if tokens[c][1] == ')':
                                                                    if tokens[c+1][1] == ';':
                                                                        print('imprimirln: ', texto)
                                                                        listaSintactico.append(['imprimirln',texto])
                                                                    else:
                                                                        c = fininstruccion(c+1,';')
                                                                else:
                                                                    c = fininstruccion(c,')')
                                                            else:
                                                                c = ErrorAFDTextoentrecomillas(c+10,'"')
                                                                c = fininstruccion(c,')')
                                                        else:
                                                            c = fininstruccion(c+11,'"')
                                                    else:
                                                        c = fininstruccion(c+10,'(')
                                                else:
                                                    c = fininstruccion(c+9,'n')
                                            else:
                                                c = fininstruccion(c+8,'( | l ')
                                    else:
                                        c = fininstruccion(c+7,'r')
                                else:
                                    c = fininstruccion(c+6,'i')
                            else:
                                c = fininstruccion(c+5,'m')
                        else:
                            c = fininstruccion(c+4,'i')
                    else:
                        c = fininstruccion(c+3,'r')
                else:
                    c = fininstruccion(c+2,'p')
            else:
                c = fininstruccion(c+1,'m')
        else:
            print(tokens[c])
            c += 1
    
def GetErrores():
    return listaErroresSintactico


def GetInstrucciones(tokens):
    global listaSintactico, listaErroresSintactico
    listaSintactico = []
    listaErroresSintactico = []

    #Evaluar tokens
    evaluartokens(tokens)

    return listaSintactico

