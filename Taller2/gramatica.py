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


string = 'abcede'
strigncopy = string.replace('f', '')
print(strigncopy)

# #GENERA LOS PRIMEROS DE LA GRAMATICA
# def primeros(rule: str):
#     symbol = rule.split(' ')
    



    




# # PROGRAMA MAIN LEE LA GRAMATICA
# rule = [rule for rule in gramatica]

# for symbol in rule:
#     setprimeros[symbol.replace()] primeros(gramatica[symbol])