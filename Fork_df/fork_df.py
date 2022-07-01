import os
import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument('-n', type= int)
parser.add_argument ('-r', type=int)
parser.add_argument('-f')
parser.add_argument('-v')

args = parser.parse_args()

archivo = open(args.f, 'w+')
abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
for i in range(args.n):
    if os.fork() == 0:
        if args.v:
            print(f"Proceso {os.getpid()}= {abc[i]}")
        for r in range(args.r):
            archivo.write(abc[i])
            archivo.flush
        
        
        time.sleep(1)
        os.exit(0)

        
for i in range(args.n):
    os.wait()
ar2 = open(args.f, 'r')
print (ar2.readlines())