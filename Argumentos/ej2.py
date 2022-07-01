import argparse
import os
parser = argparse.ArgumentParser(description="ej2")

parser.add_argument("-i", "--origen", type = str, help = "Archivo de origen")
parser.add_argument("-o", "--destino", type = str, help = "Archivo de destino")
args = parser.parse_args()

if os.path.isfile(args.origen):
    archivo1 = open(args.origen, "r")
    escritura = archivo1.read()
    archivo1.close()
    archivo2 = open(args.destino,"a+")
    archivo2.write(escritura)
    archivo2.close()
    print ("El contenido del archivo de origen ya esta sobreescrito en el destino")



