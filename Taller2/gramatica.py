from lib2to3.pgen2 import grammar


gramatica = {
    'A': 'B C',
    'A*': 'ant A all',
    'B': 'big C',
    'B*': 'bus A boss',
    'B**': 'e',
    'C': 'cat',
    'C*': 'cow'
}

terminal = ['ant', 'all', 'big', 'bus', 'boss', 'e', 'cat', 'cow']
noTerminal = [rule for rule in gramatica if '*' not in rule]

setprimeros = {
    key: {} for key in gramatica if '*' not in key
}

#GENERA LOS PRIMEROS DE LA GRAMATICA
def primeros(rule: str):
    symbol = rule.split(' ')
    if symbol[0] in terminal:
        return symbol[0]
    elif symbol[0] = 
    



    




# PROGRAMA MAIN LEE LA GRAMATICA
rule = [rule for rule in gramatica]

for symbol in rule:
    setprimeros[symbol.replace('*', '')].add(primeros(gramatica[symbol]))