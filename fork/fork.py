import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-n","--num",type = int, help="Numero de procesos hijos que quiere generar")
parser.add_argument("-v", "--verbose",action= "store_true",help= "Modo verboso")

args = parser.parse_args()


def generador():
    if os.fork():
        sumatoria = sum([i for i in range(os.getpid()) if i % 2 == 0])
        if modo_verboso == True:
            print ("Starting proces " f'{os.getpid()}')
            print ("Ending proces " f'{os.getpid()}')
            print ({os.getpid()}, "-", {os.getppid()},":", {sumatoria}) 

        else:
            print ({os.getpid()}, "-", {os.getppid()},":", {sumatoria}) 

modo_verboso = False


if args.verbose:
    modo_verboso = True

if args.num > 0:
    for i in range(args.num):
        generador()

