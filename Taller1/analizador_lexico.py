import re
import sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

reservadas = [
    'and', 'archivo', 'caso', 'const', 'constantes', 'desde', 'eval', 'fin',
    'hasta', 'inicio', 'lib', 'libext', 'matriz', 'mientras', 'not', 'or',
    'paso', 'subrutina', 'programa', 'ref', 'registro', 'repetir', 'retorna', 'si',
    'sino', 'tipos', 'var', 'variables', 'vector', 'numerico', 'imprimir', 'tan', 'logico',
    'TRUE', 'FALSE', 'SI', 'NO', 'leer', 'cadena', 'dim', 'int', 'cos', 'sin', 'cls', 'set_ifs', 
    'abs', 'arctan', 'ascii','dec', 'eof', 'exp', 'get_ifs', 'inc', 'log', 'lower', 'mem',
    'ord', 'paramval', 'pcount', 'pos', 'random', 'sec', 'set_stdin', 'set_stdout', 'sqrt',
    'str', 'strdup', 'strlen', 'substr', 'upper', 'val', 'alen'
]

exp_reg = {
    'NUMERO': r'([-+]?[0-9]+(\.[0-9]+)?([eE][-+]?[0-9]+)?)',
    'COMENTARIO_LINEA': r'([/]+[/]+.*)',
    'COMENTARIO_BLOQUE': r'([/]+[*]+.*)',
    'ID': r'([A-Za-zÑñ_]+[0-9A-Za-zÑn_]*)',
    'OPERADORES': r'([+\-*/>=<^%])',
    'SIMBOLOS': r'([\,\]\[:}{)(\.;])',
    'CADENA': r'([", \']{1})'
}



fila = 1
buscarFin = False


#Funciones

def return_string(line, pattern):
    
    match = re.split(exp_reg[pattern], line)
    if len(match) == 1:
        return match[0]
    return match[1]


#Define el tipo de token de cada parte de la linea
def return_type(line):

    if re.compile(exp_reg['OPERADORES']).match(line):
        return 'OPERADORES'
    elif re.compile(exp_reg['NUMERO']).match(line):
        return 'NUMERO'

    elif re.compile(exp_reg['ID']).match(line):
        return 'ID'

    elif re.compile(exp_reg['OPERADORES']).match(line):
        return 'OPERADORES'

    elif re.compile(exp_reg['SIMBOLOS']).match(line):
        return 'SIMBOLOS'

    elif re.compile(exp_reg['CADENA']).match(line):
        return 'CADENA'

line = ' '

