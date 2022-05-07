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

primeros = {

}



def primeros(rule):
    pos = 0
    for rule in gramatica:
        # print(gramatica[rule].split(' '))
        for word in gramatica[rule].split(' '):
            if word in terminal:
                primeros[rule] = 
                continue
            else:
                continue




# PROGRAMA MAIN
rule = [rule for rule in gramatica]
for symbol in rule:
    primeros(gramatica[rule])