from math import sqrt, log10
from config import app

@app.task
def potencia(a):
    return a**a

@app.task
def raiz(a):
    return sqrt(a)

@app.task
def logaritmo(a):
    return log10(a)