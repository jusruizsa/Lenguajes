gramatica = {
    'A': 'B C',
    'A*': 'ant A all',
    'B': 'big C',
    'B*': 'bus A boss',
    'B**': 'e',
    'C': 'cat',
    'C*': 'cow'
}

noTerminal = [rule for rule in gramatica if '*' not in rule]
terminal = []
for rule in gramatica:
    symbol = gramatica[rule].split(' ')
    for word in symbol:
        if word not in gramatica:
            terminal.append(word)


