from task import potencia, raiz, logaritmo
import sys, click


def read_matriz(path):
    with open(path, 'r') as file:
        matriz = file.readlines()
        matriz = [line.split(',') for line in matriz]
        return matriz

def calculator(fun, matriz):
    matriz_nueva: list= []
    for fila in matriz:
        fila_n = []
        for a in fila:
            a = calculate(fun, a)
            fila_n.append(a)
        matriz_nueva.append(fila_n)
    return matriz_nueva

def calculate(fun, a):
    functions = {
        'pot': potencia.delay(a),
        'raiz': raiz.delay(a),
        'log': logaritmo.delay(a)
    }
    return functions[fun]

@click.command()
@click.option('-f', '--file')
@click.option('-c', '--calcfunc')

def main():
    results = calculator(click.calcfunc, read_matriz(click.file))
    print(results)

if __name__ == '__main__':
    main()