while line:
    line = sys.stdin.readline()
    aux_line = line.strip()
    buffer = ''
    id = ''
    
    if line == '\n':
        fila += 1
        continue

    #COMENTARIOS
    #Si es un comentario de la forma // saltar linea
    if re.compile(exp_reg['COMENTARIO_LINEA']).match(line):
        fila += 1
        continue

    #Si es un comentario de la forma /* buscar la cadena */ saltar linea si no existe en la actual
    if re.compile(exp_reg['COMENTARIO_BLOQUE']).match(line):
        buscarFin = True
    if buscarFin:
        if re.search(re.compile(r'[*]+[/]'), line):
            buscarFin = False
            index = aux_line.index('*/') + 2
            aux_line = aux_line[index:]
        else:
            fila += 1
            continue

    #Clasificar cada palabra en la cadena de entrada
    while buffer != '\n':
        
        if aux_line == '':
            break
        
        if buffer != '':
            aux_line = buffer.strip()


        if aux_line == id:
            index = len(line) - 1

        else:
            index = line.index(aux_line)

        #Si es un comentario de la forma // saltar linea despues de una linea valida
        if re.compile(exp_reg['COMENTARIO_LINEA']).match(aux_line):
            break

        if re.compile(exp_reg['COMENTARIO_BLOQUE']).match(aux_line):
            buscarFin = True
            break
        
        try:
            #NUMEROS
            if return_type(aux_line) == 'NUMERO':
                id = return_string(aux_line, 'NUMERO')
                buffer = aux_line.replace(id, '', 1)
                if buffer == 'e' or buffer == 'E' or buffer == 'E+' or buffer == 'E-' or buffer == 'e-' or buffer == 'e+':
                    print(f'>>> Error lexico(linea:{fila},posicion:{line.index(aux_line)+1})')
                    exit()
                if line.count(aux_line) > 1:
                    index = line.index(aux_line)
                    print(f'<tk_numero,{id},{fila},{line.index(aux_line, index+1)+1}>')
                else:
                    print(f'<tk_numero,{id},{fila},{line.index(aux_line)+1}>')



            #IDENTIFICADORES
            elif return_type(aux_line) == 'ID':
                id = return_string(aux_line, 'ID')
                buffer = aux_line.replace(id, '', 1)

                # Verificar si el ID es una palabra reservada
                if id in reservadas:
                    if line.count(aux_line) > 1:
                        if aux_line == id:
                            print(f'<{id},{fila},{line.index(aux_line, len(line)-len(id)-1)+1}>')
                        else:
                            index = line.index(aux_line)
                            print(f'<{id},{fila},{line.index(aux_line, index+1)+1}>')
                    elif line.index(buffer) == 0:
                        print(f'<{id},{fila},{line.index(aux_line)+1}>')
                    else: 
                        print(f'<{id},{fila},{line.index(aux_line)+1}>')
                else:
                    if aux_line == id:
                        print(f'<id,{id},{fila},{line.index(aux_line, len(line)-len(id)-1)+1}>')
                    elif line.count(aux_line) > 1:
                        index = line.index(aux_line)
                        print(f'<id,{id}, {fila},{line.index(aux_line, index+1)+1}>')
                    else:
                        print(f'<id,{id},{fila},{line.index(aux_line)+1}>')

            #OPERADORES
            elif return_type(aux_line) == 'OPERADORES':
                id = return_string(aux_line, 'OPERADORES')
                buffer = aux_line.replace(id, '', 1)

                # print(f'buffer[0] = {buffer[0]}')
                
                if (id == '=' or id == '<' or id == '>') and buffer != '' and buffer[0] == '=':
                    id += '='
                    buffer = buffer[1:]
                    
                    if id == '==':
                        print(f'<tk_igual_que,{fila},{index+1}>')
                    elif id == '<=':
                        print(f'<tk_menor_igual,{fila},{index+1}>')
                    elif id == '>=':
                        print(f'<tk_mayor_igual,{fila},{index+1}>')

                elif id == '<' and buffer != '' and buffer[0] == '>':
                    print(f'<tk_distinto_de,{fila},{index+1}>')
                    buffer = buffer[1:]
                elif id == '=':
                    print(f'<tk_asignacion,{fila},{index+1}>')
                elif id == '<':
                    print(f'<tk_menor,{fila},{index+1}>')
                elif id == '>':
                    print(f'<tk_mayor,{fila},{index+1}>')
                elif id == '+':
                    print(f'<tk_suma,{fila},{index+1}>')
                elif id == '-':
                    print(f'<tk_resta,{fila},{index+1}>')
                elif id == '/':
                    print(f'<tk_division,{fila},{index+1}>')
                elif id == '*':
                    print(f'<tk_multiplicacion,{fila},{index+1}>')
                elif id == '^':
                    print(f'<tk_potenciacion,{fila},{index+1}>')
                elif id == '%':
                    print(f'<tk_modulo,{fila},{index+1}>')

            #SIMBOLOS
            elif return_type(aux_line) == 'SIMBOLOS':
                id = return_string(aux_line, 'SIMBOLOS')
                buffer = aux_line.replace(id, '', 1)

                if id == '(':
                    print(f'<tk_parentesis_izquierdo,{fila},{index+1}>')
                if id == ',':
                    print(f'<tk_coma,{fila},{index+1}>')
                if id == ')':
                    print(f'<tk_parentesis_derecho,{fila},{index+1}>')
                if id == ']':
                    print(f'<tk_corchete_derecho,{fila},{index+1}>')
                if id == '[':
                    print(f'<tk_corchete_izquierdo,{fila},{index+1}>')
                if id == ':':
                    print(f'<tk_dos_puntos,{fila},{index+1}>')
                if id == '}':
                    print(f'<tk_llave_derecha,{fila},{index+1}>')
                if id == '{':
                    print(f'<tk_llave_izquierda,{fila},{index+1}>')
                if id == ';':
                    print(f'<tk_punto_y_coma,{fila},{index+1}>')
                if id == '.':
                    print(f'<tk_punto,{fila},{index+1}>')

            

            #CADENAS
            elif return_type(aux_line) == 'CADENA':
                id = return_string(aux_line, 'CADENA')
                buffer = aux_line.replace(id, '', 1)
                try:

                    if len(id) > 32:
                        print(f'>>> Error lexico(linea:{fila},posicion:{index+1})')
                        exit()

                    if id == '"':
                        index = buffer.index('"')
                        id = id + buffer[:index+1]
                        buffer = buffer[index+1:]
                        print(f'<tk_cadena,{id},{fila},{index+1}>')

                    elif id == "'":
                        index = buffer.index("'")
                        id = id + buffer[:index+1]
                        buffer = buffer[index+1:]
                    
                        print(f'<tk_cadena,{id},{fila},{index+1}>')

                except ValueError:
                    print(f'>>> Error lexico(linea:{fila},posicion:{index+1})')
                    exit()

            #Error lexico
            elif aux_line != None and id != '\n':
                print(f'>>> Error lexico(linea:{fila},posicion:{index+1})')
                exit()

        except (IndexError) as e:
            pass

        
        if buffer == '':
            buffer = '\n'

        print(f'id = {id}')
        print(f'aux_line = {aux_line}')
        print(f'index = {index}')
        

    fila += 1