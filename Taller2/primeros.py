from gramatica import gramatica, terminal, noTerminal

#ALMACENAR CONJUNTO DE PRIMEROS EN UN DICT CON VALUES LIST
setprimeros = {
    key: [] for key in gramatica if '*' not in key
}

#GENERA LOS PRIMEROS DE LA GRAMATICA
def primeros(symbol: str):
    aux_grammar = [i for i in gramatica if symbol in i]
    for rule in aux_grammar:
        temp_rule = gramatica[rule].split(' ')
        if temp_rule[0] in terminal:
            if temp_rule[0] not in setprimeros[symbol]:
                setprimeros[symbol].append(temp_rule[0])
            continue
        else:
            primeros(temp_rule[0])

for symbol in noTerminal:
    primeros(symbol)

print(f'Primeros = {setprimeros}')