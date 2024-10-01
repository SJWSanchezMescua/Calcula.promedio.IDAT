notas = {'ec01': 13, 'ec02': 0, 'ec03': 14, 'ecf': 15}
pesos = {'ec01': 0.04, 'ec02': 0.12, 'ec03': 0.24, 'ecf': 0.60}

pf = sum(notas[key] * pesos[key] for key in notas)
print('Promedio final:', pf)