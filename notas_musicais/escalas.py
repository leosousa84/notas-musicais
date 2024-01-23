
NOTAS = 'C C# d D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0,2,3,5,7,9,11)}

def escalas(tonica, tonalidade):
    """
    >>> escalas('C', 'maior')
    {'notas': ['C', 'D' , 'E' , 'F' , 'G' , 'A' , 'B'], 'graus': ['I' , 'II' , 'III' , 'IV' , 'V' , 'VI' , 'VII']}
    """
    intervalos = ESCALAS[tonalidade]

    temp = []

    for intervalo in intervalos:
        temp.append(NOTAS[intervalo])

    return {'notas': temp, 'graus': ['I' , 'II' , 'III' , 'IV' , 'V' , 'VI' , 'VII']}